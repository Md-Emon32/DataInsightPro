import os
import json
import re
import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from openai import OpenAI
import anthropic
import streamlit as st

# Initialize API clients
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None

def generate_enhanced_insights(data: pd.DataFrame, provider: str = "openai") -> Dict[str, Any]:
    """
    Generate AI-enhanced insights from data using the specified AI provider.
    
    Args:
        data: Input DataFrame
        provider: AI provider to use ("openai" or "anthropic")
        
    Returns:
        Dictionary containing enhanced insights
    """
    # Quick validation
    if provider == "openai" and not OPENAI_API_KEY:
        return {"error": "OpenAI API key not set. Please configure the OPENAI_API_KEY environment variable."}
    
    if provider == "anthropic" and not ANTHROPIC_API_KEY:
        return {"error": "Anthropic API key not set. Please configure the ANTHROPIC_API_KEY environment variable."}
    
    # Prepare data information
    data_info = _prepare_data_info(data)
    
    # Generate insights using the selected provider
    if provider == "anthropic":
        insights = _generate_anthropic_insights(data_info, data)
    else:  # Default to OpenAI
        insights = _generate_openai_insights(data_info, data)
    
    return insights

def _prepare_data_info(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Prepare a comprehensive summary of the DataFrame structure for AI models.
    """
    # Basic DataFrame info
    info = {
        "rows": len(data),
        "columns": list(data.columns),
        "column_types": {col: str(dtype) for col, dtype in data.dtypes.items()},
        "column_examples": {},
        "column_stats": {},
        "missing_values": {col: int(data[col].isna().sum()) for col in data.columns},
        "missing_percentage": {col: float(data[col].isna().mean() * 100) for col in data.columns}
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
            numeric_data = data[col].dropna()
            if not numeric_data.empty:
                info["column_stats"][col] = {
                    "min": float(numeric_data.min()),
                    "max": float(numeric_data.max()),
                    "mean": float(numeric_data.mean()),
                    "median": float(numeric_data.median()),
                    "std": float(numeric_data.std()),
                    "skew": float(numeric_data.skew()) if len(numeric_data) > 2 else 0,
                    "unique_count": int(numeric_data.nunique()),
                    "zeros_count": int((numeric_data == 0).sum()),
                    "zeros_percentage": float(((numeric_data == 0).sum() / len(numeric_data)) * 100)
                }
            
        # Generate stats for categorical columns
        elif pd.api.types.is_object_dtype(data[col]):
            cat_data = data[col].dropna()
            if not cat_data.empty:
                value_counts = cat_data.value_counts().head(5).to_dict()
                info["column_stats"][col] = {
                    "unique_count": int(cat_data.nunique()),
                    "top_values": {str(k): int(v) for k, v in value_counts.items()},
                    "unique_percentage": float((cat_data.nunique() / len(cat_data)) * 100)
                }
            
        # Generate stats for datetime columns
        elif pd.api.types.is_datetime64_dtype(data[col]):
            date_data = data[col].dropna()
            if not date_data.empty:
                info["column_stats"][col] = {
                    "min": str(date_data.min()),
                    "max": str(date_data.max()),
                    "range_days": int((date_data.max() - date_data.min()).days),
                    "unique_dates": int(date_data.dt.date.nunique()),
                    "weekday_distribution": date_data.dt.dayofweek.value_counts().to_dict(),
                    "unique_percentage": float((date_data.nunique() / len(date_data)) * 100)
                }
    
    # Calculate correlations for numeric columns
    numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
    if len(numeric_cols) > 1:
        try:
            corr_matrix = data[numeric_cols].corr().round(2)
            # Filter to significant correlations (absolute value > 0.5)
            significant_corrs = []
            for i, col1 in enumerate(corr_matrix.columns):
                for j, col2 in enumerate(corr_matrix.columns):
                    if i < j:  # Only take pairs once and ignore self-correlations
                        corr_val = corr_matrix.iloc[i, j]
                        if abs(corr_val) > 0.5:  # Significant threshold
                            significant_corrs.append({
                                "col1": col1, 
                                "col2": col2, 
                                "correlation": float(corr_val),
                                "correlation_type": "positive" if corr_val > 0 else "negative"
                            })
            
            info["correlations"] = significant_corrs
        except:
            info["correlations"] = []
    else:
        info["correlations"] = []
    
    return info

def _generate_openai_insights(data_info: Dict[str, Any], data: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate insights using OpenAI API.
    """
    # Create a small sample of the data as context
    try:
        sample_rows = min(5, len(data))
        data_sample = data.head(sample_rows).to_string()
    except:
        data_sample = "Error creating data sample"
    
    # Prepare the system message with detailed instructions
    system_message = f"""
    You are an expert data analyst. You're tasked with analyzing a dataset and generating insightful observations.
    
    Please generate the following insights categories:
    1. General Insights - Overall patterns and notable characteristics of the dataset
    2. Data Quality Insights - Observations about missing values, outliers, and data quality issues
    3. Statistical Insights - Key statistical findings about numeric columns
    4. Trend Insights - Patterns over time if datetime data is present
    5. Correlation Insights - Relationships between variables
    6. Actionable Recommendations - Concrete suggestions based on the data
    
    Format your response as a JSON object with the following structure:
    {{
        "general_insights": [list of string insights],
        "data_quality_insights": [list of string insights],
        "statistical_insights": [list of string insights],
        "trend_insights": [list of string insights],
        "correlation_insights": [list of string insights],
        "recommendations": [list of string recommendations],
        "potential_visualizations": [
            {{
                "title": "visualization title",
                "description": "what this visualization would show",
                "type": "chart type (e.g., bar, scatter, line)",
                "columns": ["relevant columns"]
            }}
        ]
    }}
    
    Important guidelines:
    - Provide 3-6 insights for each category
    - Be specific and reference actual values from the data
    - For recommendations, suggest practical next steps for further analysis
    - For visualizations, suggest 2-4 informative visualizations that would reveal patterns
    - Focus on quality over quantity
    
    Here is the data information:
    
    Dataset Size: {data_info['rows']} rows with {len(data_info['columns'])} columns
    
    Column Types:
    {json.dumps(data_info['column_types'], indent=2)}
    
    Column Statistics:
    {json.dumps(data_info['column_stats'], indent=2)}
    
    Missing Values:
    {json.dumps(data_info['missing_values'], indent=2)}
    
    Correlations:
    {json.dumps(data_info['correlations'], indent=2)}
    
    Here's a sample of the data:
    {data_sample}
    """
    
    # Generate insights using OpenAI
    try:
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # do not change this unless explicitly requested by the user
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": "Generate comprehensive data insights based on the provided information."}
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
            max_tokens=1500
        )
        
        # Parse the response JSON
        insights_json = json.loads(response.choices[0].message.content)
        return insights_json
    except Exception as e:
        return {
            "error": f"Failed to generate insights using OpenAI: {str(e)}",
            "general_insights": ["Error generating AI-powered insights."]
        }

