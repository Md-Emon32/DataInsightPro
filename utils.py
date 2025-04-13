import streamlit as st
import pandas as pd
import numpy as np
import os
from typing import Dict, List, Any, Optional, Tuple

def get_file_extension(filename: str) -> str:
    """
    Get the file extension from a filename.
    
    Args:
        filename: Input filename
        
    Returns:
        File extension without the dot
    """
    return filename.split('.')[-1].lower() if '.' in filename else ''

def show_error(message: str) -> None:
    """
    Display an error message.
    
    Args:
        message: Error message to display
    """
    st.error(message)

def show_success(message: str) -> None:
    """
    Display a success message.
    
    Args:
        message: Success message to display
    """
    st.success(message)

def show_info(message: str) -> None:
    """
    Display an info message.
    
    Args:
        message: Info message to display
    """
    st.info(message)

def show_warning(message: str) -> None:
    """
    Display a warning message.
    
    Args:
        message: Warning message to display
    """
    st.warning(message)

def format_number(number: float, decimals: int = 2) -> str:
    """
    Format a number for display.
    
    Args:
        number: Number to format
        decimals: Number of decimal places
        
    Returns:
        Formatted number as a string
    """
    if number is None:
        return "N/A"
    
    if pd.isna(number):
        return "N/A"
    
    if abs(number) >= 1_000_000:
        return f"{number/1_000_000:.{decimals}f}M"
    elif abs(number) >= 1_000:
        return f"{number/1_000:.{decimals}f}K"
    elif abs(number) < 0.01 and number != 0:
        return f"{number:.{decimals}e}"
    else:
        return f"{number:.{decimals}f}"

def get_column_dtype_info(data: pd.DataFrame) -> Dict[str, List[str]]:
    """
    Categorize columns by data type.
    
    Args:
        data: Input DataFrame
        
    Returns:
        Dictionary mapping data type categories to column names
    """
    dtype_info = {
        'numeric': [],
        'categorical': [],
        'datetime': [],
        'boolean': [],
        'other': []
    }
    
    for col in data.columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            if set(data[col].dropna().unique()).issubset({0, 1, True, False}):
                dtype_info['boolean'].append(col)
            else:
                dtype_info['numeric'].append(col)
        elif pd.api.types.is_datetime64_dtype(data[col]):
            dtype_info['datetime'].append(col)
        elif pd.api.types.is_object_dtype(data[col]):
            if data[col].nunique() < min(20, len(data) * 0.1):
                dtype_info['categorical'].append(col)
            else:
                dtype_info['other'].append(col)
        else:
            dtype_info['other'].append(col)
    
    return dtype_info

def detect_outliers_iqr(data: pd.Series) -> Tuple[pd.Series, float, float]:
    """
    Detect outliers using the IQR method.
    
    Args:
        data: Numeric pandas Series
        
    Returns:
        Tuple containing:
        - Boolean Series indicating outliers
        - Lower bound
        - Upper bound
    """
    if not pd.api.types.is_numeric_dtype(data):
        return pd.Series([False] * len(data)), None, None
    
    # Calculate Q1, Q3, and IQR
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    
    # Calculate bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Identify outliers
    outliers = (data < lower_bound) | (data > upper_bound)
    
    return outliers, lower_bound, upper_bound

def ensure_openai_api_key() -> bool:
    """
    Check if the OpenAI API key is available.
    
    Returns:
        True if the API key is set, False otherwise
    """
    api_key = os.environ.get("OPENAI_API_KEY", "")
    
    if not api_key:
        show_warning(
            "The OpenAI API key is not set. Chatbot functionality will be limited. "
            "Please set the OPENAI_API_KEY environment variable."
        )
        return False
    
    return True

def truncate_string(text: str, max_length: int = 50) -> str:
    """
    Truncate a string to a maximum length.
    
    Args:
        text: Input string
        max_length: Maximum length
        
    Returns:
        Truncated string
    """
    if not isinstance(text, str):
        return str(text)
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length-3] + "..."
