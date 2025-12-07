#!/usr/bin/env python3
"""
Border Killings Analysis - Comprehensive Analysis Tool
Analyzes border killing incidents between Bangladesh and India by BSF
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

class BorderKillingsAnalyzer:
    """Main class for analyzing border killing data"""
    
    def __init__(self, data_path=None):
        """Initialize the analyzer with data path"""
        if data_path is None:
            # Use relative path from project root
            self.data_path = Path(__file__).parent.parent.parent / "data" / "border-inc.xlsx"
        else:
            self.data_path = Path(data_path)
        
        self.data = None
        self.data_cleaned = None
        
        # Set up plotting style
        plt.style.use('ggplot')
        sns.set_palette("husl")
    
    def load_data(self):
        """Load and clean the data"""
        try:
            self.data = pd.read_excel(self.data_path)
            # Drop columns with all NaN values
            self.data_cleaned = self.data.dropna(axis=1, how='all')
            print(f"Data loaded successfully. Shape: {self.data_cleaned.shape}")
            print(f"Columns: {self.data_cleaned.columns.tolist()}")
            return True
        except FileNotFoundError:
            print(f"Error: Data file not found at {self.data_path}")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def get_summary_stats(self):
        """Get basic summary statistics"""
        if self.data_cleaned is None:
            print("Please load data first")
            return
        
        print("\n=== SUMMARY STATISTICS ===")
        print(f"Available columns: {list(self.data_cleaned.columns)}")
        
        # Check for common column variations
        year_col = None
        killed_col = None
        injured_col = None
        
        for col in self.data_cleaned.columns:
            if 'year' in col.lower():
                year_col = col
            elif 'killed' in col.lower():
                killed_col = col
            elif 'injured' in col.lower():
                injured_col = col
        
        if year_col and killed_col:
            print(f"Total years covered: {self.data_cleaned[year_col].min()} - {self.data_cleaned[year_col].max()}")
            print(f"Total killings: {self.data_cleaned[killed_col].sum()}")
            print(f"Average killings per year: {self.data_cleaned[killed_col].mean():.2f}")
            
            if injured_col:
                print(f"Total injured: {self.data_cleaned[injured_col].sum()}")
        else:
            print("Could not find expected columns. Please check data structure.")
        
    def analyze_by_ruling_party_india(self, save_plot=False):
        """Analyze killings by ruling party in India"""
        if self.data_cleaned is None:
            return None
            
        # Calculate total killings by ruling party in India
        killed_by_party_india = self.data_cleaned.groupby('Rulling_Party_India')['Killed'].sum().reset_index()
        killed_by_party_india = killed_by_party_india.sort_values(by='Killed', ascending=False)
        
        # Plotting
        plt.figure(figsize=(12, 8))
        bars = plt.bar(killed_by_party_india['Rulling_Party_India'], 
                      killed_by_party_india['Killed'], 
                      color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        
        plt.title('Total Border Killings by Ruling Party in India', fontsize=16, fontweight='bold')
        plt.xlabel('Ruling Party in India', fontsize=12)
        plt.ylabel('Total Killings', fontsize=12)
        plt.xticks(rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{int(height)}', ha='center', va='bottom')
        
        plt.tight_layout()
        if save_plot:
            plt.savefig('plots/killings_by_india_party.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return killed_by_party_india
    
    def analyze_by_ruling_party_bangladesh(self, save_plot=False):
        """Analyze killings by ruling party in Bangladesh"""
        if self.data_cleaned is None:
            return None
            
        # Calculate total killings by ruling party in Bangladesh
        killed_by_party_bd = self.data_cleaned.groupby('Rulling_Party')['Killed'].sum().reset_index()
        killed_by_party_bd = killed_by_party_bd.sort_values(by='Killed', ascending=False)
        
        # Plotting
        plt.figure(figsize=(12, 8))
        bars = plt.bar(killed_by_party_bd['Rulling_Party'], 
                      killed_by_party_bd['Killed'], 
                      color=['#96CEB4', '#FFEAA7', '#DDA0DD'])
        
        plt.title('Total Border Killings by Ruling Party in Bangladesh', fontsize=16, fontweight='bold')
        plt.xlabel('Ruling Party in Bangladesh', fontsize=12)
        plt.ylabel('Total Killings', fontsize=12)
        plt.xticks(rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{int(height)}', ha='center', va='bottom')
        
        plt.tight_layout()
        if save_plot:
            plt.savefig('plots/killings_by_bangladesh_party.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return killed_by_party_bd
    
    def calculate_average_killings(self):
        """Calculate average killings per year by ruling parties"""
        if self.data_cleaned is None:
            return None, None
            
        # For India
        years_party_india = self.data_cleaned.groupby('Rulling_Party_India')['Years'].count().reset_index()
        years_party_india.rename(columns={'Years': 'Total_Years'}, inplace=True)
        total_killings_india = self.data_cleaned.groupby('Rulling_Party_India')['Killed'].sum().reset_index()
        avg_killings_india = pd.merge(total_killings_india, years_party_india, on='Rulling_Party_India')
        avg_killings_india['Avg_Killings_Per_Year'] = avg_killings_india['Killed'] / avg_killings_india['Total_Years']
        
        # For Bangladesh
        years_party_bd = self.data_cleaned.groupby('Rulling_Party')['Years'].count().reset_index()
        years_party_bd.rename(columns={'Years': 'Total_Years'}, inplace=True)
        total_killings_bd = self.data_cleaned.groupby('Rulling_Party')['Killed'].sum().reset_index()
        avg_killings_bd = pd.merge(total_killings_bd, years_party_bd, on='Rulling_Party')
        avg_killings_bd['Avg_Killings_Per_Year'] = avg_killings_bd['Killed'] / avg_killings_bd['Total_Years']
        
        # Rename for consistency
        avg_killings_bd['Rulling_Party'] = avg_killings_bd['Rulling_Party'].replace('Awami League', 'BAL')
        
        return avg_killings_india, avg_killings_bd
    
    def plot_average_killings_comparison(self, save_plot=False):
        """Plot comparison of average killings between major parties"""
        avg_india, avg_bd = self.calculate_average_killings()
        
        if avg_india is None or avg_bd is None:
            return
        
        # Filter for major parties
        avg_india_filtered = avg_india[avg_india['Rulling_Party_India'].isin(['BJP', 'Congress'])]
        avg_bd_filtered = avg_bd[avg_bd['Rulling_Party'].isin(['BAL', 'BNP', 'others'])]
        
        # Create subplot
        fig, axes = plt.subplots(2, 1, figsize=(14, 12))
        
        # Plot for India
        bars1 = axes[0].bar(avg_india_filtered['Rulling_Party_India'], 
                           avg_india_filtered['Avg_Killings_Per_Year'], 
                           color=['#FF6B6B', '#4ECDC4'])
        axes[0].set_title('Average Border Killings per Year - India (BJP vs Congress)', 
                         fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Ruling Party in India')
        axes[0].set_ylabel('Average Killings per Year')
        
        # Add value labels
        for bar in bars1:
            height = bar.get_height()
            axes[0].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                        f'{height:.1f}', ha='center', va='bottom')
        
        # Plot for Bangladesh
        bars2 = axes[1].bar(avg_bd_filtered['Rulling_Party'], 
                           avg_bd_filtered['Avg_Killings_Per_Year'], 
                           color=['#96CEB4', '#FFEAA7', '#DDA0DD'])
        axes[1].set_title('Average Border Killings per Year - Bangladesh (BAL vs BNP vs Others)', 
                         fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Ruling Party in Bangladesh')
        axes[1].set_ylabel('Average Killings per Year')
        
        # Add value labels
        for bar in bars2:
            height = bar.get_height()
            axes[1].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                        f'{height:.1f}', ha='center', va='bottom')
        
        plt.tight_layout()
        if save_plot:
            plt.savefig('plots/average_killings_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print results
        print("\n=== AVERAGE KILLINGS PER YEAR ===")
        print("\nIndia (BJP vs Congress):")
        print(avg_india_filtered[['Rulling_Party_India', 'Avg_Killings_Per_Year']])
        print("\nBangladesh (BAL vs BNP vs Others):")
        print(avg_bd_filtered[['Rulling_Party', 'Avg_Killings_Per_Year']])
    
    def plot_trend_over_time(self, save_plot=False):
        """Plot trend of killings over time"""
        if self.data_cleaned is None:
            return
            
        trend_data = self.data_cleaned.groupby('Years')['Killed'].sum().reset_index()
        
        plt.figure(figsize=(15, 8))
        plt.plot(trend_data['Years'], trend_data['Killed'], 
                marker='o', linewidth=2, markersize=6, color='#E74C3C')
        
        plt.title('Border Killings Trend Over Time (1971-2023)', fontsize=16, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Total Killings', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        # Add trend line
        z = np.polyfit(trend_data['Years'], trend_data['Killed'], 1)
        p = np.poly1d(z)
        plt.plot(trend_data['Years'], p(trend_data['Years']), 
                "--", alpha=0.7, color='#3498DB', label='Trend Line')
        
        plt.legend()
        plt.tight_layout()
        if save_plot:
            plt.savefig('plots/killings_trend_over_time.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_comprehensive_report(self, save_plots=False):
        """Generate a comprehensive analysis report"""
        if not self.load_data():
            return
        
        print("=" * 60)
        print("BORDER KILLINGS COMPREHENSIVE ANALYSIS REPORT")
        print("=" * 60)
        
        # Create plots directory if saving
        if save_plots:
            os.makedirs('plots', exist_ok=True)
        
        # Basic statistics
        self.get_summary_stats()
        
        # Analysis by ruling parties
        print("\n" + "=" * 40)
        print("ANALYSIS BY RULING PARTIES")
        print("=" * 40)
        
        self.analyze_by_ruling_party_india(save_plots)
        self.analyze_by_ruling_party_bangladesh(save_plots)
        self.plot_average_killings_comparison(save_plots)
        
        # Trend analysis
        print("\n" + "=" * 40)
        print("TREND ANALYSIS")
        print("=" * 40)
        self.plot_trend_over_time(save_plots)
        
        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETE")
        print("=" * 60)

def main():
    """Main function to run the analysis"""
    import numpy as np
    
    # Initialize analyzer
    analyzer = BorderKillingsAnalyzer()
    
    # Generate comprehensive report
    analyzer.generate_comprehensive_report(save_plots=True)

if __name__ == "__main__":
    main()
