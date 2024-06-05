import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'C:/Users/user/Desktop/Data Analysis/border-inc.xlsx'
data = pd.read_excel(file_path)

# Drop columns with all NaN values
data_cleaned = data.dropna(axis=1, how='all')

# Create a summary of the number of killings under each ruling party in India
killed_by_party_india = data_cleaned.groupby('Rulling_Party_India')['Killed'].sum().reset_index()

# Sort the data for better visualization
killed_by_party_india = killed_by_party_india.sort_values(by='Killed', ascending=False)

# Plotting the data
plt.figure(figsize=(12, 8))
sns.barplot(data=killed_by_party_india, x='Rulling_Party_India', y='Killed', palette='viridis')
plt.title('Total Number of Killings by Ruling Party in India')
plt.xlabel('Ruling Party in India')
plt.ylabel('Total Killings')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
