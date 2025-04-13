import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Any, Union, Optional
import base64
from PIL import Image
import io

class DataVizUI:
    """A modern UI component library for data visualization and dashboard creation in Streamlit."""
    
    # Color schemes
    COLORS = {
        'primary': '#4361EE',
        'secondary': '#3A0CA3',
        'success': '#4CC9F0',
        'warning': '#F72585',
        'info': '#4895EF',
        'light': '#F8F9FA',
        'dark': '#212529',
        'accent1': '#7209B7',
        'accent2': '#560BAD',
        'accent3': '#480CA8',
        'gradient1': 'linear-gradient(90deg, #4361EE 0%, #3A0CA3 100%)',
        'gradient2': 'linear-gradient(90deg, #F72585 0%, #7209B7 100%)',
    }
    
    # Font settings
    FONTS = {
        'title': '"Poppins", sans-serif',
        'body': '"Inter", sans-serif',
        'code': '"JetBrains Mono", monospace',
    }
    
    @staticmethod
    def load_css():
        """Load the custom CSS for the component library."""
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Poppins:wght@400;500;600;700&display=swap');
        
        /* Root variables */
        :root {
            --color-primary: #4361EE;
            --color-secondary: #3A0CA3;
            --color-success: #4CC9F0;
            --color-warning: #F72585;
            --color-info: #4895EF;
            --color-light: #F8F9FA;
            --color-dark: #212529;
            --color-accent1: #7209B7;
            --color-accent2: #560BAD;
            --color-accent3: #480CA8;
            
            --font-title: "Poppins", sans-serif;
            --font-body: "Inter", sans-serif;
            --font-code: "JetBrains Mono", monospace;
            
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
            --shadow-md: 0 4px 6px rgba(0,0,0,0.1), 0 1px 3px rgba(0,0,0,0.08);
            --shadow-lg: 0 10px 20px rgba(0,0,0,0.1), 0 3px 6px rgba(0,0,0,0.05);
            
            --radius-sm: 4px;
            --radius-md: 8px;
            --radius-lg: 16px;
            --radius-xl: 24px;
        }
        
        /* Base elements styling */
        .stApp {
            font-family: var(--font-body);
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: var(--font-title);
            font-weight: 600;
        }
        
        code {
            font-family: var(--font-code);
        }
        
        /* Card component */
        .dvz-card {
            background: white;
            border-radius: var(--radius-md);
            padding: 1.5rem;
            box-shadow: var(--shadow-md);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            margin-bottom: 1rem;
        }
        
        .dvz-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-lg);
        }
        
        .dvz-card-title {
            font-family: var(--font-title);
            font-weight: 600;
            font-size: 1.25rem;
            margin-bottom: 0.75rem;
            color: var(--color-dark);
        }
        
        /* Badge component */
        .dvz-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 50px;
            font-size: 0.75rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .dvz-badge-primary {
            background: var(--color-primary);
            color: white;
        }
        
        .dvz-badge-secondary {
            background: var(--color-secondary);
            color: white;
        }
        
        .dvz-badge-success {
            background: var(--color-success);
            color: white;
        }
        
        .dvz-badge-warning {
            background: var(--color-warning);
            color: white;
        }
        
        .dvz-badge-info {
            background: var(--color-info);
            color: white;
        }
        
        /* Alert component */
        .dvz-alert {
            padding: 1rem;
            border-radius: var(--radius-md);
            margin-bottom: 1rem;
            border-left: 4px solid;
        }
        
        .dvz-alert-primary {
            background: rgba(67, 97, 238, 0.1);
            border-left-color: var(--color-primary);
        }
        
        .dvz-alert-secondary {
            background: rgba(58, 12, 163, 0.1);
            border-left-color: var(--color-secondary);
        }
        
        .dvz-alert-success {
            background: rgba(76, 201, 240, 0.1);
            border-left-color: var(--color-success);
        }
        
        .dvz-alert-warning {
            background: rgba(247, 37, 133, 0.1);
            border-left-color: var(--color-warning);
        }
        
        .dvz-alert-info {
            background: rgba(72, 149, 239, 0.1);
            border-left-color: var(--color-info);
        }
        
        /* Button styling */
        .dvz-button {
            display: inline-block;
            padding: 0.5rem 1.25rem;
            border-radius: var(--radius-md);
            font-weight: 500;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
            border: none;
            box-shadow: var(--shadow-sm);
        }
        
        .dvz-button-primary {
            background: var(--color-primary);
            color: white;
        }
        
        .dvz-button-primary:hover {
            background: #3051d3;
            box-shadow: var(--shadow-md);
        }
        
        .dvz-button-secondary {
            background: var(--color-secondary);
            color: white;
        }
        
        .dvz-button-secondary:hover {
            background: #2e0a82;
            box-shadow: var(--shadow-md);
        }
        
        .dvz-button-success {
            background: var(--color-success);
            color: white;
        }
        
        .dvz-button-success:hover {
            background: #39b4d9;
            box-shadow: var(--shadow-md);
        }
        
        .dvz-button-outline {
            background: transparent;
            border: 1px solid var(--color-primary);
            color: var(--color-primary);
        }
        
        .dvz-button-outline:hover {
            background: rgba(67, 97, 238, 0.1);
        }
        
        /* Progress bar */
        .dvz-progress {
            height: 8px;
            background: #e9ecef;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 1rem;
        }
        
        .dvz-progress-bar {
            height: 100%;
            border-radius: 4px;
            background: var(--color-primary);
        }
        
        /* Gradient text */
        .dvz-gradient-text {
            background: linear-gradient(90deg, var(--color-primary) 0%, var(--color-accent1) 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline-block;
        }
        
        /* Stats card */
        .dvz-stat-card {
            background: white;
            border-radius: var(--radius-md);
            padding: 1.25rem;
            box-shadow: var(--shadow-md);
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .dvz-stat-value {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            font-family: var(--font-title);
        }
        
        .dvz-stat-label {
            font-size: 0.875rem;
            color: #6c757d;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Data table styling */
        .dvz-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin-bottom: 1rem;
        }
        
        .dvz-table th {
            background: #f8f9fa;
            padding: 0.75rem 1rem;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid #dee2e6;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        
        .dvz-table td {
            padding: 0.75rem 1rem;
            border-bottom: 1px solid #dee2e6;
            vertical-align: middle;
        }
        
        .dvz-table tr:last-child td {
            border-bottom: none;
        }
        
        .dvz-table tr:hover {
            background-color: rgba(67, 97, 238, 0.05);
        }
        
        /* Chart container */
        .dvz-chart-container {
            background: white;
            border-radius: var(--radius-md);
            padding: 1rem;
            box-shadow: var(--shadow-md);
            margin-bottom: 1rem;
        }
        
        .dvz-chart-title {
            font-family: var(--font-title);
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 0.5rem;
            color: var(--color-dark);
        }
        
        /* Insight tag */
        .dvz-insight-tag {
            display: flex;
            align-items: center;
            padding: 0.5rem 1rem;
            background: rgba(67, 97, 238, 0.1);
            border-radius: var(--radius-md);
            margin-bottom: 0.5rem;
        }
        
        .dvz-insight-tag i {
            margin-right: 0.5rem;
            color: var(--color-primary);
        }
        
        /* Animated container */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .dvz-animated {
            animation: fadeIn 0.3s ease-out forwards;
        }
        
        /* Dashboard layout helpers */
        .dvz-dashboard-row {
            display: flex;
            flex-wrap: wrap;
            margin: 0 -0.5rem;
        }
        
        .dvz-dashboard-col {
            flex: 1;
            padding: 0 0.5rem;
            min-width: 250px;
        }
        
        /* Tabs styling */
        .dvz-tabs {
            display: flex;
            border-bottom: 1px solid #dee2e6;
            margin-bottom: 1rem;
        }
        
        .dvz-tab {
            padding: 0.5rem 1rem;
            cursor: pointer;
            border-bottom: 2px solid transparent;
            font-weight: 500;
        }
        
        .dvz-tab-active {
            border-bottom: 2px solid var(--color-primary);
            color: var(--color-primary);
        }
        
        /* Modern toggle switch */
        .dvz-toggle {
            display: inline-block;
            position: relative;
            width: 50px;
            height: 24px;
        }
        
        .dvz-toggle input {
            opacity: 0;
            width: 0;
            height: 0;
        }
        
        .dvz-toggle-slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            transition: 0.4s;
            border-radius: 34px;
        }
        
        .dvz-toggle-slider:before {
            position: absolute;
            content: "";
            height: 16px;
            width: 16px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            transition: 0.4s;
            border-radius: 50%;
        }
        
        input:checked + .dvz-toggle-slider {
            background-color: var(--color-primary);
        }
        
        input:checked + .dvz-toggle-slider:before {
            transform: translateX(26px);
        }
        </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def card(title: str, content: str = None, children: Any = None, key: Optional[str] = None):
        """
        Display a card component with a title and content.
        
        Args:
            title: The card title
            content: Text content (optional)
            children: Custom Streamlit elements to include in the card (optional)
            key: Optional unique key for the component
        """
        st.markdown(f"""
        <div class="dvz-card" key="{key or ''}">
            <div class="dvz-card-title">{title}</div>
            {content or ''}
        </div>
        """, unsafe_allow_html=True)
        
        if children:
            with st.container():
                children

    @staticmethod
    def badge(text: str, variant: str = "primary"):
        """
        Display a badge component.
        
        Args:
            text: The badge text
            variant: Badge variant (primary, secondary, success, warning, info)
        """
        return f'<span class="dvz-badge dvz-badge-{variant}">{text}</span>'

    @staticmethod
    def alert(content: str, variant: str = "info"):
        """
        Display an alert component.
        
        Args:
            content: The alert content
            variant: Alert variant (primary, secondary, success, warning, info)
        """
        st.markdown(f"""
        <div class="dvz-alert dvz-alert-{variant}">
            {content}
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def button(text: str, variant: str = "primary", key: Optional[str] = None):
        """
        Display a button component.
        
        Args:
            text: The button text
            variant: Button variant (primary, secondary, success, outline)
            key: Optional unique key for the component
        """
        return f'<button class="dvz-button dvz-button-{variant}" key="{key or ""}">{text}</button>'

    @staticmethod
    def progress(value: float, key: Optional[str] = None):
        """
        Display a progress bar.
        
        Args:
            value: The progress value (0-100)
            key: Optional unique key for the component
        """
        clamped_value = max(0, min(100, value))
        st.markdown(f"""
        <div class="dvz-progress" key="{key or ''}">
            <div class="dvz-progress-bar" style="width: {clamped_value}%"></div>
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def gradient_text(text: str):
        """
        Display gradient text.
        
        Args:
            text: The text to display with gradient
        """
        return f'<h2 class="dvz-gradient-text">{text}</h2>'

    @staticmethod
    def stat_card(value: Union[str, int, float], label: str, key: Optional[str] = None):
        """
        Display a statistics card.
        
        Args:
            value: The statistic value to display
            label: Label describing the statistic
            key: Optional unique key for the component
        """
        st.markdown(f"""
        <div class="dvz-stat-card" key="{key or ''}">
            <div class="dvz-stat-value">{value}</div>
            <div class="dvz-stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def data_table(data: pd.DataFrame, key: Optional[str] = None):
        """
        Display a styled data table.
        
        Args:
            data: Pandas DataFrame to display
            key: Optional unique key for the component
        """
        html_table = f'<div class="dvz-table-container" key="{key or ""}">'
        html_table += '<table class="dvz-table">'
        
        # Add header
        html_table += '<thead><tr>'
        for col in data.columns:
            html_table += f'<th>{col}</th>'
        html_table += '</tr></thead>'
        
        # Add body
        html_table += '<tbody>'
        for _, row in data.head(10).iterrows():
            html_table += '<tr>'
            for col in data.columns:
                cell_value = row[col]
                if pd.isna(cell_value):
                    html_table += '<td><em>N/A</em></td>'
                elif isinstance(cell_value, (int, float)):
                    if abs(cell_value) < 0.01 and cell_value != 0:
                        html_table += f'<td>{cell_value:.2e}</td>'
                    else:
                        html_table += f'<td>{cell_value:,}</td>'
                else:
                    html_table += f'<td>{str(cell_value)}</td>'
            html_table += '</tr>'
        html_table += '</tbody></table></div>'
        
        st.markdown(html_table, unsafe_allow_html=True)
        
        if len(data) > 10:
            st.caption(f"Showing 10 of {len(data)} rows")

    @staticmethod
    def chart_container(chart: Any, title: str = None):
        """
        Display a chart inside a styled container.
        
        Args:
            chart: Plotly figure object
            title: Optional chart title
        """
        with st.container():
            if title:
                st.markdown(f'<div class="dvz-chart-title">{title}</div>', unsafe_allow_html=True)
            st.plotly_chart(chart, use_container_width=True)

    @staticmethod
    def insight_tag(text: str, key: Optional[str] = None):
        """
        Display an insight tag.
        
        Args:
            text: The insight text
            key: Optional unique key for the component
        """
        st.markdown(f"""
        <div class="dvz-insight-tag" key="{key or ''}">
            <i>💡</i> {text}
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def animated_container(children: Any, key: Optional[str] = None):
        """
        Create an animated container.
        
        Args:
            children: Streamlit elements to include in the container
            key: Optional unique key for the component
        """
        st.markdown(f'<div class="dvz-animated" key="{key or ""}"></div>', unsafe_allow_html=True)
        children

    @staticmethod
    def dashboard_row(cols: int = 2):
        """
        Create a dashboard row with specified number of columns.
        
        Args:
            cols: Number of columns
        
        Returns:
            List of streamlit columns
        """
        return st.columns(cols)

    @staticmethod
    def tabs(tab_names: List[str], key: Optional[str] = None):
        """
        Create custom styled tabs.
        
        Args:
            tab_names: List of tab names
            key: Optional unique key for the component
        
        Returns:
            Selected tab index
        """
        col1, col2 = st.columns([1, 3])
        
        with col1:
            selected_tab = st.radio("Select tab:", tab_names, label_visibility="collapsed", key=key)
        
        selected_index = tab_names.index(selected_tab)
        
        # Display tab indicator visually
        tab_html = '<div class="dvz-tabs">'
        for i, tab in enumerate(tab_names):
            active_class = "dvz-tab-active" if i == selected_index else ""
            tab_html += f'<div class="dvz-tab {active_class}">{tab}</div>'
        tab_html += '</div>'
        
        st.markdown(tab_html, unsafe_allow_html=True)
        
        return selected_index

    @staticmethod
    def metric_comparison(label: str, value: Union[int, float], delta: Union[int, float] = None, 
                          delta_suffix: str = "%", precision: int = 1):
        """
        Display a metric with comparison to previous value.
        
        Args:
            label: Metric label
            value: Current value
            delta: Change from previous value (optional)
            delta_suffix: Suffix for delta value (default: %)
            precision: Number of decimal places
        """
        # Format the delta value
        if delta is not None:
            if delta > 0:
                delta_color = "green"
                delta_value = f"+{delta:.{precision}f}{delta_suffix}"
            elif delta < 0:
                delta_color = "red"
                delta_value = f"{delta:.{precision}f}{delta_suffix}"
            else:
                delta_color = "gray"
                delta_value = f"{delta:.{precision}f}{delta_suffix}"
                
            st.metric(label=label, value=f"{value:,}", delta=delta_value)
        else:
            st.metric(label=label, value=f"{value:,}")

    @staticmethod
    def image_card(title: str, image: Union[str, Image.Image], caption: str = None, width: int = None):
        """
        Display an image inside a card.
        
        Args:
            title: Card title
            image: Image path or PIL Image object
            caption: Optional image caption
            width: Optional image width
        """
        with st.container():
            st.markdown(f'<div class="dvz-card-title">{title}</div>', unsafe_allow_html=True)
            st.image(image, caption=caption, width=width)

    @staticmethod
    def info_card(title: str, description: str, icon: str = "ℹ️"):
        """
        Display an info card with icon.
        
        Args:
            title: Card title
            description: Card description
            icon: Emoji icon
        """
        st.markdown(f"""
        <div class="dvz-card">
            <div style="display: flex; align-items: center;">
                <div style="font-size: 2rem; margin-right: 0.75rem;">{icon}</div>
                <div>
                    <div class="dvz-card-title">{title}</div>
                    <div>{description}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def feature_card(title: str, description: str, icon: str = "✨"):
        """
        Display a feature card.
        
        Args:
            title: Feature title
            description: Feature description
            icon: Emoji icon
        """
        st.markdown(f"""
        <div class="dvz-card">
            <div style="font-size: 1.5rem; color: var(--color-primary); margin-bottom: 0.5rem;">{icon}</div>
            <div class="dvz-card-title">{title}</div>
            <div>{description}</div>
        </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def kpi_card(value: Union[str, int, float], label: str, delta: Optional[float] = None, 
                 target: Optional[float] = None, icon: str = "📈"):
        """
        Display a KPI card with optional trend indicator.
        
        Args:
            value: The KPI value
            label: KPI description
            delta: Change from previous period (optional)
            target: Target value (optional)
            icon: Emoji icon
        """
        # Format the delta value if provided
        delta_html = ""
        if delta is not None:
            if delta > 0:
                delta_color = "#4CC9F0"
                delta_icon = "↑"
            elif delta < 0:
                delta_color = "#F72585"
                delta_icon = "↓"
            else:
                delta_color = "#6c757d"
                delta_icon = "→"
                
            delta_html = f"""
            <div style="color: {delta_color}; font-size: 0.875rem; font-weight: 500; margin-top: 0.25rem;">
                {delta_icon} {abs(delta):.1f}%
            </div>
            """
        
        # Format target information if provided
        target_html = ""
        if target is not None:
            progress = min(100, max(0, (float(value) / target) * 100)) if target != 0 else 0
            target_html = f"""
            <div style="margin-top: 0.5rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                    <span>Progress</span>
                    <span>{progress:.1f}% of {target:,}</span>
                </div>
                <div class="dvz-progress">
                    <div class="dvz-progress-bar" style="width: {progress}%"></div>
                </div>
            </div>
            """
        
        st.markdown(f"""
        <div class="dvz-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; color: #6c757d;">{label}</div>
                    <div style="font-size: 1.5rem; font-weight: 700; margin-top: 0.25rem;">{value:,}</div>
                    {delta_html}
                </div>
                <div style="font-size: 1.5rem;">{icon}</div>
            </div>
            {target_html}
        </div>
        """, unsafe_allow_html=True)


class ModernForm:
    """Modern form component with styled inputs and validation."""
    
    @staticmethod
    def load_css():
        """Load custom CSS for form elements."""
        st.markdown("""
        <style>
        /* Modern form styling */
        .modern-form-container {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
        
        .modern-form-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #212529;
        }
        
        .modern-form-label {
            font-size: 0.875rem;
            font-weight: 500;
            margin-bottom: 0.25rem;
            color: #495057;
        }
        
        .modern-form-hint {
            font-size: 0.75rem;
            color: #6c757d;
            margin-top: 0.25rem;
        }
        
        .modern-form-submit {
            background: #4361EE;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.5rem 1.25rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        
        .modern-form-submit:hover {
            background: #3051d3;
        }
        
        /* Override Streamlit's default form styling */
        div[data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
        }
        
        /* Streamlit select box styling */
        div[data-baseweb="select"] {
            border-radius: 4px !important;
        }
        
        /* Streamlit text input styling */
        div.stTextInput > div > div > input {
            border-radius: 4px !important;
        }
        
        /* Streamlit number input styling */
        div.stNumberInput > div > div > input {
            border-radius: 4px !important;
        }
        </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def form(title: str, key: str):
        """
        Create a styled form container.
        
        Args:
            title: Form title
            key: Unique form key
            
        Returns:
            Streamlit form
        """
        st.markdown(f'<div class="modern-form-title">{title}</div>', unsafe_allow_html=True)
        return st.form(key=key)

    @staticmethod
    def label(text: str, hint: str = None):
        """
        Display a form field label with optional hint.
        
        Args:
            text: Label text
            hint: Optional hint text
        """
        st.markdown(f'<div class="modern-form-label">{text}</div>', unsafe_allow_html=True)
        if hint:
            st.markdown(f'<div class="modern-form-hint">{hint}</div>', unsafe_allow_html=True)
            

class DataWidgets:
    """Custom widgets for data visualization and analysis."""
    
    @staticmethod
    def date_range_selector(data: pd.DataFrame, date_column: str, key: str = None):
        """
        Create a date range selector for a datetime column.
        
        Args:
            data: Pandas DataFrame
            date_column: Datetime column name
            key: Optional unique key prefix
            
        Returns:
            Tuple of (start_date, end_date)
        """
        if date_column not in data.columns or not pd.api.types.is_datetime64_dtype(data[date_column]):
            st.error(f"'{date_column}' is not a valid datetime column")
            return None, None
        
        min_date = data[date_column].min().date()
        max_date = data[date_column].max().date()
        
        col1, col2 = st.columns(2)
        
        with col1:
            start_date = st.date_input("Start date", min_date, min_value=min_date, max_value=max_date, key=f"{key}_start" if key else None)
        
        with col2:
            end_date = st.date_input("End date", max_date, min_value=min_date, max_value=max_date, key=f"{key}_end" if key else None)
        
        # Ensure start_date <= end_date
        if start_date > end_date:
            st.warning("Start date should be before or equal to end date")
            end_date = start_date
        
        return start_date, end_date

    @staticmethod
    def column_selector(data: pd.DataFrame, 
                        numeric_only: bool = False, 
                        categorical_only: bool = False,
                        label: str = "Select columns",
                        default: List[str] = None,
                        key: str = None):
        """
        Create a column selector with filtering options.
        
        Args:
            data: Pandas DataFrame
            numeric_only: Only show numeric columns
            categorical_only: Only show categorical columns
            label: Selector label
            default: Default selected columns
            key: Optional unique key
            
        Returns:
            List of selected column names
        """
        if numeric_only:
            available_cols = data.select_dtypes(include=['number']).columns.tolist()
            if not available_cols:
                st.warning("No numeric columns found in the dataset")
                return []
        elif categorical_only:
            available_cols = data.select_dtypes(include=['object']).columns.tolist()
            if not available_cols:
                st.warning("No categorical columns found in the dataset")
                return []
        else:
            available_cols = data.columns.tolist()
        
        if default is None:
            default = available_cols[:3] if len(available_cols) >= 3 else available_cols
        else:
            # Filter default to only include available columns
            default = [col for col in default if col in available_cols]
        
        return st.multiselect(label, available_cols, default=default, key=key)

    @staticmethod
    def outlier_filter(data: pd.DataFrame, numeric_column: str, key: str = None):
        """
        Create an outlier filter for a numeric column with a slider.
        
        Args:
            data: Pandas DataFrame
            numeric_column: Numeric column name
            key: Optional unique key
            
        Returns:
            DataFrame with outliers filtered
        """
        if numeric_column not in data.columns or not pd.api.types.is_numeric_dtype(data[numeric_column]):
            st.error(f"'{numeric_column}' is not a valid numeric column")
            return data
        
        # Calculate quartiles and IQR
        Q1 = data[numeric_column].quantile(0.25)
        Q3 = data[numeric_column].quantile(0.75)
        IQR = Q3 - Q1
        
        # Default outlier bounds (1.5 IQR)
        default_lower = Q1 - 1.5 * IQR
        default_upper = Q3 + 1.5 * IQR
        
        # Get min/max for slider
        min_val = data[numeric_column].min()
        max_val = data[numeric_column].max()
        
        st.markdown(f"#### Filter outliers in '{numeric_column}'")
        
        # Create range slider
        values = st.slider(
            "Select value range",
            float(min_val),
            float(max_val),
            (float(default_lower), float(default_upper)),
            key=key
        )
        
        # Apply filter
        filtered_data = data[(data[numeric_column] >= values[0]) & (data[numeric_column] <= values[1])]
        
        # Show how many rows were filtered
        original_rows = len(data)
        filtered_rows = len(filtered_data)
        excluded_rows = original_rows - filtered_rows
        
        if excluded_rows > 0:
            st.caption(f"Excluded {excluded_rows} rows ({excluded_rows/original_rows:.1%} of data) as outliers")
        
        return filtered_data
    
    @staticmethod
    def categorical_filter(data: pd.DataFrame, categorical_column: str, max_items: int = 10, key: str = None):
        """
        Create a categorical filter with checkboxes.
        
        Args:
            data: Pandas DataFrame
            categorical_column: Categorical column name
            max_items: Maximum number of categories to show
            key: Optional unique key
            
        Returns:
            DataFrame with categories filtered
        """
        if categorical_column not in data.columns:
            st.error(f"'{categorical_column}' is not a valid column")
            return data
        
        # Get value counts and sort by frequency
        value_counts = data[categorical_column].value_counts()
        
        # If too many categories, limit to top ones plus "Other"
        if len(value_counts) > max_items:
            top_categories = value_counts.head(max_items).index.tolist()
            has_other = True
        else:
            top_categories = value_counts.index.tolist()
            has_other = False
        
        st.markdown(f"#### Filter '{categorical_column}' categories")
        
        # Create a selectbox for "Select All" option
        select_all = st.checkbox("Select All", True, key=f"{key}_all" if key else None)
        
        # Create individual category checkboxes
        selected_categories = []
        for category in top_categories:
            # Convert category to string for display
            category_str = str(category)
            # Truncate long category names
            display_name = category_str if len(category_str) < 30 else category_str[:27] + "..."
            # Add count information
            display_name = f"{display_name} ({value_counts[category]:,})"
            
            if st.checkbox(display_name, select_all, key=f"{key}_{category}" if key else None):
                selected_categories.append(category)
        
        # Handle "Other" category
        include_other = False
        if has_other:
            other_count = value_counts[max_items:].sum()
            if st.checkbox(f"Other ({other_count:,})", select_all, key=f"{key}_other" if key else None):
                include_other = True
        
        # Apply filtering
        if has_other:
            if include_other:
                filtered_data = data[
                    data[categorical_column].isin(selected_categories) | 
                    ~data[categorical_column].isin(top_categories)
                ]
            else:
                filtered_data = data[data[categorical_column].isin(selected_categories)]
        else:
            filtered_data = data[data[categorical_column].isin(selected_categories)]
        
        # Show how many rows were filtered
        original_rows = len(data)
        filtered_rows = len(filtered_data)
        excluded_rows = original_rows - filtered_rows
        
        if excluded_rows > 0:
            st.caption(f"Excluded {excluded_rows} rows ({excluded_rows/original_rows:.1%} of data)")
        
        return filtered_data


class ChartBuilder:
    """Interactive chart builder for creating visualizations."""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the chart builder with a DataFrame.
        
        Args:
            data: Pandas DataFrame
        """
        self.data = data
        self.numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
        self.categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
        self.datetime_columns = data.select_dtypes(include=['datetime']).columns.tolist()
        self.all_columns = data.columns.tolist()
    
    def build(self, key_prefix: str = "chart_builder"):
        """
        Build an interactive chart based on user selection.
        
        Args:
            key_prefix: Prefix for component keys
            
        Returns:
            Plotly figure object
        """
        st.markdown("### Chart Builder")
        
        # Chart type selector
        chart_types = {
            "Bar Chart": "bar",
            "Line Chart": "line",
            "Scatter Plot": "scatter",
            "Histogram": "histogram",
            "Box Plot": "box",
            "Heatmap": "heatmap",
            "Pie Chart": "pie"
        }
        
        chart_type_name = st.selectbox(
            "Chart Type",
            options=list(chart_types.keys()),
            key=f"{key_prefix}_type"
        )
        chart_type = chart_types[chart_type_name]
        
        fig = None
        
        # Configure chart based on type
        if chart_type == "bar":
            fig = self._create_bar_chart(key_prefix)
        elif chart_type == "line":
            fig = self._create_line_chart(key_prefix)
        elif chart_type == "scatter":
            fig = self._create_scatter_chart(key_prefix)
        elif chart_type == "histogram":
            fig = self._create_histogram(key_prefix)
        elif chart_type == "box":
            fig = self._create_box_plot(key_prefix)
        elif chart_type == "heatmap":
            fig = self._create_heatmap(key_prefix)
        elif chart_type == "pie":
            fig = self._create_pie_chart(key_prefix)
        
        if fig:
            # Add common chart settings
            with st.expander("Chart Settings", expanded=False):
                # Title and layout settings
                title = st.text_input("Chart Title", f"{chart_type_name}", key=f"{key_prefix}_title")
                
                col1, col2 = st.columns(2)
                with col1:
                    height = st.slider("Height", 300, 1000, 500, 50, key=f"{key_prefix}_height")
                with col2:
                    width = st.slider("Width", 400, 1200, 700, 50, key=f"{key_prefix}_width")
                
                # Apply settings
                fig.update_layout(
                    title=title,
                    height=height,
                    width=width,
                    template="plotly_white"
                )
            
            return fig
        
        return None
    
    def _create_bar_chart(self, key_prefix: str):
        """Create a bar chart configuration."""
        st.markdown("#### Bar Chart Settings")
        
        x_col_options = self.categorical_columns + self.numeric_columns
        if not x_col_options:
            st.warning("No suitable columns found for the X-axis")
            return None
        
        x_col = st.selectbox("X-axis", x_col_options, key=f"{key_prefix}_bar_x")
        
        # For Y-axis, offer numeric columns or "count"
        y_options = ["Count"] + self.numeric_columns
        y_selection = st.selectbox("Y-axis", y_options, key=f"{key_prefix}_bar_y")
        
        # Color options
        color_col = st.selectbox(
            "Color (optional)", 
            ["None"] + self.categorical_columns, 
            key=f"{key_prefix}_bar_color"
        )
        color_col = None if color_col == "None" else color_col
        
        # Create the chart
        if y_selection == "Count":
            # Count-based bar chart
            fig = px.bar(
                self.data,
                x=x_col,
                color=color_col,
                title=f"Count by {x_col}"
            )
        else:
            # Value-based bar chart
            fig = px.bar(
                self.data,
                x=x_col,
                y=y_selection,
                color=color_col,
                title=f"{y_selection} by {x_col}"
            )
        
        return fig
    
    def _create_line_chart(self, key_prefix: str):
        """Create a line chart configuration."""
        st.markdown("#### Line Chart Settings")
        
        # Best x-axis options are datetime or numeric
        x_options = self.datetime_columns + self.numeric_columns
        if not x_options:
            st.warning("No suitable columns found for the X-axis")
            return None
        
        x_col = st.selectbox("X-axis", x_options, key=f"{key_prefix}_line_x")
        
        # Y-axis should be numeric
        if not self.numeric_columns:
            st.warning("No numeric columns found for the Y-axis")
            return None
        
        y_col = st.selectbox("Y-axis", self.numeric_columns, key=f"{key_prefix}_line_y")
        
        # Group by/color options
        color_col = st.selectbox(
            "Group by (optional)", 
            ["None"] + self.categorical_columns, 
            key=f"{key_prefix}_line_color"
        )
        color_col = None if color_col == "None" else color_col
        
        # Create the chart
        fig = px.line(
            self.data,
            x=x_col,
            y=y_col,
            color=color_col,
            title=f"{y_col} vs {x_col}"
        )
        
        return fig
    
    def _create_scatter_chart(self, key_prefix: str):
        """Create a scatter plot configuration."""
        st.markdown("#### Scatter Plot Settings")
        
        if len(self.numeric_columns) < 2:
            st.warning("Need at least two numeric columns for scatter plot")
            return None
        
        x_col = st.selectbox("X-axis", self.numeric_columns, key=f"{key_prefix}_scatter_x")
        
        # Filter out the selected x-column
        y_options = [col for col in self.numeric_columns if col != x_col]
        y_col = st.selectbox("Y-axis", y_options, key=f"{key_prefix}_scatter_y")
        
        # Additional options
        col1, col2 = st.columns(2)
        
        with col1:
            color_col = st.selectbox(
                "Color by (optional)", 
                ["None"] + self.all_columns, 
                key=f"{key_prefix}_scatter_color"
            )
            color_col = None if color_col == "None" else color_col
        
        with col2:
            size_col = st.selectbox(
                "Size by (optional)", 
                ["None"] + self.numeric_columns, 
                key=f"{key_prefix}_scatter_size"
            )
            size_col = None if size_col == "None" else size_col
        
        # Create the chart
        fig = px.scatter(
            self.data,
            x=x_col,
            y=y_col,
            color=color_col,
            size=size_col,
            title=f"{y_col} vs {x_col}"
        )
        
        return fig
    
    def _create_histogram(self, key_prefix: str):
        """Create a histogram configuration."""
        st.markdown("#### Histogram Settings")
        
        col = st.selectbox("Column", self.all_columns, key=f"{key_prefix}_hist_col")
        
        # Additional options
        col1, col2 = st.columns(2)
        
        with col1:
            bins = st.slider("Number of bins", 5, 100, 20, key=f"{key_prefix}_hist_bins")
        
        with col2:
            color_col = st.selectbox(
                "Color by (optional)", 
                ["None"] + self.categorical_columns, 
                key=f"{key_prefix}_hist_color"
            )
            color_col = None if color_col == "None" else color_col
        
        # Create the chart
        fig = px.histogram(
            self.data,
            x=col,
            color=color_col,
            nbins=bins,
            title=f"Distribution of {col}"
        )
        
        return fig
    
    def _create_box_plot(self, key_prefix: str):
        """Create a box plot configuration."""
        st.markdown("#### Box Plot Settings")
        
        if not self.numeric_columns:
            st.warning("No numeric columns found for Y-axis")
            return None
        
        y_col = st.selectbox("Value (Y-axis)", self.numeric_columns, key=f"{key_prefix}_box_y")
        
        # X-axis is optional for box plots
        x_col = st.selectbox(
            "Group by (X-axis, optional)", 
            ["None"] + self.categorical_columns, 
            key=f"{key_prefix}_box_x"
        )
        x_col = None if x_col == "None" else x_col
        
        # Additional options
        color_col = st.selectbox(
            "Color by (optional)", 
            ["None"] + self.categorical_columns, 
            key=f"{key_prefix}_box_color"
        )
        color_col = None if color_col == "None" else color_col
        
        # Create the chart
        fig = px.box(
            self.data,
            y=y_col,
            x=x_col,
            color=color_col,
            title=f"Distribution of {y_col}" + (f" by {x_col}" if x_col else "")
        )
        
        return fig
    
    def _create_heatmap(self, key_prefix: str):
        """Create a heatmap configuration."""
        st.markdown("#### Heatmap Settings")
        
        # Option for correlation matrix
        heatmap_type = st.radio(
            "Heatmap Type",
            ["Correlation Matrix", "Two-Column Heatmap"],
            key=f"{key_prefix}_heatmap_type"
        )
        
        if heatmap_type == "Correlation Matrix":
            if len(self.numeric_columns) < 2:
                st.warning("Need at least two numeric columns for correlation matrix")
                return None
            
            # Select columns for correlation
            corr_columns = st.multiselect(
                "Select columns for correlation",
                self.numeric_columns,
                default=self.numeric_columns[:min(6, len(self.numeric_columns))],
                key=f"{key_prefix}_corr_cols"
            )
            
            if not corr_columns or len(corr_columns) < 2:
                st.warning("Please select at least two columns")
                return None
            
            # Calculate correlation matrix
            corr_matrix = self.data[corr_columns].corr()
            
            # Create the heatmap
            fig = px.imshow(
                corr_matrix,
                text_auto='.2f',
                aspect="auto",
                color_continuous_scale="RdBu_r",
                title="Correlation Matrix"
            )
            
        else:  # Two-Column Heatmap
            if not self.categorical_columns:
                st.warning("No categorical columns found for axes")
                return None
            
            x_col = st.selectbox("X-axis", self.categorical_columns, key=f"{key_prefix}_heatmap_x")
            
            # Filter out selected x-column
            y_options = [col for col in self.categorical_columns if col != x_col]
            if not y_options:
                st.warning("Need a different column for Y-axis")
                return None
            
            y_col = st.selectbox("Y-axis", y_options, key=f"{key_prefix}_heatmap_y")
            
            # Create the heatmap
            fig = px.density_heatmap(
                self.data,
                x=x_col,
                y=y_col,
                title=f"Heatmap of {y_col} vs {x_col}"
            )
        
        return fig
    
    def _create_pie_chart(self, key_prefix: str):
        """Create a pie chart configuration."""
        st.markdown("#### Pie Chart Settings")
        
        # Names column (categories)
        names_col = st.selectbox(
            "Categories", 
            self.categorical_columns, 
            key=f"{key_prefix}_pie_names"
        )
        
        # Values column
        values_options = ["Count"] + self.numeric_columns
        values_selection = st.selectbox(
            "Values", 
            values_options, 
            key=f"{key_prefix}_pie_values"
        )
        
        if values_selection == "Count":
            # Count occurrences of each category
            value_counts = self.data[names_col].value_counts().reset_index()
            value_counts.columns = [names_col, 'count']
            
            fig = px.pie(
                value_counts,
                names=names_col,
                values='count',
                title=f"Distribution of {names_col}"
            )
        else:
            # Use the selected numeric column
            fig = px.pie(
                self.data,
                names=names_col,
                values=values_selection,
                title=f"Distribution of {values_selection} by {names_col}"
            )
        
        # Additional options
        hole = st.slider("Donut hole size", 0.0, 0.8, 0.0, 0.1, key=f"{key_prefix}_pie_hole")
        fig.update_traces(hole=hole)
        
        return fig


# Utility functions for the component library
def dataframe_to_csv_download(data: pd.DataFrame, filename: str = "data.csv"):
    """
    Create a download link for a DataFrame.
    
    Args:
        data: Pandas DataFrame
        filename: Download filename
        
    Returns:
        Download link HTML
    """
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" class="dvz-button dvz-button-primary">Download CSV</a>'
    return href


def image_to_base64(image_path: str) -> str:
    """
    Convert an image to base64 encoding.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Base64 encoded string
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def pil_image_to_base64(pil_image: Image.Image) -> str:
    """
    Convert a PIL Image to base64 encoding.
    
    Args:
        pil_image: PIL Image object
        
    Returns:
        Base64 encoded string
    """
    buffered = io.BytesIO()
    pil_image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()