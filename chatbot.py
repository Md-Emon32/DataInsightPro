import pandas as pd
import numpy as np
import os
import re
import plotly.express as px
import plotly.graph_objects as go
from typing import Tuple, Dict, List, Any, Optional, Union
import json
from openai import OpenAI
import streamlit as st

# Initialize OpenAI client
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def process_query(user_query: str, data: pd.DataFrame) -> Tuple[str, Optional[go.Figure]]:
    """
    Process a natural language query about the data and return a response with optional visualization.
    
    Args:
        user_query: The user's question or command
        data: The DataFrame being analyzed
        
    Returns:
        Tuple containing the text response and an optional Plotly figure
    """
    if not OPENAI_API_KEY:
        return ("Please set up the OPENAI_API_KEY environment variable to enable the chat functionality. " +
                "Contact your administrator for more information."), None
    
    try:
        # Prepare data information for the model
        data_info = _prepare_data_info(data)
        
        # Generate response using OpenAI
        response = _generate_ai_response(user_query, data_info, data)
        
        # Parse the response to extract any visualization requests
        text_response, visualization = _parse_visualization_request(response, data)
        
        return text_response, visualization
    
    except Exception as e:
        error_message = f"Sorry, I encountered an error while processing your request: {str(e)}"
        return error_message, None

