#!/usr/bin/env python3
"""
Generate model comparison data for visualization
Extracts model performance metrics and creates JSON data for charts
"""

import json
from pathlib import Path

# Model performance data from the notebook analysis
model_performance = {
    'Naive': {'MAE': 5.50, 'MSE': 50.50, 'RMSE': 7.11, 'MAPE': 20.63, 'R²': -1.02},
    'ARIMA': {'MAE': 12.90, 'MSE': 179.70, 'RMSE': 13.41, 'MAPE': 68.25, 'R²': -6.29},
    'Moving Avg': {'MAE': 13.33, 'MSE': 202.44, 'RMSE': 14.23, 'MAPE': 71.77, 'R²': -7.21},
    'Average': {'MAE': 16.96, 'MSE': 312.28, 'RMSE': 17.67, 'MAPE': 89.91, 'R²': -11.66},
    'ARIMA_alt': {'MAE': 17.38, 'MSE': 323.20, 'RMSE': 17.98, 'MAPE': 91.48, 'R²': -12.10},
    'Auto-ARIMA': {'MAE': 19.05, 'MSE': 396.30, 'RMSE': 19.91, 'MAPE': 101.15, 'R²': -15.07},
    'SES': {'MAE': 21.76, 'MSE': 498.03, 'RMSE': 22.32, 'MAPE': 113.92, 'R²': -19.19},
    'Holt': {'MAE': 23.23, 'MSE': 560.33, 'RMSE': 23.67, 'MAPE': 120.85, 'R²': -21.72},
    'Holt-Winters': {'MAE': 19.83, 'MSE': 583.49, 'RMSE': 24.16, 'MAPE': 113.30, 'R²': -22.65},
    'SARIMA': {'MAE': 25.84, 'MSE': 710.57, 'RMSE': 26.66, 'MAPE': 135.63, 'R²': -27.81},
    'LSTM': {'MAE': 27.26, 'MSE': 766.64, 'RMSE': 27.69, 'MAPE': 141.33, 'R²': -30.08},
    'Exponential Trend': {'MAE': 38.71, 'MSE': 1512.86, 'RMSE': 38.90, 'MAPE': 197.49, 'R²': -60.33},
    'Linear Trend': {'MAE': 42.75, 'MSE': 1845.58, 'RMSE': 42.96, 'MAPE': 218.18, 'R²': -73.82}
}

# Categorize models
arima_models = ['ARIMA', 'ARIMA_alt', 'Auto-ARIMA', 'SARIMA']
other_models = [m for m in model_performance.keys() if m not in arima_models]

def generate_chart_data():
    """Generate data for Chart.js visualizations"""
    
    # Sort models by RMSE for better visualization
    sorted_models = sorted(model_performance.items(), key=lambda x: x[1]['RMSE'])
    model_names = [m[0] for m in sorted_models]
    
    # Prepare data for different chart types
    chart_data = {
        'rmse_comparison': {
            'labels': model_names,
            'data': [model_performance[m]['RMSE'] for m in model_names],
            'colors': ['#667eea' if m in arima_models else '#764ba2' for m in model_names]
        },
        'mae_comparison': {
            'labels': model_names,
            'data': [model_performance[m]['MAE'] for m in model_names],
            'colors': ['#667eea' if m in arima_models else '#764ba2' for m in model_names]
        },
        'arima_vs_others': {
            'arima_models': {
                'labels': arima_models,
                'rmse': [model_performance[m]['RMSE'] for m in arima_models],
                'mae': [model_performance[m]['MAE'] for m in arima_models]
            },
            'top_others': {
                'labels': ['Naive', 'Moving Avg', 'Average', 'SES', 'Holt', 'LSTM'],
                'rmse': [model_performance[m]['RMSE'] for m in ['Naive', 'Moving Avg', 'Average', 'SES', 'Holt', 'LSTM']],
                'mae': [model_performance[m]['MAE'] for m in ['Naive', 'Moving Avg', 'Average', 'SES', 'Holt', 'LSTM']]
            }
        },
        'performance_metrics': {
            'top_5_models': {
                'labels': model_names[:5],
                'rmse': [model_performance[m]['RMSE'] for m in model_names[:5]],
                'mae': [model_performance[m]['MAE'] for m in model_names[:5]],
                'mape': [model_performance[m]['MAPE'] for m in model_names[:5]]
            }
        },
        'full_data': model_performance
    }
    
    return chart_data

def save_data():
    """Save chart data to JSON file"""
    chart_data = generate_chart_data()
    output_path = Path(__file__).parent / 'model_comparison_data.json'
    
    with open(output_path, 'w') as f:
        json.dump(chart_data, f, indent=2)
    
    print(f"Model comparison data saved to {output_path}")
    return chart_data

if __name__ == "__main__":
    data = save_data()
    print("\nModel Performance Summary:")
    print("=" * 60)
    df = pd.DataFrame(model_performance).T
    df = df.sort_values('RMSE')
    print(df.to_string())
    print("\nTop 5 Models by RMSE:")
    print(df.head(5)[['RMSE', 'MAE', 'MAPE']].to_string())

