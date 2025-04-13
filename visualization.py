import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Any, Tuple, Optional
import numpy as np

def create_trend_chart(data: pd.DataFrame, x_column: str, y_column: str) -> go.Figure:
    """
    Create a trend chart for the given columns.
    
    Args:
        data: Input DataFrame
        x_column: Column to use for the x-axis (categorical or date)
        y_column: Column to use for the y-axis (numeric)
        
    Returns:
        Plotly figure object
    """
    # Check if x_column might be a date
    if data[x_column].dtype == 'datetime64[ns]':
        # For datetime x-axis, create a line chart
        fig = px.line(
            data, 
            x=x_column, 
            y=y_column,
            title=f"Trend of {y_column} over {x_column}"
        )
    else:
        # For categorical x-axis, calculate aggregated y values
        agg_data = data.groupby(x_column)[y_column].agg(['mean', 'count']).reset_index()
        agg_data.columns = [x_column, 'mean', 'count']
        
        # Sort by mean value for better visualization
        agg_data = agg_data.sort_values('mean', ascending=False)
        
        # Create bar chart
        fig = px.bar(
            agg_data, 
            x=x_column, 
            y='mean',
            title=f"Average {y_column} by {x_column}",
            color='count',
            color_continuous_scale='Viridis',
            labels={'mean': f'Average {y_column}', 'count': 'Count'}
        )
        
        # Add count information on hover
        fig.update_traces(
            hovertemplate=f"{x_column}: %{{x}}<br>Average {y_column}: %{{y:.2f}}<br>Count: %{{marker.color}}<extra></extra>"
        )
    
    fig.update_layout(
        xaxis_title=x_column,
        yaxis_title=y_column,
        plot_bgcolor='white',
        hovermode='closest'
    )
    
    return fig

def create_correlation_heatmap(data: pd.DataFrame, columns: List[str] = None) -> go.Figure:
    """
    Create a correlation heatmap for numerical columns.
    
    Args:
        data: Input DataFrame
        columns: List of columns to include (defaults to all numeric columns)
        
    Returns:
        Plotly figure object
    """
    # Select numeric columns if not specified
    if columns is None:
        numeric_data = data.select_dtypes(include=['number'])
    else:
        numeric_data = data[columns].select_dtypes(include=['number'])
    
    # Compute correlation matrix
    corr_matrix = numeric_data.corr(numeric_only=True)
    
    # Create heatmap
    fig = px.imshow(
        corr_matrix,
        text_auto='.2f',
        aspect='auto',
        color_continuous_scale='RdBu_r',
        title='Correlation Heatmap'
    )
    
    fig.update_layout(
        plot_bgcolor='white',
        width=700,
        height=700
    )
    
    return fig

def create_distribution_plot(data: pd.DataFrame, column: str) -> go.Figure:
    """
    Create a distribution plot for a numeric column.
    
    Args:
        data: Input DataFrame
        column: The column to visualize
        
    Returns:
        Plotly figure object
    """
    if column not in data.columns or data[column].dtype not in ['int64', 'float64']:
        fig = go.Figure()
        fig.add_annotation(
            text="Selected column is not numeric",
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=16)
        )
        return fig
    
    # Filter out nulls and infinite values
    col_data = data[column].replace([np.inf, -np.inf], np.nan).dropna()
    
    if col_data.empty:
        fig = go.Figure()
        fig.add_annotation(
            text="No valid data points to display",
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=16)
        )
        return fig
    
    # Create a subplot with two y-axes
    fig = px.histogram(
        col_data, 
        x=column,
        histnorm='probability density',
        title=f'Distribution of {column}',
        color_discrete_sequence=['rgba(0, 123, 255, 0.5)'],
        marginal='box',
    )
    
    # Calculate basic statistics for annotations
    mean_val = col_data.mean()
    median_val = col_data.median()
    std_val = col_data.std()
    
    # Add vertical lines for mean and median
    fig.add_vline(
        x=mean_val, 
        line_dash="dash", 
        line_color="red", 
        annotation_text=f"Mean: {mean_val:.2f}",
        annotation_position="top right"
    )
    
    fig.add_vline(
        x=median_val, 
        line_dash="dash", 
        line_color="green", 
        annotation_text=f"Median: {median_val:.2f}",
        annotation_position="top left"
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title=column,
        yaxis_title='Density',
        plot_bgcolor='white',
        bargap=0.1,
        showlegend=False
    )
    
    return fig

