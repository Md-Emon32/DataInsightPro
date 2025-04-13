import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional
import scipy.stats as stats
from data_processor import identify_correlated_columns, detect_outliers
import os
import json
import streamlit as st

def generate_automated_insights(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate automated insights from the data.
    
    Args:
        data: Input DataFrame
        
    Returns:
        Dictionary containing various insights
    """
    insights = {
        'general_insights': [],
        'column_insights': {},
        'correlation_insights': []
    }
    
    # General dataset insights
    insights['general_insights'].extend(_generate_general_insights(data))
    
    # Column-specific insights
    for column in data.columns:
        col_insights = _generate_column_insights(data, column)
        if col_insights:
            insights['column_insights'][column] = col_insights
    
    # Correlation insights
    insights['correlation_insights'] = _generate_correlation_insights(data)
    
    return insights

def _generate_general_insights(data: pd.DataFrame) -> List[str]:
    """Generate general insights about the dataset."""
    insights = []
    
    # Dataset size
    insights.append(f"The dataset contains {data.shape[0]:,} rows and {data.shape[1]} columns.")
    
    # Missing values
    missing_count = data.isna().sum().sum()
    if missing_count > 0:
        missing_pct = (missing_count / (data.shape[0] * data.shape[1])) * 100
        insights.append(f"The dataset contains {missing_count:,} missing values ({missing_pct:.2f}% of all data points).")
        
        # Columns with most missing values
        missing_by_col = data.isna().sum()
        high_missing_cols = missing_by_col[missing_by_col > 0].sort_values(ascending=False)
        if not high_missing_cols.empty:
            top_missing_cols = high_missing_cols.head(3)
            cols_str = ", ".join([f"{col} ({val:,} missing, {(val/data.shape[0])*100:.1f}%)" 
                                for col, val in top_missing_cols.items()])
            insights.append(f"Top columns with missing values: {cols_str}.")
    else:
        insights.append("The dataset is complete with no missing values.")
    
    # Numeric vs categorical columns
    num_cols = data.select_dtypes(include=['number']).columns
    cat_cols = data.select_dtypes(include=['object']).columns
    date_cols = data.select_dtypes(include=['datetime']).columns
    
    insights.append(f"The dataset has {len(num_cols)} numeric columns, {len(cat_cols)} categorical columns, and {len(date_cols)} date columns.")
    
    # Potential ID columns
    potential_id_cols = []
    for col in data.columns:
        if data[col].nunique() == data.shape[0]:
            potential_id_cols.append(col)
    
    if potential_id_cols:
        if len(potential_id_cols) == 1:
            insights.append(f"'{potential_id_cols[0]}' appears to be a unique identifier column.")
        else:
            insights.append(f"Potential identifier columns: {', '.join(potential_id_cols[:3])}.")
    
    # Duplicated rows
    dup_count = data.duplicated().sum()
    if dup_count > 0:
        insights.append(f"Found {dup_count:,} duplicate rows ({(dup_count/data.shape[0])*100:.1f}% of the dataset).")
    else:
        insights.append("No duplicate rows found in the dataset.")
    
    return insights

def _generate_column_insights(data: pd.DataFrame, column: str) -> List[str]:
    """Generate insights for a specific column."""
    insights = []
    
    # Skip columns with too many unique values (likely IDs)
    if data[column].nunique() == data.shape[0] and data.shape[0] > 100:
        insights.append(f"This column has unique values for every row and might be an identifier column.")
        return insights
    
    # Handle different column types
    dtype = data[column].dtype
    
    # Numeric columns
    if pd.api.types.is_numeric_dtype(dtype):
        insights.extend(_analyze_numeric_column(data, column))
    
    # Categorical/text columns
    elif pd.api.types.is_object_dtype(dtype):
        insights.extend(_analyze_categorical_column(data, column))
    
    # Date columns
    elif pd.api.types.is_datetime64_dtype(dtype):
        insights.extend(_analyze_datetime_column(data, column))
    
    return insights

def _analyze_numeric_column(data: pd.DataFrame, column: str) -> List[str]:
    """Analyze a numeric column and generate insights."""
    insights = []
    
    # Basic stats
    col_data = data[column].dropna()
    
    if col_data.empty:
        insights.append("This column has no valid numeric data (all values are missing).")
        return insights
    
    # Calculate statistics
    mean_val = col_data.mean()
    median_val = col_data.median()
    min_val = col_data.min()
    max_val = col_data.max()
    
    # Format numbers properly
    if abs(mean_val) < 0.01 or abs(mean_val) > 1000:
        mean_str = f"{mean_val:.2e}"
    else:
        mean_str = f"{mean_val:.2f}"
    
    insights.append(f"Average value is {mean_str}, with range from {min_val:,} to {max_val:,}.")
    
    # Skewness
    skewness = col_data.skew()
    if abs(skewness) > 1:
        skew_direction = "positively" if skewness > 0 else "negatively"
        insights.append(f"The distribution is strongly {skew_direction} skewed (skewness = {skewness:.2f}).")
    elif abs(skewness) > 0.5:
        skew_direction = "positively" if skewness > 0 else "negatively"
        insights.append(f"The distribution is moderately {skew_direction} skewed (skewness = {skewness:.2f}).")
    
    # Mean vs Median
    mean_median_diff_pct = abs(mean_val - median_val) / max(abs(median_val), 1e-10) * 100
    if mean_median_diff_pct > 20:
        insights.append(f"The mean ({mean_str}) is significantly different from the median ({median_val:,}), suggesting potential outliers or a skewed distribution.")
    
    # Detect outliers
    outliers, outlier_pct = detect_outliers(data, column)
    if outlier_pct > 0:
        insights.append(f"Found {len(outliers):,} outliers ({outlier_pct:.1f}% of values) based on the IQR method.")
    
    # Zero values
    zero_count = (col_data == 0).sum()
    if zero_count > 0:
        zero_pct = (zero_count / len(col_data)) * 100
        if zero_pct > 25:
            insights.append(f"High number of zero values: {zero_count:,} ({zero_pct:.1f}% of the data).")
    
    # Missing values
    missing_count = data[column].isna().sum()
    if missing_count > 0:
        missing_pct = (missing_count / len(data)) * 100
        insights.append(f"Contains {missing_count:,} missing values ({missing_pct:.1f}% of the data).")
    
    return insights

def _analyze_categorical_column(data: pd.DataFrame, column: str) -> List[str]:
    """Analyze a categorical/text column and generate insights."""
    insights = []
    
    # Unique values
    unique_count = data[column].nunique()
    total_count = len(data[column].dropna())
    
    if total_count == 0:
        insights.append("This column has no valid data (all values are missing).")
        return insights
    
    # Missing values
    missing_count = data[column].isna().sum()
    if missing_count > 0:
        missing_pct = (missing_count / len(data)) * 100
        insights.append(f"Contains {missing_count:,} missing values ({missing_pct:.1f}% of the data).")
    
    # Unique value analysis
    if unique_count == 1:
        only_value = data[column].dropna().iloc[0]
        insights.append(f"This column contains only one value: '{only_value}'.")
    else:
        insights.append(f"Contains {unique_count:,} unique values.")
        
        # Get value frequency
        value_counts = data[column].value_counts()
        top_values = value_counts.head(3)
        
        # Format the output for top values
        top_values_str = ", ".join([f"'{val}' ({count:,}, {(count/total_count)*100:.1f}%)" 
                                  for val, count in top_values.items()])
        
        insights.append(f"Most common values: {top_values_str}.")
        
        # Low cardinality check
        if 1 < unique_count <= 10:
            insights.append(f"This is a low-cardinality categorical column with {unique_count} categories.")
        
        # High cardinality check
        elif unique_count > 100:
            unique_ratio = unique_count / total_count
            if unique_ratio > 0.9:
                insights.append(f"This column has very high cardinality with {unique_count:,} unique values, suggesting it might be an ID or free-text field.")
    
    return insights

def _analyze_datetime_column(data: pd.DataFrame, column: str) -> List[str]:
    """Analyze a datetime column and generate insights."""
    insights = []
    
    # Filter out NaT values
    date_data = data[column].dropna()
    
    if date_data.empty:
        insights.append("This column has no valid date data (all values are missing or invalid).")
        return insights
    
    # Date range
    min_date = date_data.min()
    max_date = date_data.max()
    date_range = max_date - min_date
    
    insights.append(f"Date range from {min_date.date()} to {max_date.date()} (spanning {date_range.days} days).")
    
    # Check for gaps
    if len(date_data) > 1 and date_range.days > 0:
        unique_dates = date_data.dt.date.nunique()
        coverage = unique_dates / date_range.days
        
        if coverage < 0.1:
            insights.append(f"Sparse date coverage: only {unique_dates:,} unique dates out of {date_range.days:,} days in the range.")
        elif coverage > 0.9:
            insights.append(f"Dense date coverage: {unique_dates:,} unique dates out of {date_range.days:,} days in the range.")
    
    # Look for patterns in the data
    if len(date_data) >= 10:
        # Check for weekday patterns
        weekday_counts = date_data.dt.dayofweek.value_counts().sort_index()
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_counts.index = [weekday_names[i] for i in weekday_counts.index]
        
        # Find the most and least common days
        most_common_day = weekday_counts.idxmax()
        least_common_day = weekday_counts.idxmin()
        
        # Only report if there's a significant difference
        max_count = weekday_counts.max()
        min_count = weekday_counts.min()
        if max_count > 2 * min_count:
            insights.append(f"Date pattern detected: {most_common_day} is the most common day, while {least_common_day} is the least common.")
    
    # Missing values
    missing_count = data[column].isna().sum()
    if missing_count > 0:
        missing_pct = (missing_count / len(data)) * 100
        insights.append(f"Contains {missing_count:,} missing or invalid dates ({missing_pct:.1f}% of the data).")
    
    return insights

def _generate_correlation_insights(data: pd.DataFrame) -> List[str]:
    """Generate insights about correlations between columns."""
    insights = []
    
    # Only analyze numeric columns
    numeric_data = data.select_dtypes(include=['number'])
    
    if numeric_data.shape[1] <= 1:
        return insights
    
    # Find highly correlated pairs
    correlated_pairs = identify_correlated_columns(data, threshold=0.7)
    
    if correlated_pairs:
        # Sort by correlation strength
        correlated_pairs.sort(key=lambda x: x[2], reverse=True)
        
        # Top correlations
        top_correlations = correlated_pairs[:5]  # Limit to top 5
        
        for col1, col2, corr_val in top_correlations:
            corr_strength = "strong positive" if corr_val > 0.8 else "moderate positive"
            insights.append(f"Found {corr_strength} correlation ({corr_val:.2f}) between '{col1}' and '{col2}'.")
    else:
        insights.append("No strong correlations found between numeric columns.")
    
    return insights

def extract_key_metrics(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Extract key metrics that can be displayed on a dashboard.
    
    Args:
        data: Input DataFrame
        
    Returns:
        Dictionary of key metrics
    """
    metrics = {}
    
    # Basic data metrics
    metrics['row_count'] = len(data)
    metrics['column_count'] = len(data.columns)
    
    # Missing data percentage
    total_cells = data.size
    total_missing = data.isna().sum().sum()
    metrics['missing_percentage'] = (total_missing / total_cells) * 100 if total_cells > 0 else 0
    
    # Summary stats for numeric columns
    numeric_data = data.select_dtypes(include=['number'])
    
    if not numeric_data.empty:
        # Calculate averages and standard deviations for each column
        metrics['column_stats'] = {}
        
        for col in numeric_data.columns:
            col_data = numeric_data[col].dropna()
            
            if not col_data.empty:
                metrics['column_stats'][col] = {
                    'mean': col_data.mean(),
                    'median': col_data.median(),
                    'std': col_data.std(),
                    'min': col_data.min(),
                    'max': col_data.max()
                }
    
    # Top categories for categorical data
    categorical_data = data.select_dtypes(include=['object'])
    
    if not categorical_data.empty:
        metrics['categorical_stats'] = {}
        
        for col in categorical_data.columns:
            # Skip columns with high cardinality
            if categorical_data[col].nunique() <= 10:
                value_counts = categorical_data[col].value_counts().head(5).to_dict()
                metrics['categorical_stats'][col] = value_counts
    
    return metrics