def _generate_anthropic_insights(data_info: Dict[str, Any], data: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate insights using Anthropic API.
    """
    # Create a small sample of the data as context
    try:
        sample_rows = min(5, len(data))
        data_sample = data.head(sample_rows).to_string()
    except:
        data_sample = "Error creating data sample"
    
    # Prepare the prompt with detailed instructions
    prompt = f"""
    You are an expert data analyst. You're tasked with analyzing a dataset and generating insightful observations.
    
    Please generate the following insights categories:
    1. General Insights - Overall patterns and notable characteristics of the dataset
    2. Data Quality Insights - Observations about missing values, outliers, and data quality issues
    3. Statistical Insights - Key statistical findings about numeric columns
    4. Trend Insights - Patterns over time if datetime data is present
    5. Correlation Insights - Relationships between variables
    6. Actionable Recommendations - Concrete suggestions based on the data
    
    Format your response as a JSON object with the following structure:
    {{
        "general_insights": [list of string insights],
        "data_quality_insights": [list of string insights],
        "statistical_insights": [list of string insights],
        "trend_insights": [list of string insights],
        "correlation_insights": [list of string insights],
        "recommendations": [list of string recommendations],
        "potential_visualizations": [
            {{
                "title": "visualization title",
                "description": "what this visualization would show",
                "type": "chart type (e.g., bar, scatter, line)",
                "columns": ["relevant columns"]
            }}
        ]
    }}
    
    Important guidelines:
    - Provide 3-6 insights for each category
    - Be specific and reference actual values from the data
    - For recommendations, suggest practical next steps for further analysis
    - For visualizations, suggest 2-4 informative visualizations that would reveal patterns
    - Focus on quality over quantity
    
    Here is the data information:
    
    Dataset Size: {data_info['rows']} rows with {len(data_info['columns'])} columns
    
    Column Types:
    {json.dumps(data_info['column_types'], indent=2)}
    
    Column Statistics:
    {json.dumps(data_info['column_stats'], indent=2)}
    
    Missing Values:
    {json.dumps(data_info['missing_values'], indent=2)}
    
    Correlations:
    {json.dumps(data_info['correlations'], indent=2)}
    
    Here's a sample of the data:
    {data_sample}
    """
    
    # Generate insights using Anthropic
    try:
        # the newest Anthropic model is "claude-3-5-sonnet-20241022" which was released October 22, 2024
        message = anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1500,
            temperature=0.2,
            system="You are an expert data analyst. Provide detailed insights only based on the data provided. Present your analysis in well-structured JSON format.",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract and parse the JSON response
        content = message.content[0].text
        
        # Try to extract JSON from the response if it's wrapped in code blocks
        if "```json" in content:
            json_text = content.split("```json")[1].split("```")[0].strip()
            insights_json = json.loads(json_text)
        else:
            # Otherwise try to parse the entire response as JSON
            insights_json = json.loads(content)
            
        return insights_json
    except Exception as e:
        return {
            "error": f"Failed to generate insights using Anthropic: {str(e)}",
            "general_insights": ["Error generating AI-powered insights."]
        }

def format_insights_for_display(insights: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format AI-generated insights for better display in the UI.
    
    Args:
        insights: Raw insights from AI
        
    Returns:
        Formatted insights ready for display
    """
    formatted = {}
    
    # Check for error
    if "error" in insights:
        return {
            "error": insights["error"],
            "general_insights": ["Error generating AI-powered insights. Please check the API keys."]
        }
    
    # Format general insights
    if "general_insights" in insights:
        formatted["general_insights"] = insights["general_insights"]
    
    # Format data quality insights
    if "data_quality_insights" in insights:
        formatted["data_quality_insights"] = insights["data_quality_insights"]
    
    # Format statistical insights
    if "statistical_insights" in insights:
        formatted["statistical_insights"] = insights["statistical_insights"]
    
    # Format trend insights
    if "trend_insights" in insights:
        formatted["trend_insights"] = insights["trend_insights"]
    
    # Format correlation insights
    if "correlation_insights" in insights:
        formatted["correlation_insights"] = insights["correlation_insights"]
    
    # Format recommendations
    if "recommendations" in insights:
        formatted["recommendations"] = insights["recommendations"]
    
    # Format visualization suggestions
    if "potential_visualizations" in insights:
        formatted["visualizations"] = []
        for viz in insights["potential_visualizations"]:
            formatted["visualizations"].append({
                "title": viz.get("title", "Visualization"),
                "description": viz.get("description", ""),
                "type": viz.get("type", "bar"),
                "columns": viz.get("columns", [])
            })
    
    return formatted

def generate_insight_highlights(data: pd.DataFrame, max_insights: int = 3) -> List[str]:
    """
    Generate a short list of the most important insights about the data.
    
    Args:
        data: Input DataFrame
        max_insights: Maximum number of insights to return
        
    Returns:
        List of key insight strings
    """
    if not openai_client and not anthropic_client:
        return ["AI insights unavailable - please configure API keys."]
    
    provider = "anthropic" if anthropic_client else "openai"
    insights = generate_enhanced_insights(data, provider)
    
    # Extract key highlights from insights
    highlights = []
    
    if "general_insights" in insights and insights["general_insights"]:
        highlights.extend(insights["general_insights"][:1])
    
    if "statistical_insights" in insights and insights["statistical_insights"]:
        highlights.extend(insights["statistical_insights"][:1])
    
    if "correlation_insights" in insights and insights["correlation_insights"]:
        highlights.extend(insights["correlation_insights"][:1])
        
    if "recommendations" in insights and insights["recommendations"]:
        highlights.extend(insights["recommendations"][:1])
    
    # If we still need more insights, look at other categories
    if len(highlights) < max_insights:
        if "data_quality_insights" in insights and insights["data_quality_insights"]:
            highlights.extend(insights["data_quality_insights"][:1])
    
    if len(highlights) < max_insights:
        if "trend_insights" in insights and insights["trend_insights"]:
            highlights.extend(insights["trend_insights"][:1])
    
    # Limit to requested number of insights
    return highlights[:max_insights]

def get_column_recommendations(data: pd.DataFrame, column_name: str) -> List[str]:
    """
    Get AI-powered recommendations for a specific column.
    
    Args:
        data: Input DataFrame
        column_name: Name of the column to analyze
        
    Returns:
        List of recommendations for this column
    """
    if not openai_client and not anthropic_client:
        return ["AI recommendations unavailable - please configure API keys."]
    
    provider = "anthropic" if anthropic_client else "openai"
    
    # Extract column-specific information
    column_type = str(data[column_name].dtype)
    
    # Prepare column-specific statistics
    if pd.api.types.is_numeric_dtype(data[column_name]):
        stats = {
            "min": data[column_name].min(),
            "max": data[column_name].max(),
            "mean": data[column_name].mean(),
            "median": data[column_name].median(),
            "std": data[column_name].std(),
            "missing": data[column_name].isna().sum()
        }
    elif pd.api.types.is_object_dtype(data[column_name]):
        stats = {
            "unique_values": data[column_name].nunique(),
            "most_common": data[column_name].value_counts().head(3).to_dict(),
            "missing": data[column_name].isna().sum()
        }
    else:
        # Datetime or other type
        stats = {
            "unique_values": data[column_name].nunique(),
            "missing": data[column_name].isna().sum()
        }
    
    # Generate column-specific prompt
    prompt = f"""
    Analyze this column from the dataset and provide specific recommendations:
    
    Column Name: {column_name}
    Data Type: {column_type}
    Statistics: {json.dumps(stats)}
    
    Provide 3-5 specific recommendations for further analysis or data cleaning for this column.
    Focus on actionable advice based on the column's characteristics.
    """
    
    try:
        if provider == "anthropic":
            message = anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=500,
                temperature=0.2,
                messages=[{"role": "user", "content": prompt}]
            )
            recommendations = message.content[0].text.split("\n")
        else:
            response = openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=500
            )
            recommendations = response.choices[0].message.content.split("\n")
        
        # Clean up the recommendations
        clean_recommendations = []
        for rec in recommendations:
            rec = rec.strip()
            if rec and not rec.startswith("#") and len(rec) > 10:
                # Remove numbering if present (e.g., "1.", "1)", etc.)
                rec = re.sub(r"^\d+[\.\)\-]\s*", "", rec)
                clean_recommendations.append(rec)
        
        return clean_recommendations
    except Exception as e:
        return [f"Error generating recommendations: {str(e)}"]