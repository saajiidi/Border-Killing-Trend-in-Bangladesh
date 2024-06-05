import pandas as pd

# Load the Excel file
file_path = 'C:/Users/user/Desktop/Data Analysis/border-inc.xlsx'
data = pd.read_excel(file_path)

# Filter relevant columns and data
data_filtered = data[['Years', 'Killed', 'Rulling_Party', 'Rulling_Party_India']]

# Calculate total years for each ruling party in India
years_party_india = data_filtered.groupby('Rulling_Party_India')['Years'].count().reset_index().rename(columns={'Years': 'Total_Years'})
total_killings_india = data_filtered.groupby('Rulling_Party_India')['Killed'].sum().reset_index()
avg_killings_india = pd.merge(total_killings_india, years_party_india, on='Rulling_Party_India')
avg_killings_india['Avg_Killings_Per_Year'] = avg_killings_india['Killed'] / avg_killings_india['Total_Years']

# Calculate total years for each ruling party in Bangladesh
years_party_bd = data_filtered.groupby('Rulling_Party')['Years'].count().reset_index().rename(columns={'Years': 'Total_Years'})
total_killings_bd = data_filtered.groupby('Rulling_Party')['Killed'].sum().reset_index()
avg_killings_bd = pd.merge(total_killings_bd, years_party_bd, on='Rulling_Party')
avg_killings_bd['Avg_Killings_Per_Year'] = avg_killings_bd['Killed'] / avg_killings_bd['Total_Years']

# Extract relevant parties for India and Bangladesh
avg_killings_india_filtered = avg_killings_india[avg_killings_india['Rulling_Party_India'].isin(['BJP', 'Congress'])]
avg_killings_bd_filtered = avg_killings_bd[avg_killings_bd['Rulling_Party'].isin(['BAL', 'BNP', 'others'])]

# Display the results
print("Average Killings in Border per Year by India (BJP vs Congress):")
print(avg_killings_india_filtered)

print("\nAverage Bangladeshis Killings per Year(Timeline: BAL vs BNP vs others):")
print(avg_killings_bd_filtered)