def _prepare_data_info(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Prepare a summary of the DataFrame structure for the model.
    """
    # Basic DataFrame info
    info = {
        "rows": len(data),
        "columns": list(data.columns),
        "column_types": {col: str(dtype) for col, dtype in data.dtypes.items()},
        "column_examples": {},
        "column_stats": {}
    }
    
    # Generate examples and stats for each column
    for col in data.columns:
        # Get examples
        non_null_vals = data[col].dropna()
        if not non_null_vals.empty:
            examples = non_null_vals.sample(min(3, len(non_null_vals))).tolist()
            info["column_examples"][col] = examples
        
        # Generate stats for numeric columns
        if pd.api.types.is_numeric_dtype(data[col]):
            info["column_stats"][col] = {
                "min": float(data[col].min()) if not pd.isna(data[col].min()) else None,
                "max": float(data[col].max()) if not pd.isna(data[col].max()) else None,
                "mean": float(data[col].mean()) if not pd.isna(data[col].mean()) else None,
                "median": float(data[col].median()) if not pd.isna(data[col].median()) else None,
                "missing_count": int(data[col].isna().sum()),
                "missing_percentage": float(data[col].isna().mean() * 100)
            }
        # Generate stats for categorical columns
        elif pd.api.types.is_object_dtype(data[col]):
            value_counts = data[col].value_counts().head(5).to_dict()
            info["column_stats"][col] = {
                "unique_count": int(data[col].nunique()),
                "top_values": {str(k): int(v) for k, v in value_counts.items()},
                "missing_count": int(data[col].isna().sum()),
                "missing_percentage": float(data[col].isna().mean() * 100)
            }
        # Generate stats for datetime columns
        elif pd.api.types.is_datetime64_dtype(data[col]):
            info["column_stats"][col] = {
                "min": str(data[col].min()) if not pd.isna(data[col].min()) else None,
                "max": str(data[col].max()) if not pd.isna(data[col].max()) else None,
                "missing_count": int(data[col].isna().sum()),
                "missing_percentage": float(data[col].isna().mean() * 100)
            }
    
    return info

def _generate_ai_response(query: str, data_info: Dict[str, Any], data: pd.DataFrame) -> str:
    """
    Generate a response using the OpenAI API.
    """
    # Create a simplified dataset sample for context
    try:
        # Create a small sample of the data as context
        sample_rows = min(5, len(data))
        data_sample = data.head(sample_rows).to_string()
    except:
        data_sample = "Error creating data sample"
    
    # Prepare the system message with instructions
    system_message = f"""
    You are a helpful data analyst assistant. You help users understand their data and answer questions about it.
    Your responses should be clear, informative, and based only on the data provided.
    
    When the user asks for a visualization, include a JSON specification in your response enclosed in 
    ```visualization_json
    {{
        "type": "scatter",  // Options: "scatter", "bar", "line", "histogram", "box", "heatmap"
        "x": "column_name",  // X-axis column
        "y": "column_name",  // Y-axis column (optional for some chart types)
        "color": "column_name",  // Color column (optional)
        "title": "Chart Title"
    }}
    ```
    
    Use proper data analysis terminology and provide specific insights from the data.
    
    Here is the data information:
    - Rows: {data_info['rows']}
    - Columns: {', '.join(data_info['columns'])}
    
    Column details:
    {json.dumps(data_info['column_types'], indent=2)}
    
    Statistical information:
    {json.dumps(data_info['column_stats'], indent=2)}
    
    Here's a sample of the data:
    {data_sample}
    """
    
    # Generate the AI response
    try:
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # do not change this unless explicitly requested by the user
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": query}
            ],
            temperature=0.3,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error generating AI response: {str(e)}")

def _parse_visualization_request(response: str, data: pd.DataFrame) -> Tuple[str, Optional[go.Figure]]:
    """
    Parse the AI response to extract any visualization requests and generate the appropriate chart.
    """
    # Check if the response contains a visualization spec
    viz_match = re.search(r'```visualization_json\s*(.*?)\s*```', response, re.DOTALL)
    
    if not viz_match:
        # No visualization requested
        return response, None
    
    # Extract and parse the visualization JSON
    try:
        viz_json_str = viz_match.group(1)
        viz_spec = json.loads(viz_json_str)
        
        # Create the visualization
        chart = _create_visualization(viz_spec, data)
        
        # Remove the JSON spec from the response
        clean_response = response.replace(viz_match.group(0), "")
        
        return clean_response, chart
    
    except Exception as e:
        # If there's an error parsing or creating the visualization,
        # return the original response with an error note
        error_note = f"\n\nNote: I tried to create a visualization but encountered an error: {str(e)}"
        return response + error_note, None

def _create_visualization(viz_spec: Dict[str, Any], data: pd.DataFrame) -> go.Figure:
    """
    Create a visualization based on the specification.
    """
    chart_type = viz_spec.get("type", "").lower()
    x_col = viz_spec.get("x")
    y_col = viz_spec.get("y")
    color_col = viz_spec.get("color")
    title = viz_spec.get("title", "Data Visualization")
    
    # Input validation
    if not x_col or x_col not in data.columns:
        raise ValueError(f"Invalid or missing x column: {x_col}")
    
    if chart_type in ["scatter", "line", "bar"] and (not y_col or y_col not in data.columns):
        raise ValueError(f"Invalid or missing y column: {y_col}")
    
    if color_col and color_col not in data.columns:
        color_col = None  # Ignore invalid color column
    
    # Create the appropriate chart
    if chart_type == "scatter":
        fig = px.scatter(data, x=x_col, y=y_col, color=color_col, title=title)
    
    elif chart_type == "bar":
        fig = px.bar(data, x=x_col, y=y_col, color=color_col, title=title)
    
    elif chart_type == "line":
        fig = px.line(data, x=x_col, y=y_col, color=color_col, title=title)
    
    elif chart_type == "histogram":
        fig = px.histogram(data, x=x_col, color=color_col, title=title)
    
    elif chart_type == "box":
        fig = px.box(data, x=x_col, y=y_col, color=color_col, title=title)
    
    elif chart_type == "heatmap":
        # For heatmap, we need to prepare a correlation matrix
        if not y_col:
            # If y_col is not specified, create a correlation heatmap
            numeric_data = data.select_dtypes(include=['number'])
            if numeric_data.empty:
                raise ValueError("No numeric columns available for correlation heatmap")
            
            corr_matrix = numeric_data.corr()
            fig = px.imshow(
                corr_matrix,
                text_auto='.2f',
                aspect='auto',
                color_continuous_scale='RdBu_r',
                title=title or "Correlation Heatmap"
            )
        else:
            # Custom heatmap based on two columns
            fig = px.density_heatmap(data, x=x_col, y=y_col, title=title)
    
    else:
        raise ValueError(f"Unsupported chart type: {chart_type}")
    
    # Apply consistent styling
    fig.update_layout(
        plot_bgcolor='white',
        hovermode='closest'
    )
    
    return fig
