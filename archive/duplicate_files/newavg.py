import pandas as pd
import matplotlib.pyplot as plt

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

# Rename 'Awami League' to 'BAL'
avg_killings_bd['Rulling_Party'] = avg_killings_bd['Rulling_Party'].replace('Awami League', 'BAL')

# Extract relevant parties for India and Bangladesh
avg_killings_india_filtered = avg_killings_india[avg_killings_india['Rulling_Party_India'].isin(['BJP', 'Congress'])]
avg_killings_bd_filtered = avg_killings_bd[avg_killings_bd['Rulling_Party'].isin(['BAL', 'BNP', 'others'])]

# Plotting the data
fig, axes = plt.subplots(2, 1, figsize=(14, 12))

# Plot for India
axes[0].bar(avg_killings_india_filtered['Rulling_Party_India'], avg_killings_india_filtered['Avg_Killings_Per_Year'], color=['orange', 'blue'])
axes[0].set_title('Average Killings per Year in India (BJP vs Congress)')
axes[0].set_xlabel('Ruling Party in India')
axes[0].set_ylabel('Average Killings per Year')

# Plot for Bangladesh
axes[1].bar(avg_killings_bd_filtered['Rulling_Party'], avg_killings_bd_filtered['Avg_Killings_Per_Year'], color=['green', 'red', 'grey'])
axes[1].set_title('Average Killings per Year in Bangladesh (BAL vs BNP vs others)')
axes[1].set_xlabel('Ruling Party in Bangladesh')
axes[1].set_ylabel('Average Killings per Year')

plt.tight_layout()
plt.show()

print("Average Killings per Year in India (BJP vs Congress):")
print(avg_killings_india_filtered)

print("\nAverage Killings per Year in Bangladesh (BAL vs BNP vs others):")
print(avg_killings_bd_filtered)
