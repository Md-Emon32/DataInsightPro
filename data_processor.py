import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional, Tuple
import streamlit as st

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Process and clean the uploaded data.
    
    Args:
        data: The input DataFrame
        
    Returns:
        Processed DataFrame
    """
    # Make a copy to avoid modifying the original data
    df = data.copy()
    
    # Basic cleaning operations
    
    # 1. Handle common date formats
    for col in df.columns:
        # Try to convert string columns that might be dates
        if df[col].dtype == 'object':
            try:
                # Check if it has date-like patterns
                date_sample = df[col].dropna().iloc[0] if not df[col].dropna().empty else ""
                if isinstance(date_sample, str) and (
                    '/' in date_sample or 
                    '-' in date_sample or 
                    ':' in date_sample
                ):
                    df[col] = pd.to_datetime(df[col], errors='ignore')
            except:
                # If conversion fails, keep the original
                pass
    
    # 2. Fix column names (remove spaces, special characters)
    df.columns = [str(col).strip().replace(' ', '_').lower() for col in df.columns]
    
    # 3. Handle missing values for numeric columns (optional)
    numeric_cols = df.select_dtypes(include=['number']).columns
    # For this tool, we'll keep nulls as is to allow users to see them
    
    return df

def filter_data(data: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Filter the DataFrame to include only the selected columns.
    
    Args:
        data: The input DataFrame
        columns: List of column names to keep
        
    Returns:
        Filtered DataFrame
    """
    if not columns:
        return data
    
    # Ensure all specified columns exist in the dataframe
    valid_columns = [col for col in columns if col in data.columns]
    
    if not valid_columns:
        return data
    
    return data[valid_columns]

def get_basic_stats(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate basic statistics for the DataFrame.
    
    Args:
        data: The input DataFrame
        
    Returns:
        Dictionary containing basic statistics
    """
    stats = {}
    
    # Basic dataframe info
    stats['row_count'] = len(data)
    stats['column_count'] = len(data.columns)
    
    # Missing values
    missing_values = data.isna().sum().sum()
    stats['missing_values'] = missing_values
    stats['missing_percentage'] = (missing_values / (len(data) * len(data.columns))) * 100
    
    # Column types
    dtype_counts = data.dtypes.value_counts().to_dict()
    stats['column_types'] = {str(k): v for k, v in dtype_counts.items()}
    
    # Numeric column statistics
    numeric_cols = data.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        stats['numeric_columns'] = len(numeric_cols)
        stats['numeric_columns_list'] = numeric_cols.tolist()
    else:
        stats['numeric_columns'] = 0
        stats['numeric_columns_list'] = []
    
    # Categorical column statistics
    categorical_cols = data.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        stats['categorical_columns'] = len(categorical_cols)
        stats['categorical_columns_list'] = categorical_cols.tolist()
    else:
        stats['categorical_columns'] = 0
        stats['categorical_columns_list'] = []
    
    return stats

def detect_outliers(data: pd.DataFrame, column: str) -> Tuple[pd.DataFrame, float]:
    """
    Detect outliers in a numerical column using IQR method.
    
    Args:
        data: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Tuple containing DataFrame of outlier values and percentage of outliers
    """
    if column not in data.columns or data[column].dtype not in ['int64', 'float64']:
        return pd.DataFrame(), 0
    
    # Calculate IQR
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    
    # Define outlier bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Filter outliers
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    outlier_percentage = (len(outliers) / len(data)) * 100
    
    return outliers, outlier_percentage

def identify_correlated_columns(data: pd.DataFrame, threshold: float = 0.7) -> List[Tuple[str, str, float]]:
    """
    Identify highly correlated numerical columns.
    
    Args:
        data: Input DataFrame
        threshold: Correlation coefficient threshold
        
    Returns:
        List of tuples with correlated column pairs and their correlation value
    """
    numeric_data = data.select_dtypes(include=['number'])
    
    if numeric_data.shape[1] <= 1:
        return []
    
    # Calculate correlation matrix
    corr_matrix = numeric_data.corr().abs()
    
    # Get upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    
    # Find index of feature columns with correlation greater than threshold
    correlated_pairs = []
    for i, col in enumerate(upper.columns):
        for j, row in enumerate(upper.index):
            if upper.iloc[j, i] > threshold:
                correlated_pairs.append((col, row, upper.iloc[j, i]))
    
    return correlated_pairs
