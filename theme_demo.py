import streamlit as st
from custom_theme import ModernTheme, CustomPanels, BackgroundEffects
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    """Theme demo application"""
    st.set_page_config(
        page_title="Custom Theme Demo",
        page_icon="🎨",
        layout="wide"
    )
    
    # Initialize theme and load CSS
    selected_theme = ModernTheme.create_theme_selector()
    CustomPanels.load_css()
    
    # Background pattern/gradient selection
    bg_type = st.sidebar.radio("Background Style", ["None", "Gradient", "Pattern"])
    if bg_type == "Gradient":
        direction = st.sidebar.selectbox(
            "Gradient Direction", 
            ["to right", "to left", "to bottom", "to top", "to bottom right", "to bottom left"]
        )
        primary_color = st.sidebar.color_picker("Primary Color", ModernTheme.THEMES[selected_theme]["primaryColor"])
        secondary_color = st.sidebar.color_picker("Secondary Color", "#7209B7")
        BackgroundEffects.gradient_background([primary_color, secondary_color], direction)
    elif bg_type == "Pattern":
        pattern = st.sidebar.selectbox("Pattern Type", ["circuit", "dots", "waves"])
        BackgroundEffects.pattern_background(pattern)
    
    # Hero section
    CustomPanels.hero_section(
        "Modern UI Theming Framework",
        "Create beautiful and consistent UIs with custom themes and components",
        "Explore Components"
    )
    
    # Feature panels
    st.markdown("## Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        CustomPanels.feature_panel(
            "Custom Themes",
            "Apply predefined themes or create your own with custom colors and fonts.",
            "🎨"
        )
    
    with col2:
        CustomPanels.feature_panel(
            "Modern UI Components",
            "Responsive and visually appealing components for your Streamlit apps.",
            "🧩"
        )
    
    with col3:
        CustomPanels.feature_panel(
            "Background Effects",
            "Add gradient backgrounds and patterns to enhance visual appeal.",
            "✨"
        )
    
    # Panel examples
    st.markdown("## Panel Components")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("### Basic Panel")
            with st.expander("Show code", expanded=False):
                st.code("""
CustomPanels.panel(
    content=st.markdown("This is a basic panel with a title and content."),
    title="Basic Panel"
)
                """)
            
            CustomPanels.panel(
                content=st.markdown("This is a basic panel with a title and content."),
                title="Basic Panel"
            )
    
    with col2:
        with st.container():
            st.markdown("### Primary Panel")
            with st.expander("Show code", expanded=False):
                st.code("""
CustomPanels.panel(
    content=st.markdown("This is a panel with a primary variant."),
    title="Primary Panel",
    variant="primary"
)
                """)
            
            CustomPanels.panel(
                content=st.markdown("This is a panel with a primary variant."),
                title="Primary Panel",
                variant="primary"
            )
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("### Success Panel")
            with st.expander("Show code", expanded=False):
                st.code("""
CustomPanels.panel(
    content=st.markdown("This is a panel with a success variant."),
    title="Success Panel",
    variant="success"
)
                """)
            
            CustomPanels.panel(
                content=st.markdown("This is a panel with a success variant."),
                title="Success Panel",
                variant="success"
            )
    
    with col2:
        with st.container():
            st.markdown("### Warning Panel")
            with st.expander("Show code", expanded=False):
                st.code("""
CustomPanels.panel(
    content=st.markdown("This is a panel with a warning variant."),
    title="Warning Panel",
    variant="warning"
)
                """)
            
            CustomPanels.panel(
                content=st.markdown("This is a panel with a warning variant."),
                title="Warning Panel",
                variant="warning"
            )
    
    # Theme presets
    st.markdown("## Theme Presets")
    st.write("Choose a theme from the sidebar to see different presets in action.")
    
    # Display theme colors
    theme = ModernTheme.THEMES[selected_theme]
    
    st.markdown("### Current Theme Colors")
    color_cols = st.columns(5)
    
    with color_cols[0]:
        st.markdown(f"""
        <div style="background-color: {theme['primaryColor']}; height: 50px; border-radius: 5px; margin-bottom: 10px;"></div>
        <p style="text-align: center;">Primary</p>
        """, unsafe_allow_html=True)
    
    with color_cols[1]:
        st.markdown(f"""
        <div style="background-color: {theme['backgroundColor']}; height: 50px; border-radius: 5px; margin-bottom: 10px; border: 1px solid #ddd;"></div>
        <p style="text-align: center;">Background</p>
        """, unsafe_allow_html=True)
    
    with color_cols[2]:
        st.markdown(f"""
        <div style="background-color: {theme['secondaryBackgroundColor']}; height: 50px; border-radius: 5px; margin-bottom: 10px; border: 1px solid #ddd;"></div>
        <p style="text-align: center;">Secondary</p>
        """, unsafe_allow_html=True)
    
    with color_cols[3]:
        st.markdown(f"""
        <div style="background-color: {theme['textColor']}; height: 50px; border-radius: 5px; margin-bottom: 10px;"></div>
        <p style="text-align: center;">Text</p>
        """, unsafe_allow_html=True)
    
    with color_cols[4]:
        gradient_colors = [theme['primaryColor'], "#7209B7"]
        gradient = f"linear-gradient(to right, {gradient_colors[0]}, {gradient_colors[1]})"
        st.markdown(f"""
        <div style="background: {gradient}; height: 50px; border-radius: 5px; margin-bottom: 10px;"></div>
        <p style="text-align: center;">Gradient</p>
        """, unsafe_allow_html=True)
    
    # Sample data visualization with theme
    st.markdown("## Styled Data Visualization")
    st.write("Data visualizations with theme-consistent styling")
    
    # Generate sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'category': ['A', 'B', 'C', 'D', 'E'] * 10,
        'value': np.random.normal(50, 10, 50),
        'group': np.random.choice(['Group 1', 'Group 2', 'Group 3'], 50)
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Bar Chart")
        
        fig = px.bar(
            data.groupby('category')['value'].mean().reset_index(),
            x='category',
            y='value',
            color_discrete_sequence=[theme['primaryColor']],
            title="Average Values by Category"
        )
        
        # Apply consistent styling with theme
        fig.update_layout(
            plot_bgcolor=theme['backgroundColor'],
            paper_bgcolor=theme['backgroundColor'],
            font_color=theme['textColor'],
            title_font_family=theme['font']
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Scatter Plot")
        
        fig = px.scatter(
            data,
            x='category',
            y='value',
            color='group',
            title="Values by Category and Group"
        )
        
        # Apply consistent styling with theme
        fig.update_layout(
            plot_bgcolor=theme['backgroundColor'],
            paper_bgcolor=theme['backgroundColor'],
            font_color=theme['textColor'],
            title_font_family=theme['font']
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # CTA panel
    CustomPanels.cta_panel(
        "Ready to Enhance Your UI?",
        "Integrate these components into your own Streamlit applications for a modern, cohesive UI.",
        "Get Started"
    )
    
    # Code examples
    st.markdown("## How to Use")
    
    with st.expander("Theme Setup", expanded=False):
        st.code("""
# Import the theme module
from custom_theme import ModernTheme

# Apply a predefined theme
ModernTheme.apply_theme("dark")  # Options: default, dark, colorful, minimal, elegant

# Or create a theme selector
selected_theme = ModernTheme.create_theme_selector()

# Or set a custom theme
ModernTheme.set_theme(
    primaryColor="#4361EE",
    backgroundColor="#FFFFFF",
    secondaryBackgroundColor="#F8F9FA",
    textColor="#262730",
    font="Inter"
)
        """)
    
    with st.expander("Panel Components", expanded=False):
        st.code("""
# Import panel components
from custom_theme import CustomPanels

# Load the required CSS
CustomPanels.load_css()

# Create a feature panel
CustomPanels.feature_panel(
    title="Feature Title",
    description="Feature description goes here.",
    icon="✨"
)

# Create a hero section
CustomPanels.hero_section(
    title="Hero Title",
    subtitle="Hero subtitle goes here",
    cta_text="Get Started"
)

# Create a call-to-action panel
CustomPanels.cta_panel(
    title="Ready to Get Started?",
    description="Start using these components today!",
    button_text="Get Started"
)
        """)
    
    with st.expander("Background Effects", expanded=False):
        st.code("""
# Import background effects
from custom_theme import BackgroundEffects

# Apply a gradient background
BackgroundEffects.gradient_background(
    colors=["#4361EE", "#3A0CA3"],
    direction="to right"  # Options: "to right", "to left", "to bottom", "to top", etc.
)

# Apply a pattern background
BackgroundEffects.pattern_background(
    pattern_type="circuit"  # Options: "circuit", "dots", "waves"
)
        """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Modern UI Theme Framework • Created with ❤️ using Streamlit"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()