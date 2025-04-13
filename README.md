# Modern UI Component Library for Streamlit

A unique and modern component library for Streamlit applications that provides a beautiful, responsive, and customizable UI framework. This library includes a comprehensive set of components for creating data-driven web applications with consistent styling.

## Features

- **Modern UI Components**: A collection of visually appealing UI components with consistent styling
- **Custom Theming System**: Apply predefined themes or create your own with custom colors and fonts
- **Interactive Data Widgets**: Specialized components for data filtering, visualization, and analysis
- **Background Effects**: Add gradient backgrounds and patterns to enhance visual appeal
- **Responsive Design**: Components adapt to different screen sizes and viewport dimensions
- **Comprehensive CSS Framework**: Consistent styling across all components

## Component Libraries

The package consists of three main modules:

### 1. UI Components (`ui_components.py`)

A comprehensive set of UI components for data visualization and dashboard creation:

- **Cards**: Various card styles including info cards, stat cards, and KPI cards
- **Data Tables**: Styled data tables with proper formatting
- **Charts**: Chart containers with consistent styling
- **Badges & Alerts**: Visual indicators for different types of information
- **Progress Bars**: Visual indicators for progress or completion
- **Layout Helpers**: Tools for creating responsive dashboard layouts
- **Interactive Widgets**: Form elements and specialized data widgets

### 2. Custom Theming (`custom_theme.py`)

A theming system for creating consistent UIs:

- **Theme Presets**: Several predefined themes (default, dark, colorful, etc.)
- **Font Management**: Management of typography with Google Fonts
- **Custom Panels**: Special containers like hero sections, feature panels, and CTA panels
- **Background Effects**: Gradient backgrounds and pattern backgrounds

### 3. Example Applications

- **Example UI Demo**: Demonstrates all UI components (`example_ui.py`)
- **Theme Demo**: Showcases the theming capabilities (`theme_demo.py`)

## Getting Started

### Installation

1. Copy the `.py` files to your Streamlit project
2. Import the components as needed

### Basic Usage

```python
import streamlit as st
from ui_components import DataVizUI, ModernForm
from custom_theme import ModernTheme, CustomPanels

# Initialize the UI components
st.set_page_config(page_title="Modern UI Demo", layout="wide")
DataVizUI.load_css()
ModernForm.load_css()

# Apply a theme
ModernTheme.apply_theme("colorful")

# Create UI components
st.title("Modern UI Components")

# Create a card component
DataVizUI.card(
    title="Example Card",
    content="This is a simple card component with a title and content."
)

# Create a stat card
DataVizUI.stat_card(
    value="1,234",
    label="Total Users"
)

# Create a KPI card with trend indicator
DataVizUI.kpi_card(
    value="$5,678",
    label="Revenue",
    delta=12.5,
    target=6000,
    icon="💰"
)

# Add a hero section
CustomPanels.hero_section(
    title="Welcome to My App",
    subtitle="A modern Streamlit application with custom UI components",
    cta_text="Get Started"
)
```

## Component Showcase

See the `example_ui.py` and `theme_demo.py` files for comprehensive demonstrations of all available components.

Run these demos to explore all the components and their variants:

```bash
streamlit run example_ui.py
streamlit run theme_demo.py
```

## Customization

### Customizing Themes

```python
from custom_theme import ModernTheme

# Apply custom theme
ModernTheme.set_theme(
    primaryColor="#4361EE",      # Primary color for buttons, links, etc.
    backgroundColor="#FFFFFF",   # Background color
    secondaryBackgroundColor="#F8F9FA",  # Secondary background
    textColor="#262730",         # Text color
    font="Inter"                 # Font family
)
```

### Custom Background Effects

```python
from custom_theme import BackgroundEffects

# Apply gradient background
BackgroundEffects.gradient_background(
    colors=["#4361EE", "#3A0CA3"],
    direction="to right"
)

# Apply pattern background
BackgroundEffects.pattern_background(pattern_type="circuit")
```

## Technical Details

- Built purely with Streamlit and standard Python libraries
- No external JavaScript dependencies
- Compatible with Streamlit v1.0+
- Uses Google Fonts for typography
- Uses Plotly for data visualization examples

## License

MIT License