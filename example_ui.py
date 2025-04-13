import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from ui_components import DataVizUI, ModernForm, DataWidgets, ChartBuilder

# Set page configuration
st.set_page_config(
    page_title="UI Component Library Demo",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the custom CSS
DataVizUI.load_css()
ModernForm.load_css()

def generate_sample_data():
    """Generate sample data for demonstration"""
    np.random.seed(42)
    
    # Create a DataFrame with various data types
    df = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=100),
        'category': np.random.choice(['A', 'B', 'C', 'D'], 100),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 100),
        'value': np.random.normal(100, 20, 100),
        'count': np.random.randint(1, 100, 100),
        'growth': np.random.uniform(-0.2, 0.5, 100),
        'score': np.random.randint(0, 10, 100),
        'active': np.random.choice([True, False], 100),
    })
    
    # Add some correlations
    df['related_value'] = df['value'] * 0.8 + np.random.normal(0, 10, 100)
    
    # Add some text data
    df['description'] = [f"Item {i}" for i in range(100)]
    
    return df

def main():
    # Title with gradient
    st.markdown(DataVizUI.gradient_text("Modern UI Component Library"), unsafe_allow_html=True)
    
    st.markdown("""
    This is a demo of a custom UI component library for Streamlit applications.
    The library provides modern, visually appealing components for data visualization and analytics dashboards.
    """)
    
    # Feature overview
    st.markdown("### Features")
    
    col1, col2, col3 = DataVizUI.dashboard_row(3)
    
    with col1:
        DataVizUI.feature_card(
            "Modern UI Components", 
            "A comprehensive set of visually appealing UI components designed for data applications.",
            "🎨"
        )
    
    with col2:
        DataVizUI.feature_card(
            "Interactive Data Widgets", 
            "Specialized widgets for data filtering, selection, and visualization.",
            "📊"
        )
    
    with col3:
        DataVizUI.feature_card(
            "Responsive Design", 
            "Components adapt to different screen sizes and viewport dimensions.",
            "📱"
        )
    
    # Generate sample data
    data = generate_sample_data()
    
    # Component Showcase Tabs
    selected_tab = DataVizUI.tabs(
        ["Cards & Metrics", "Forms & Inputs", "Data Tables", "Chart Builder", "Data Widgets"],
        key="main_tabs"
    )
    
    # Tab 1: Cards & Metrics
    if selected_tab == 0:
        st.markdown("### Cards & Metrics Components")
        
        # KPI Cards Row
        row1 = DataVizUI.dashboard_row(4)
        
        with row1[0]:
            DataVizUI.kpi_card(
                value=f"${data['value'].sum():,.0f}",
                label="Total Revenue",
                delta=12.5,
                target=15000,
                icon="💰"
            )
        
        with row1[1]:
            DataVizUI.kpi_card(
                value=len(data),
                label="Total Orders",
                delta=-3.2,
                icon="📦"
            )
        
        with row1[2]:
            DataVizUI.kpi_card(
                value=f"{data['growth'].mean()*100:.1f}%",
                label="Average Growth",
                delta=5.4,
                target=30,
                icon="📈"
            )
        
        with row1[3]:
            DataVizUI.kpi_card(
                value=data['score'].mean().round(1),
                label="Average Score",
                delta=0.2,
                target=8.5,
                icon="⭐"
            )
        
        # Regular Cards
        st.markdown("### Information Cards")
        row2 = DataVizUI.dashboard_row(3)
        
        with row2[0]:
            DataVizUI.card(
                title="Basic Card",
                content="This is a basic card component with a title and content."
            )
        
        with row2[1]:
            DataVizUI.info_card(
                title="Info Card",
                description="This card includes an icon and is designed to display informational content.",
                icon="ℹ️"
            )
        
        with row2[2]:
            # Card with custom children
            with st.container():
                DataVizUI.card(
                    title="Card with Chart",
                    content="This card contains a Plotly chart:"
                )
                
                # Create a simple chart
                chart = px.bar(
                    data.groupby('region')['value'].mean().reset_index(),
                    x='region',
                    y='value',
                    title="Average Value by Region"
                )
                st.plotly_chart(chart, use_container_width=True)
        
        # Alert Components
        st.markdown("### Alert Components")
        row3 = DataVizUI.dashboard_row(2)
        
        with row3[0]:
            DataVizUI.alert(
                "This is a primary alert component. It can be used to display important information.",
                variant="primary"
            )
            DataVizUI.alert(
                "This is a success alert. Use it to indicate successful operations.",
                variant="success"
            )
        
        with row3[1]:
            DataVizUI.alert(
                "This is a warning alert. It draws attention to important warnings.",
                variant="warning"
            )
            DataVizUI.alert(
                "This is an info alert. It provides general information to the user.",
                variant="info"
            )
        
        # Badges and Metrics
        st.markdown("### Badges and Metrics")
        
        badge_html = f"""
        <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px;">
            {DataVizUI.badge("Primary", "primary")}
            {DataVizUI.badge("Secondary", "secondary")}
            {DataVizUI.badge("Success", "success")}
            {DataVizUI.badge("Warning", "warning")}
            {DataVizUI.badge("Info", "info")}
        </div>
        """
        st.markdown(badge_html, unsafe_allow_html=True)
        
        row4 = DataVizUI.dashboard_row(4)
        
        with row4[0]:
            DataVizUI.metric_comparison("Conversion Rate", 3.45, 0.28)
        
        with row4[1]:
            DataVizUI.metric_comparison("Average Order", 85.20, -2.35)
        
        with row4[2]:
            DataVizUI.metric_comparison("Customer Count", 1250, 12.5)
        
        with row4[3]:
            DataVizUI.metric_comparison("Bounce Rate", 28.6, -1.8)
        
        # Progress bars
        st.markdown("### Progress Components")
        
        DataVizUI.progress(75)
        DataVizUI.progress(45)
        DataVizUI.progress(90)
    
    # Tab 2: Forms & Inputs
    elif selected_tab == 1:
        st.markdown("### Forms & Input Components")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            with ModernForm.form("Sample Form", "sample_form"):
                ModernForm.label("Personal Information")
                name = st.text_input("Name")
                email = st.text_input("Email")
                
                ModernForm.label("Settings", "Configure your preferences")
                option = st.selectbox("Preferred Option", ["Option 1", "Option 2", "Option 3"])
                
                col1, col2 = st.columns(2)
                with col1:
                    value = st.number_input("Value", min_value=0, max_value=100, value=50)
                with col2:
                    date = st.date_input("Date")
                
                ModernForm.label("Additional Options")
                notifications = st.checkbox("Enable notifications")
                
                submitted = st.form_submit_button("Submit")
            
            if submitted:
                st.success("Form submitted successfully!")
                st.json({
                    "name": name,
                    "email": email,
                    "option": option,
                    "value": value,
                    "date": str(date),
                    "notifications": notifications
                })
        
        with col2:
            DataVizUI.card(
                title="Custom Input Components",
                content="These components provide a modern look and feel for your forms."
            )
            
            st.markdown("### Toggle Switch")
            
            toggle_html = """
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                <label class="dvz-toggle">
                    <input type="checkbox" checked>
                    <span class="dvz-toggle-slider"></span>
                </label>
                <span style="margin-left: 10px;">Enable dark mode</span>
            </div>
            """
            st.markdown(toggle_html, unsafe_allow_html=True)
            
            st.markdown("### Buttons")
            
            buttons_html = f"""
            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px;">
                {DataVizUI.button("Primary Button", "primary")}
                {DataVizUI.button("Secondary Button", "secondary")}
                {DataVizUI.button("Success Button", "success")}
                {DataVizUI.button("Outline Button", "outline")}
            </div>
            """
            st.markdown(buttons_html, unsafe_allow_html=True)
    
    # Tab 3: Data Tables
    elif selected_tab == 2:
        st.markdown("### Data Table Components")
        
        # Sample DataFrames
        sample_data = data.head(10)
        
        # Show sample data with styled table
        DataVizUI.card(title="Styled Data Table")
        DataVizUI.data_table(sample_data)
        
        # Regular Streamlit table vs styled table
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### Standard Streamlit Table")
            st.dataframe(sample_data)
        
        with col2:
            st.markdown("### Styled Data Table")
            DataVizUI.data_table(sample_data)
        
        # Show download link
        st.markdown("### Data Export")
        download_link = dataframe_to_csv_download(sample_data, "sample_data.csv")
        st.markdown(download_link, unsafe_allow_html=True)
        
        # Insight tags
        st.markdown("### Data Insights")
        
        DataVizUI.insight_tag(f"Average value: {data['value'].mean():.2f}")
        DataVizUI.insight_tag(f"Most common category: {data['category'].value_counts().idxmax()}")
        DataVizUI.insight_tag(f"Date range: {data['date'].min().date()} to {data['date'].max().date()}")
    
    # Tab 4: Chart Builder
    elif selected_tab == 3:
        st.markdown("### Interactive Chart Builder")
        
        # Create a chart builder instance
        chart_builder = ChartBuilder(data)
        
        # Build a chart
        fig = chart_builder.build()
        
        if fig:
            # Display the chart
            st.plotly_chart(fig, use_container_width=True)
    
    # Tab 5: Data Widgets
    elif selected_tab == 4:
        st.markdown("### Data Widgets")
        
        # Date range selector
        st.markdown("#### Date Range Selector")
        start_date, end_date = DataWidgets.date_range_selector(data, 'date', key="demo_dates")
        
        if start_date and end_date:
            filtered_data = data[(data['date'].dt.date >= start_date) & (data['date'].dt.date <= end_date)]
            st.write(f"Selected date range: {start_date} to {end_date}")
            st.write(f"Data points in range: {len(filtered_data)}")
        
        # Column selector
        st.markdown("#### Column Selector")
        selected_columns = DataWidgets.column_selector(
            data, 
            numeric_only=False,
            label="Select columns to display",
            key="demo_cols"
        )
        
        if selected_columns:
            st.dataframe(data[selected_columns].head())
        
        # Outlier filter
        st.markdown("#### Outlier Filter")
        filtered_data = DataWidgets.outlier_filter(data, 'value', key="demo_outlier")
        
        if len(filtered_data) < len(data):
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("##### Original Distribution")
                fig1 = px.histogram(data, x='value', title="Original Value Distribution")
                st.plotly_chart(fig1, use_container_width=True)
            
            with col2:
                st.markdown("##### Filtered Distribution")
                fig2 = px.histogram(filtered_data, x='value', title="Filtered Value Distribution")
                st.plotly_chart(fig2, use_container_width=True)
        
        # Categorical filter
        st.markdown("#### Categorical Filter")
        cat_filtered_data = DataWidgets.categorical_filter(data, 'region', key="demo_cat")
        
        if len(cat_filtered_data) < len(data):
            st.write(f"Filtered data contains {len(cat_filtered_data)} rows")
            st.dataframe(cat_filtered_data.head())

if __name__ == "__main__":
    main()

# Helper function from the UI components library
def dataframe_to_csv_download(data, filename="data.csv"):
    """Helper function to create a download link for a DataFrame"""
    import base64
    
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" class="dvz-button dvz-button-primary">Download CSV</a>'
    return href