def create_scatter_plot(data: pd.DataFrame, x_column: str, y_column: str, color_column: Optional[str] = None) -> go.Figure:
    """
    Create a scatter plot for two numeric columns.
    
    Args:
        data: Input DataFrame
        x_column: Column for x-axis
        y_column: Column for y-axis
        color_column: Optional column for color encoding
        
    Returns:
        Plotly figure object
    """
    # Create the scatter plot
    fig = px.scatter(
        data,
        x=x_column,
        y=y_column,
        color=color_column,
        title=f"{y_column} vs {x_column}",
        opacity=0.7,
        size_max=10
    )
    
    # Add trendline if no color column is specified
    if color_column is None:
        fig.update_layout(
            shapes=[
                dict(
                    type='line',
                    xref='x', yref='y',
                    x0=data[x_column].min(), y0=data[y_column].min(),
                    x1=data[x_column].max(), y1=data[y_column].max(),
                    line=dict(color='red', dash='dash')
                )
            ]
        )
    
    # Update layout
    fig.update_layout(
        plot_bgcolor='white',
        xaxis_title=x_column,
        yaxis_title=y_column,
        hovermode='closest'
    )
    
    return fig

def create_bar_chart(data: pd.DataFrame, x_column: str, y_column: Optional[str] = None) -> go.Figure:
    """
    Create a bar chart for a categorical column.
    
    Args:
        data: Input DataFrame
        x_column: Categorical column
        y_column: Optional numeric column for y-axis (defaults to count)
        
    Returns:
        Plotly figure object
    """
    if y_column is None:
        # Count-based bar chart
        count_data = data[x_column].value_counts().reset_index()
        count_data.columns = [x_column, 'count']
        
        # Only take top 20 categories for readability
        if len(count_data) > 20:
            count_data = count_data.head(20)
            title = f"Top 20 categories in {x_column} by count"
        else:
            title = f"Categories in {x_column} by count"
        
        fig = px.bar(
            count_data,
            x=x_column,
            y='count',
            title=title,
            color='count',
            color_continuous_scale='Viridis'
        )
    else:
        # Group by categorical column and calculate mean of numeric column
        agg_data = data.groupby(x_column)[y_column].mean().reset_index()
        
        # Only take top 20 categories for readability
        if len(agg_data) > 20:
            agg_data = agg_data.sort_values(y_column, ascending=False).head(20)
            title = f"Top 20 {x_column} by average {y_column}"
        else:
            title = f"{x_column} by average {y_column}"
        
        fig = px.bar(
            agg_data,
            x=x_column,
            y=y_column,
            title=title,
            color=y_column,
            color_continuous_scale='Viridis'
        )
    
    # Update layout
    fig.update_layout(
        plot_bgcolor='white',
        xaxis_title=x_column,
        hovermode='closest'
    )
    
    return fig

def create_box_plot(data: pd.DataFrame, x_column: str, y_column: str) -> go.Figure:
    """
    Create a box plot for a numeric column grouped by a categorical column.
    
    Args:
        data: Input DataFrame
        x_column: Categorical column
        y_column: Numeric column
        
    Returns:
        Plotly figure object
    """
    # Calculate category counts for hover info
    category_counts = data[x_column].value_counts().to_dict()
    
    # Create box plot
    fig = px.box(
        data,
        x=x_column,
        y=y_column,
        title=f"Distribution of {y_column} by {x_column}",
        points="outliers"
    )
    
    # Add category counts as annotations
    annotations = []
    for i, category in enumerate(fig.data[0].x):
        if category in category_counts:
            annotations.append(
                dict(
                    x=i,
                    y=data[y_column].max(),
                    text=f"n={category_counts[category]}",
                    showarrow=False,
                    yshift=10
                )
            )
    
    fig.update_layout(annotations=annotations)
    
    # Update layout
    fig.update_layout(
        plot_bgcolor='white',
        xaxis_title=x_column,
        yaxis_title=y_column,
        hovermode='closest'
    )
    
    return fig
