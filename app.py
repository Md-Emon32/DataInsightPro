import streamlit as st
import pandas as pd
import numpy as np
import os
import io
import plotly.express as px

from data_processor import process_data, filter_data, get_basic_stats
from insights_generator import generate_automated_insights, extract_key_metrics
from visualization import create_trend_chart, create_correlation_heatmap, create_distribution_plot
from chatbot import process_query
from utils import get_file_extension, show_error, show_success

# Import AI-powered insights mechanism
from ai_insights import (
    generate_enhanced_insights, 
    format_insights_for_display, 
    generate_insight_highlights,
    get_column_recommendations
)

# Set page configuration
st.set_page_config(
    page_title="Data Insights Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
if 'data' not in st.session_state:
    st.session_state.data = None
if 'file_name' not in st.session_state:
    st.session_state.file_name = None
if 'insights' not in st.session_state:
    st.session_state.insights = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


def main():
    # Sidebar for data upload and options
    with st.sidebar:
        st.title("📊 Data Insights Explorer")
        st.markdown("---")
        
        # Data upload section
        st.header("Upload Your Data")
        uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx', 'xls'])
        
        if uploaded_file is not None:
            try:
                file_extension = get_file_extension(uploaded_file.name)
                
                if file_extension == 'csv':
                    data = pd.read_csv(uploaded_file)
                elif file_extension in ['xlsx', 'xls']:
                    data = pd.read_excel(uploaded_file)
                else:
                    show_error("Unsupported file format. Please upload a CSV or Excel file.")
                    return
                
                # Store data in session state
                st.session_state.data = data
                st.session_state.file_name = uploaded_file.name
                
                # Reset insights when new data is uploaded
                st.session_state.insights = None
                st.session_state.chat_history = []
                
                show_success(f"Successfully loaded {uploaded_file.name} with {len(data)} rows and {len(data.columns)} columns")
            except Exception as e:
                show_error(f"Error loading file: {str(e)}")
        
        # Data filtering options (only show when data is loaded)
        if st.session_state.data is not None:
            st.markdown("---")
            st.header("Data Filtering")
            
            # Select columns to use
            all_columns = st.session_state.data.columns.tolist()
            selected_columns = st.multiselect(
                "Select columns to analyze",
                options=all_columns,
                default=all_columns[:5] if len(all_columns) > 5 else all_columns
            )
            
            # Filter for numerical analysis
            numeric_columns = st.session_state.data.select_dtypes(include=['number']).columns.tolist()
            analysis_columns = st.multiselect(
                "Select numerical columns for analytics",
                options=numeric_columns,
                default=numeric_columns[:3] if len(numeric_columns) > 3 else numeric_columns
            )
            
            # Apply filters button
            if st.button("Apply Filters"):
                if selected_columns:
                    st.session_state.data = filter_data(st.session_state.data, selected_columns)
                    show_success("Filters applied successfully")
                else:
                    show_error("Please select at least one column")
    
    # Main content area
    if st.session_state.data is not None:
        data = st.session_state.data
        
        # Quick stats row
        st.header(f"📊 Data Overview: {st.session_state.file_name}")
        
        # Data summary metrics in columns
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Rows", f"{data.shape[0]:,}")
        with col2:
            st.metric("Columns", data.shape[1])
        with col3:
            st.metric("Numeric Columns", len(data.select_dtypes(include=['number']).columns))
        with col4:
            missing_percentage = round((data.isna().sum().sum() / (data.shape[0] * data.shape[1])) * 100, 2)
            st.metric("Missing Values", f"{missing_percentage}%")
        
        # Data exploration tab area
        tab1, tab2, tab3, tab4 = st.tabs(["Data Explorer", "Automated Insights", "Visualizations", "Chat with Data"])
        
        # Tab 1: Data Explorer
        with tab1:
            st.subheader("Data Preview")
            st.dataframe(data.head(100), use_container_width=True)
            
            st.subheader("Data Summary")
            
            # Display different statistics based on column types
            numeric_summary = data.describe().T
            if not numeric_summary.empty:
                st.write("Numerical Columns Summary")
                st.dataframe(numeric_summary, use_container_width=True)
            
            categorical_cols = data.select_dtypes(include=['object']).columns
            if len(categorical_cols) > 0:
                st.write("Categorical Columns Summary")
                cat_summary = pd.DataFrame({
                    'Column': categorical_cols,
                    'Unique Values': [data[col].nunique() for col in categorical_cols],
                    'Most Common': [data[col].value_counts().index[0] if not data[col].value_counts().empty else None for col in categorical_cols],
                    'Most Common Count': [data[col].value_counts().iloc[0] if not data[col].value_counts().empty else 0 for col in categorical_cols],
                })
                st.dataframe(cat_summary, use_container_width=True)
            
            # Basic data statistics
            st.subheader("Additional Information")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("Data Types")
                st.dataframe(pd.DataFrame({'Data Type': data.dtypes}), use_container_width=True)
            
            with col2:
                st.write("Missing Values")
                missing_data = pd.DataFrame({
                    'Missing Values': data.isna().sum(),
                    'Percentage': round(data.isna().sum() / len(data) * 100, 2)
                })
                st.dataframe(missing_data, use_container_width=True)
        
        # Tab 2: Automated Insights
        with tab2:
            st.subheader("Automated Data Insights")
            
            # Add tabs for different insight types
            insight_tabs = st.tabs(["Basic Insights", "AI-Powered Insights"])
            
            with insight_tabs[0]:
                # Generate basic insights button
                if st.button("Generate Basic Insights") or st.session_state.insights is not None:
                    with st.spinner("Generating basic insights..."):
                        if st.session_state.insights is None:
                            # Store insights in session state to avoid regenerating on rerun
                            st.session_state.insights = generate_automated_insights(data)
                        
                        insights = st.session_state.insights
                        
                        # Display general insights
                        st.markdown("### Key Insights")
                        for insight in insights['general_insights']:
                            st.markdown(f"- {insight}")
                        
                        # Display column-specific insights
                        st.markdown("### Column-Specific Insights")
                        for col, col_insights in insights['column_insights'].items():
                            with st.expander(f"{col}"):
                                for insight in col_insights:
                                    st.markdown(f"- {insight}")
                        
                        # Display correlation insights if available
                        if 'correlation_insights' in insights and insights['correlation_insights']:
                            st.markdown("### Correlation Insights")
                            for insight in insights['correlation_insights']:
                                st.markdown(f"- {insight}")
            
            with insight_tabs[1]:
                # Add AI provider selection
                ai_provider = st.radio("Select AI Provider:", ["OpenAI", "Anthropic"], horizontal=True)
                
                # Check if API keys are configured
                if (ai_provider == "OpenAI" and not os.environ.get("OPENAI_API_KEY")) or \
                   (ai_provider == "Anthropic" and not os.environ.get("ANTHROPIC_API_KEY")):
                    st.warning(f"{ai_provider} API key not configured. Please set up the appropriate API key in the environment variables.")
                else:
                    # Store AI insights in session state
                    if 'ai_insights' not in st.session_state:
                        st.session_state.ai_insights = None
                    
                    # Generate AI-powered insights button
                    if st.button("Generate AI-Powered Insights") or st.session_state.ai_insights is not None:
                        with st.spinner("Generating AI-powered insights... This may take a moment."):
                            provider = ai_provider.lower()
                            
                            if st.session_state.ai_insights is None:
                                # Generate new insights
                                raw_insights = generate_enhanced_insights(data, provider)
                                st.session_state.ai_insights = format_insights_for_display(raw_insights)
                            
                            ai_insights = st.session_state.ai_insights
                            
                            # Check for errors
                            if "error" in ai_insights:
                                st.error(ai_insights["error"])
                            else:
                                # Display insights in a nicely formatted way
                                if "general_insights" in ai_insights:
                                    st.markdown("### 📌 General Insights")
                                    for insight in ai_insights["general_insights"]:
                                        st.markdown(f"- {insight}")
                                    st.markdown("---")
                                
                                if "data_quality_insights" in ai_insights:
                                    with st.expander("✅ Data Quality Insights", expanded=True):
                                        for insight in ai_insights["data_quality_insights"]:
                                            st.markdown(f"- {insight}")
                                
                                if "statistical_insights" in ai_insights:
                                    with st.expander("📊 Statistical Insights", expanded=True):
                                        for insight in ai_insights["statistical_insights"]:
                                            st.markdown(f"- {insight}")
                                
                                if "trend_insights" in ai_insights:
                                    with st.expander("📈 Trend Insights", expanded=True):
                                        for insight in ai_insights["trend_insights"]:
                                            st.markdown(f"- {insight}")
                                
                                if "correlation_insights" in ai_insights:
                                    with st.expander("🔄 Correlation Insights", expanded=True):
                                        for insight in ai_insights["correlation_insights"]:
                                            st.markdown(f"- {insight}")
                                
                                if "recommendations" in ai_insights:
                                    st.markdown("### 🔍 Recommendations")
                                    for recommendation in ai_insights["recommendations"]:
                                        st.markdown(f"- {recommendation}")
                                
                                # Visualization suggestions
                                if "visualizations" in ai_insights and ai_insights["visualizations"]:
                                    st.markdown("### 📊 Suggested Visualizations")
                                    for i, viz in enumerate(ai_insights["visualizations"]):
                                        with st.expander(f"{viz['title']}", expanded=i==0):
                                            st.markdown(f"**Description**: {viz['description']}")
                                            st.markdown(f"**Type**: {viz['type']}")
                                            if viz['columns']:
                                                st.markdown(f"**Columns**: {', '.join(viz['columns'])}")
                    
                    # Add a section for column-specific recommendations
                    st.markdown("### 🔍 Column-Specific Recommendations")
                    col_for_analysis = st.selectbox("Select a column for detailed AI analysis:", data.columns.tolist())
                    
                    if st.button("Analyze Column"):
                        with st.spinner(f"Analyzing column '{col_for_analysis}'..."):
                            recommendations = get_column_recommendations(data, col_for_analysis)
                            
                            for rec in recommendations:
                                st.markdown(f"- {rec}")
        
        # Tab 3: Visualizations
        with tab3:
            st.subheader("Data Visualizations")
            
            # Select visualization type
            vis_type = st.selectbox(
                "Select Visualization Type",
                options=[
                    "Distribution Plot", 
                    "Trend Analysis", 
                    "Correlation Heatmap", 
                    "Scatter Plot",
                    "Bar Chart",
                    "Box Plot"
                ]
            )
            
            # Get numerical and categorical columns
            numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
            categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
            
            if vis_type == "Distribution Plot":
                if numeric_cols:
                    selected_col = st.selectbox("Select column", options=numeric_cols)
                    fig = create_distribution_plot(data, selected_col)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("No numerical columns available for distribution plot")
            
            elif vis_type == "Trend Analysis":
                if len(numeric_cols) > 0 and len(categorical_cols) > 0:
                    x_col = st.selectbox("Select X-axis (categorical/date)", options=categorical_cols)
                    y_col = st.selectbox("Select Y-axis (numerical)", options=numeric_cols)
                    fig = create_trend_chart(data, x_col, y_col)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Need at least one numeric and one categorical/date column for trend analysis")
            
            elif vis_type == "Correlation Heatmap":
                if len(numeric_cols) > 1:
                    fig = create_correlation_heatmap(data, numeric_cols)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Need at least two numerical columns for correlation heatmap")
            
            elif vis_type == "Scatter Plot":
                if len(numeric_cols) >= 2:
                    col1, col2 = st.columns(2)
                    with col1:
                        x_col = st.selectbox("Select X-axis", options=numeric_cols)
                    with col2:
                        y_col = st.selectbox("Select Y-axis", options=[col for col in numeric_cols if col != x_col] if len(numeric_cols) > 1 else numeric_cols)
                    
                    color_col = None
                    if categorical_cols:
                        color_col = st.selectbox("Color by (optional)", options=["None"] + categorical_cols)
                        if color_col == "None":
                            color_col = None
                    
                    fig = px.scatter(data, x=x_col, y=y_col, color=color_col, title=f"{y_col} vs {x_col}")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Need at least two numerical columns for scatter plot")
            
            elif vis_type == "Bar Chart":
                if categorical_cols:
                    x_col = st.selectbox("Select Category (X-axis)", options=categorical_cols)
                    
                    if numeric_cols:
                        y_col = st.selectbox("Select Value (Y-axis)", options=numeric_cols)
                        color_col = None
                        if len(categorical_cols) > 1:
                            color_options = [col for col in categorical_cols if col != x_col]
                            color_col = st.selectbox("Color by (optional)", options=["None"] + color_options)
                            if color_col == "None":
                                color_col = None
                        
                        fig = px.bar(data, x=x_col, y=y_col, color=color_col, title=f"{y_col} by {x_col}")
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        # Simple count-based bar chart if no numeric columns
                        fig = px.histogram(data, x=x_col, title=f"Count by {x_col}")
                        st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Need at least one categorical column for bar chart")
            
            elif vis_type == "Box Plot":
                if numeric_cols and categorical_cols:
                    y_col = st.selectbox("Select Value (Y-axis)", options=numeric_cols)
                    x_col = st.selectbox("Select Category (X-axis)", options=categorical_cols)
                    
                    fig = px.box(data, x=x_col, y=y_col, title=f"Distribution of {y_col} by {x_col}")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Need at least one numerical and one categorical column for box plot")
        
        # Tab 4: Chat with Data
        with tab4:
            st.subheader("Chat with Your Data")
            st.write("Ask questions about your data in plain English!")
            
            # Display chat history
            for message in st.session_state.chat_history:
                if message["role"] == "user":
                    st.markdown(f"**You:** {message['content']}")
                else:
                    st.markdown(f"**Assistant:** {message['content']}")
                    if "chart" in message:
                        st.plotly_chart(message["chart"], use_container_width=True)
            
            # Chat input
            user_query = st.text_input("Ask a question about your data:", key="user_query")
            
            if st.button("Ask") and user_query:
                # Add user message to chat history
                st.session_state.chat_history.append({"role": "user", "content": user_query})
                
                # Process the query and get response
                with st.spinner("Processing your question..."):
                    response, chart = process_query(user_query, data)
                
                # Add response to chat history
                response_msg = {"role": "assistant", "content": response}
                if chart is not None:
                    response_msg["chart"] = chart
                
                st.session_state.chat_history.append(response_msg)
                
                # Clear the input box by triggering a rerun
                st.session_state.user_query = ""
                st.rerun()
    
    else:
        # Display welcome message when no data is loaded
        st.title("Welcome to Data Insights Explorer 📊")
        
        st.markdown("""
        ### Get started by uploading your data file
        
        This tool helps you:
        - Explore and visualize your data easily
        - Discover insights automatically
        - Create visualizations to understand trends
        - Ask questions about your data in plain English
        
        Upload a CSV or Excel file from the sidebar to begin.
        """)
        
        # Example layout with empty placeholders
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("#### 📝 Data Exploration")
            st.markdown("View and understand your data structure")
        with col2:
            st.markdown("#### 🔍 Automated Insights")
            st.markdown("Discover patterns and anomalies")
        with col3:
            st.markdown("#### 💬 Chat with Data")
            st.markdown("Ask questions in plain English")


if __name__ == "__main__":
    main()
