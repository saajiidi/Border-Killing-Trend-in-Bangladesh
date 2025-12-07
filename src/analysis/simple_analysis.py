#!/usr/bin/env python3
"""
Simple Border Killings Analysis - Basic version without heavy dependencies
"""

import sys
import os
from pathlib import Path

# Add basic data processing without pandas initially
def load_excel_basic(file_path):
    """Basic Excel loading fallback"""
    try:
        import pandas as pd
        return pd.read_excel(file_path)
    except ImportError:
        print("Pandas not available. Please install dependencies first.")
        return None

def main():
    """Main analysis function"""
    print("=" * 60)
    print("BORDER KILLINGS ANALYSIS")
    print("=" * 60)
    
    # Get data path
    data_path = Path(__file__).parent.parent.parent / "data" / "border-inc.xlsx"
    
    if not data_path.exists():
        print(f"Error: Data file not found at {data_path}")
        return
    
    print(f"Data file found: {data_path}")
    
    # Try to load data
    data = load_excel_basic(data_path)
    
    if data is not None:
        print(f"Data loaded successfully!")
        print(f"Shape: {data.shape}")
        print(f"Columns: {list(data.columns)}")
        
        # Basic statistics
        if 'Killed' in data.columns:
            total_killed = data['Killed'].sum()
            avg_killed = data['Killed'].mean()
            print(f"\nBasic Statistics:")
            print(f"Total killings: {total_killed}")
            print(f"Average per year: {avg_killed:.2f}")
            
        if 'Years' in data.columns:
            year_range = f"{data['Years'].min()} - {data['Years'].max()}"
            print(f"Year range: {year_range}")
    else:
        print("Could not load data. Please ensure dependencies are installed.")
        print("Run: .venv/bin/pip install pandas openpyxl")

if __name__ == "__main__":
    main()
