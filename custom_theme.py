import streamlit as st
import base64
from typing import Dict, Any, List, Optional

class ModernTheme:
    """A class to create and apply custom themes to a Streamlit application."""
    
    # Theme presets
    THEMES = {
        "default": {
            "primaryColor": "#4361EE",
            "backgroundColor": "#FFFFFF",
            "secondaryBackgroundColor": "#F8F9FA",
            "textColor": "#262730",
            "font": "Inter"
        },
        "dark": {
            "primaryColor": "#4CC9F0",
            "backgroundColor": "#1A1A1A",
            "secondaryBackgroundColor": "#252525",
            "textColor": "#F9F9F9",
            "font": "Inter"
        },
        "colorful": {
            "primaryColor": "#7209B7",
            "backgroundColor": "#FFFFFF",
            "secondaryBackgroundColor": "#F0F2F6",
            "textColor": "#262730",
            "font": "Poppins"
        },
        "minimal": {
            "primaryColor": "#0077B6",
            "backgroundColor": "#FFFFFF",
            "secondaryBackgroundColor": "#F8F9FA",
            "textColor": "#2A2A2A",
            "font": "Roboto"
        },
        "elegant": {
            "primaryColor": "#6A0572",
            "backgroundColor": "#FFFFFF",
            "secondaryBackgroundColor": "#F7F3FB",
            "textColor": "#333333",
            "font": "Playfair Display"
        }
    }
    
    # Font options
    FONTS = {
        "Inter": "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
        "Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap",
        "Roboto": "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap",
        "Lato": "https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap",
        "Montserrat": "https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap",
        "Open Sans": "https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap",
        "Playfair Display": "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&display=swap",
        "JetBrains Mono": "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap"
    }
    
    @staticmethod
    def apply_theme(theme_name: str = "default"):
        """
        Apply a predefined theme to the Streamlit app.
        
        Args:
            theme_name: Name of the theme to apply (default, dark, colorful, minimal, elegant)
        """
        theme = ModernTheme.THEMES.get(theme_name, ModernTheme.THEMES["default"])
        ModernTheme.set_theme(**theme)
    
    @staticmethod
    def set_theme(
        primaryColor: str,
        backgroundColor: str,
        secondaryBackgroundColor: str,
        textColor: str,
        font: str = "Inter"
    ):
        """
        Set a custom theme with the specified colors and font.
        
        Args:
            primaryColor: Primary color for buttons, links, etc.
            backgroundColor: Background color for the main content
            secondaryBackgroundColor: Background color for sidebar and cards
            textColor: Text color
            font: Font family to use
        """
        # Load the font CSS
        font_url = ModernTheme.FONTS.get(font, ModernTheme.FONTS["Inter"])
        
        # Apply the theme
        st.markdown(f"""
        <style>
        @import url('{font_url}');
        
        :root {{
            --primary-color: {primaryColor};
            --background-color: {backgroundColor};
            --secondary-background-color: {secondaryBackgroundColor};
            --text-color: {textColor};
            --font: {font}, sans-serif;
        }}
        
        .stApp {{
            background-color: var(--background-color);
            color: var(--text-color);
            font-family: var(--font);
        }}
        
        .stTextInput > div > div > input,
        .stSelectbox > div > div > div,
        .stTextArea > div > div > textarea {{
            background-color: var(--background-color);
            color: var(--text-color);
        }}
        
        .stButton > button {{
            background-color: var(--primary-color);
            color: white;
        }}
        
        .stSidebar {{
            background-color: var(--secondary-background-color);
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-family: var(--font);
            color: var(--text-color);
        }}
        
        .stTabs [data-baseweb="tab-list"] {{
            gap: 2px;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            height: auto;
            white-space: pre-wrap;
            background-color: var(--secondary-background-color);
            border-radius: 4px 4px 0 0;
            gap: 1px;
            padding: 0.5rem 1rem;
        }}
        
        .stTabs [aria-selected="true"] {{
            background-color: var(--primary-color) !important;
            color: white !important;
        }}
        
        div[data-testid="stExpander"] {{
            border-radius: 8px;
            border: 1px solid rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        div[data-testid="stExpander"] > div[role="button"] {{
            background-color: var(--secondary-background-color);
            transition: background-color 0.3s;
        }}
        
        div[data-testid="stExpander"] > div[role="button"]:hover {{
            background-color: rgba(0,0,0,0.05);
        }}
        
        div[data-testid="stImage"] {{
            border-radius: 4px;
            overflow: hidden;
        }}
        
        div[data-testid="stMarkdownContainer"] a {{
            color: var(--primary-color);
            text-decoration: none;
        }}
        
        div[data-testid="stMarkdownContainer"] a:hover {{
            text-decoration: underline;
        }}
        
        /* Card-like elements */
        div.stMetric {{
            background-color: var(--secondary-background-color);
            border-radius: 8px;
            padding: 10px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        }}
        
        div[data-testid="stMetricValue"] {{
            font-size: 1.8rem;
            font-weight: 600;
            color: var(--primary-color);
        }}
        
        div[data-testid="stMetricLabel"] {{
            font-size: 0.8rem;
            color: rgba(0,0,0,0.6);
        }}
        
        div[data-testid="stDataFrameContainer"] {{
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid rgba(0,0,0,0.1);
        }}
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def create_theme_selector():
        """
        Create a theme selector in the sidebar.
        
        Returns:
            Selected theme name
        """
        themes = list(ModernTheme.THEMES.keys())
        selected_theme = st.sidebar.selectbox("Select theme", themes, index=0)
        
        # Apply the selected theme immediately
        ModernTheme.apply_theme(selected_theme)
        
        return selected_theme

class CustomPanels:
    """A class to create custom panels and containers for Streamlit apps."""
    
    @staticmethod
    def load_css():
        """Load custom CSS for panels and containers."""
        st.markdown("""
        <style>
        /* Panel container */
        .custom-panel {
            background-color: var(--secondary-background-color, #F8F9FA);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            border: 1px solid rgba(0,0,0,0.05);
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        
        /* Panel with header */
        .panel-header {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(0,0,0,0.1);
        }
        
        /* Panel with different variants */
        .panel-primary {
            border-left: 4px solid var(--primary-color, #4361EE);
        }
        
        .panel-success {
            border-left: 4px solid #4CAF50;
        }
        
        .panel-warning {
            border-left: 4px solid #FFC107;
        }
        
        .panel-danger {
            border-left: 4px solid #F44336;
        }
        
        .panel-info {
            border-left: 4px solid #03A9F4;
        }
        
        /* Hero section */
        .hero-section {
            text-align: center;
            padding: 30px 20px;
            margin-bottom: 30px;
            background: linear-gradient(90deg, #4361EE, #3A0CA3);
            color: white;
            border-radius: 8px;
        }
        
        .hero-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 10px;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
            font-weight: 400;
            opacity: 0.9;
            margin-bottom: 20px;
        }
        
        /* Feature panels for landing pages */
        .feature-panel {
            display: flex;
            background-color: var(--secondary-background-color, #F8F9FA);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .feature-panel:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        }
        
        .feature-icon {
            font-size: 2rem;
            margin-right: 20px;
            color: var(--primary-color, #4361EE);
        }
        
        .feature-content {
            flex: 1;
        }
        
        .feature-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .feature-description {
            font-size: 0.9rem;
            color: rgba(0,0,0,0.6);
        }
        
        /* Call to action panel */
        .cta-panel {
            background: linear-gradient(90deg, #7209B7, #4361EE);
            color: white;
            border-radius: 8px;
            padding: 30px;
            margin: 30px 0;
            text-align: center;
        }
        
        .cta-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 15px;
        }
        
        .cta-description {
            font-size: 1rem;
            margin-bottom: 20px;
            opacity: 0.9;
        }
        
        .cta-button {
            display: inline-block;
            background-color: white;
            color: #4361EE;
            padding: 8px 24px;
            border-radius: 4px;
            font-weight: 600;
            text-decoration: none;
            transition: transform 0.2s;
        }
        
        .cta-button:hover {
            transform: scale(1.05);
        }
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def panel(content: Any, title: Optional[str] = None, variant: str = None):
        """
        Create a custom styled panel.
        
        Args:
            content: Content to display in the panel
            title: Optional panel title
            variant: Panel variant (primary, success, warning, danger, info)
        """
        variant_class = f"panel-{variant}" if variant else ""
        
        panel_html = f'<div class="custom-panel {variant_class}">'
        
        if title:
            panel_html += f'<div class="panel-header">{title}</div>'
        
        panel_html += '</div>'
        
        st.markdown(panel_html, unsafe_allow_html=True)
        
        # Display the content
        content
    
    @staticmethod
    def hero_section(title: str, subtitle: str, cta_text: Optional[str] = None):
        """
        Create a hero section for a landing page.
        
        Args:
            title: Hero section title
            subtitle: Hero section subtitle
            cta_text: Optional call-to-action button text
        """
        cta_html = ""
        if cta_text:
            cta_html = f'<button class="cta-button">{cta_text}</button>'
        
        hero_html = f"""
        <div class="hero-section">
            <div class="hero-title">{title}</div>
            <div class="hero-subtitle">{subtitle}</div>
            {cta_html}
        </div>
        """
        
        st.markdown(hero_html, unsafe_allow_html=True)
    
    @staticmethod
    def feature_panel(title: str, description: str, icon: str = "✨"):
        """
        Create a feature panel for landing pages.
        
        Args:
            title: Feature title
            description: Feature description
            icon: Emoji or icon to display
        """
        feature_html = f"""
        <div class="feature-panel">
            <div class="feature-icon">{icon}</div>
            <div class="feature-content">
                <div class="feature-title">{title}</div>
                <div class="feature-description">{description}</div>
            </div>
        </div>
        """
        
        st.markdown(feature_html, unsafe_allow_html=True)
    
    @staticmethod
    def cta_panel(title: str, description: str, button_text: str = "Get Started"):
        """
        Create a call-to-action panel.
        
        Args:
            title: CTA title
            description: CTA description
            button_text: Button text
        """
        cta_html = f"""
        <div class="cta-panel">
            <div class="cta-title">{title}</div>
            <div class="cta-description">{description}</div>
            <button class="cta-button">{button_text}</button>
        </div>
        """
        
        st.markdown(cta_html, unsafe_allow_html=True)


class BackgroundEffects:
    """A class to create custom background effects for Streamlit apps."""
    
    @staticmethod
    def gradient_background(
        colors: List[str] = ["#4361EE", "#3A0CA3"],
        direction: str = "to right"
    ):
        """
        Apply a gradient background to the app.
        
        Args:
            colors: List of color hex codes
            direction: CSS gradient direction
        """
        color_str = ", ".join(colors)
        
        st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient({direction}, {color_str});
        }}
        
        .stSidebar {{
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }}
        
        /* Make content areas have white background */
        .stText, .stMarkdown, .stDataFrame, .stTable, .element-container {{
            background-color: white;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }}
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def pattern_background(pattern_type: str = "circuit"):
        """
        Apply a patterned background to the app.
        
        Args:
            pattern_type: Type of pattern (circuit, dots, waves)
        """
        patterns = {
            "circuit": """
            background-color: #ffffff;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 304 304' width='304' height='304'%3E%3Cpath fill='%23000000' fill-opacity='0.05' d='M44.1 224a5 5 0 1 1 0 2H0v-2h44.1zm160 48a5 5 0 1 1 0 2H82v-2h122.1zm57.8-46a5 5 0 1 1 0-2H304v2h-42.1zm0 16a5 5 0 1 1 0-2H304v2h-42.1zm6.2-114a5 5 0 1 1 0 2h-86.2a5 5 0 1 1 0-2h86.2zm-256-48a5 5 0 1 1 0 2H0v-2h12.1zm185.8 34a5 5 0 1 1 0-2h86.2a5 5 0 1 1 0 2h-86.2zM258 12.1a5 5 0 1 1-2 0V0h2v12.1zm-64 208a5 5 0 1 1-2 0v-54.2a5 5 0 1 1 2 0v54.2zm48-198.2V80h62v2h-64V21.9a5 5 0 1 1 2 0zm16 16V64h46v2h-48V37.9a5 5 0 1 1 2 0zm-128 96V208h16v12.1a5 5 0 1 1-2 0V210h-16v-76.1a5 5 0 1 1 2 0zm-5.9-21.9a5 5 0 1 1 0 2H114v48H85.9a5 5 0 1 1 0-2H112v-48h12.1zm-6.2 130a5 5 0 1 1 0-2H176v-74.1a5 5 0 1 1 2 0V242h-60.1zm-16-64a5 5 0 1 1 0-2H114v48h10.1a5 5 0 1 1 0 2H112v-48h-10.1zM66 284.1a5 5 0 1 1-2 0V274H50v30h-2v-32h18v12.1zM236.1 176a5 5 0 1 1 0 2H226v94h48v32h-2v-30h-48v-98h12.1zm25.8-30a5 5 0 1 1 0-2H274v44.1a5 5 0 1 1-2 0V146h-10.1zm-64 96a5 5 0 1 1 0-2H208v-80h16v-14h-42.1a5 5 0 1 1 0-2H226v18h-16v80h-12.1zm86.2-210a5 5 0 1 1 0 2H272V0h2v32h10.1zM98 101.9V146H53.9a5 5 0 1 1 0-2H96v-42.1a5 5 0 1 1 2 0zM53.9 34a5 5 0 1 1 0-2H80V0h2v34H53.9zm60.1 3.9V66H82v64H69.9a5 5 0 1 1 0-2H80V64h32V37.9a5 5 0 1 1 2 0zM101.9 82a5 5 0 1 1 0-2H128V37.9a5 5 0 1 1 2 0V82h-28.1zm16-64a5 5 0 1 1 0-2H146v44.1a5 5 0 1 1-2 0V18h-26.1zm102.2 270a5 5 0 1 1 0 2H98v14h-2v-16h124.1zM242 149.9V160h16v34h-16v62h48v48h-2v-46h-48v-66h16v-30h-16v-12.1a5 5 0 1 1 2 0zM53.9 18a5 5 0 1 1 0-2H64V2H48V0h18v18H53.9zm112 32a5 5 0 1 1 0-2H192V0h50v2h-48v48h-28.1zm-48-48a5 5 0 0 1-9.8-2h2.07a3 3 0 1 0 5.66 0H178v34h-18V21.9a5 5 0 1 1 2 0V32h14V2h-58.1zm0 96a5 5 0 1 1 0-2H137l32-32h39V21.9a5 5 0 1 1 2 0V66h-40.17l-32 32H117.9zm28.1 90.1a5 5 0 1 1-2 0v-76.51L175.59 80H224V21.9a5 5 0 1 1 2 0V82h-49.59L146 112.41v75.69zm16 32a5 5 0 1 1-2 0v-99.51L184.59 96H300.1a5 5 0 0 1 3.9-3.9v2.07a3 3 0 0 0 0 5.66v2.07a5 5 0 0 1-3.9-3.9H185.41L162 121.41v98.69zm-144-64a5 5 0 1 1-2 0v-3.51l48-48V48h32V0h2v50H66v55.41l-48 48v2.69zM50 53.9v43.51l-48 48V208h26.1a5 5 0 1 1 0 2H0v-65.41l48-48V53.9a5 5 0 1 1 2 0zm-16 16V89.41l-34 34v-2.82l32-32V69.9a5 5 0 1 1 2 0zM12.1 32a5 5 0 1 1 0 2H9.41L0 43.41V40.6L8.59 32h3.51zm265.8 18a5 5 0 1 1 0-2h18.69l7.41-7.41v2.82L297.41 50H277.9zm-16 160a5 5 0 1 1 0-2H288v-71.41l16-16v2.82l-14 14V210h-28.1zm-208 32a5 5 0 1 1 0-2H64v-22.59L40.59 194H21.9a5 5 0 1 1 0-2H41.41L66 217.59V242H53.9zm150.2 14a5 5 0 1 1 0 2H96v-56.6L56.6 162H37.9a5 5 0 1 1 0-2h19.5L98 200.6V256h106.1zm-150.2 2a5 5 0 1 1 0-2H80v-46.59L48.59 178H21.9a5 5 0 1 1 0-2H49.41L82 208.59V258H53.9zM34 39.8v1.61L9.41 66H0v-2h8.59L32 40.59V0h2v39.8zM2 300.1a5 5 0 0 1 3.9 3.9H3.83A3 3 0 0 0 0 302.17V256h18v48h-2v-46H2v42.1zM34 241v63h-2v-62H0v-2h34v1zM17 18H0v-2h16V0h2v18h-1zm273-2h14v2h-16V0h2v16zm-32 273v15h-2v-14h-14v14h-2v-16h18v1zM0 92.1A5.02 5.02 0 0 1 6 97a5 5 0 0 1-6 4.9v-2.07a3 3 0 1 0 0-5.66V92.1zM80 272h2v32h-2v-32zm37.9 32h-2.07a3 3 0 0 0-5.66 0h-2.07a5 5 0 0 1 9.8 0zM5.9 0A5.02 5.02 0 0 1 0 5.9V3.83A3 3 0 0 0 3.83 0H5.9zm294.2 0h2.07A3 3 0 0 0 304 3.83V5.9a5 5 0 0 1-3.9-5.9zm3.9 300.1v2.07a3 3 0 0 0-1.83 1.83h-2.07a5 5 0 0 1 3.9-3.9zM97 100a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-48 32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm32 48a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm32-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0-32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm32 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16-64a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 96a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16-144a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16-32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-96 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16-32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm96 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16-64a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-32 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM49 36a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-32 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm32 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM33 68a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16-48a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 240a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16-64a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16-32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm80-176a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm32 48a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0-32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm112 176a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-16 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM17 180a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 16a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0-32a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM17 84a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm32 64a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm16-16a3 3 0 1 0 0-6 3 3 0 0 0 0 6z'%3E%3C/path%3E%3C/svg%3E");
            """,
            
            "dots": """
            background-color: #ffffff;
            background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23000000' fill-opacity='0.05' fill-rule='evenodd'%3E%3Ccircle cx='3' cy='3' r='3'/%3E%3Ccircle cx='13' cy='13' r='3'/%3E%3C/g%3E%3C/svg%3E");
            """,
            
            "waves": """
            background-color: #ffffff;
            background-image: url("data:image/svg+xml,%3Csvg width='100' height='20' viewBox='0 0 100 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M21.184 20c.357-.13.72-.264.888-.14 1.254.902 1.854 2.997 2.475 4.875.344.996.837 1.805 1.537 2.227.882.533 1.87.64 2.913.297 1.45-.476 2.846-1.315 2.79-1.305 1.017-.74 1.44-.607 2.335-.082 1.215.703 1.952 2.343 2.606 3.777.134.292.26.594.382.905.12.31.238.638.344.98.105.343.2.7.276 1.067.077.365.133.737.17 1.107.038.37.057.743.056 1.116 0 .344-.035.656-.085.948-1.03-.282-2.19-.55-3.14-.825-.71-.206-1.167-.237-1.796.238-.306.23-.55.539-.78.913-.5.822-.857 1.988-1.274 3.257-.416 1.37-.803 2.857-1.316 3.934-.46.976-1.05 1.536-1.964 1.857-.785.275-1.68.35-2.654.16-1.306-.268-2.648-1.008-3.47-1.26-.214-.066-.378.01-.56.188-.36.347-.614.895-.852 1.47-.344.83-.678 1.7-1.16 2.21-.332.35-.805.473-1.528.38-.604-.08-1.204-.289-1.645-.77-.435-.476-.7-1.155-.635-1.892.08-.906.485-1.915.83-2.923.175-.5.336-.975.48-1.425.142-.447.266-.873.37-1.273.116-.433.197-.83.254-1.201.056-.375.091-.719.098-1.04.007-.332-.012-.64-.072-.919-.081-.376-.227-.707-.435-.992-.364-.501-.84-.908-1.38-1.234-.354-.213-.722-.384-1.098-.52-.376-.132-.76-.233-1.144-.299-.385-.066-.77-.1-1.147-.09-.375.01-.74.066-1.075.174-.75.243-1.328.696-1.705 1.46-.16.32-.318.74-.493 1.21l-.092.252c-.737-.03-1.047-.322-1.263-.537-.279-.277-.578-.614-.795-1.24-.105-.307-.24-.776-.308-1.313-.05-.394-.034-1.782.013-2.306.015-.175.03-.366.043-.567.013-.214.022-.436.03-.655.004-.13.007-.248.01-.354v-.03c.001-.084.002-.152.002-.2V.093L0 0h21.184v20z' fill='%23000000' fill-opacity='0.05' fill-rule='evenodd'/%3E%3C/svg%3E");
            """
        }
        
        if pattern_type not in patterns:
            pattern_type = "circuit"
        
        st.markdown(f"""
        <style>
        .stApp {{
            {patterns[pattern_type]}
        }}
        
        .stSidebar {{
            background-color: rgba(255, 255, 255, 0.9);
        }}
        
        /* Make content areas more distinct */
        .stText, .stMarkdown, .stDataFrame, .stTable {{
            background-color: white !important;
            padding: 10px !important;
            border-radius: 8px !important;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
            margin-bottom: 10px !important;
        }}
        </style>
        """, unsafe_allow_html=True)


def create_theme_demo():
    """Create a demonstration of the custom theme components."""
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
        "Modern Streamlit Theming",
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
            CustomPanels.panel(
                content=st.markdown("This is a basic panel with a title and content."),
                title="Basic Panel"
            )
    
    with col2:
        with st.container():
            CustomPanels.panel(
                content=st.markdown("This is a panel with a primary variant."),
                title="Primary Panel",
                variant="primary"
            )
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            CustomPanels.panel(
                content=st.markdown("This is a panel with a success variant."),
                title="Success Panel",
                variant="success"
            )
    
    with col2:
        with st.container():
            CustomPanels.panel(
                content=st.markdown("This is a panel with a warning variant."),
                title="Warning Panel",
                variant="warning"
            )
    
    # CTA panel
    CustomPanels.cta_panel(
        "Ready to Try It Out?",
        "Integrate these components into your own Streamlit applications for a modern, cohesive UI.",
        "Get Started"
    )
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Modern Streamlit Theme Demo • Created with ❤️ using Streamlit"
        "</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    create_theme_demo()