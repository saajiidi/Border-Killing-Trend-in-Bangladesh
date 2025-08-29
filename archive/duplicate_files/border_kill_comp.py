import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'C:/Users/user/Desktop/Data Analysis/border-inc.xlsx'
data = pd.read_excel(file_path)

# Drop columns with all NaN values
data_cleaned = data.dropna(axis=1, how='all')

# Create summaries of the number of killings under each ruling party in Bangladesh and India
killed_by_party_bd = data_cleaned.groupby('Rulling_Party')['Killed'].sum().reset_index().rename(columns={'Rulling_Party': 'Party', 'Killed': 'Killed_BD'})
killed_by_party_india = data_cleaned.groupby('Rulling_Party_India')['Killed'].sum().reset_index().rename(columns={'Rulling_Party_India': 'Party', 'Killed': 'Killed_India'})

# Merging the two summaries for comparison
comparison_df = pd.merge(killed_by_party_bd, killed_by_party_india, on='Party', how='outer').fillna(0)

# Plotting the comparison
plt.figure(figsize=(14, 8))
sns.barplot(data=comparison_df, x='Party', y='Killed_BD', color='blue', label='Bangladesh')
sns.barplot(data=comparison_df, x='Party', y='Killed_India', color='red', label='India', alpha=0.6)
plt.title('Comparison of Total Killings by Ruling Parties in Bangladesh and India')
plt.xlabel('Ruling Party')
plt.ylabel('Total Killings')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()

# Display the merged dataframe for clarity
print(comparison_df)
