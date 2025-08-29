import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'C:/Users/user/Desktop/Data Analysis//border-inc.xlsx'
data = pd.read_excel(file_path)

# Inspect the data
print(data.head())

# Drop columns with all NaN values
data_cleaned = data.dropna(axis=1, how='all')
# Calculate total killings for each ruling party in India
total_killings_india = data_cleaned.groupby('Rulling_Party_India')['Killed'].sum().reset_index()

# Plot total killings by ruling party in India
plt.figure(figsize=(10, 6))
plt.bar(total_killings_india['Rulling_Party_India'], total_killings_india['Killed'], color='skyblue')
plt.title('Total Killings by Ruling Party in India')
plt.xlabel('Ruling Party in India')
plt.ylabel('Total Killings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Calculate total killings for each ruling party in Bangladesh
total_killings_bd = data_cleaned.groupby('Rulling_Party')['Killed'].sum().reset_index()

# Plot total killings by ruling party in Bangladesh
plt.figure(figsize=(10, 6))
plt.bar(total_killings_bd['Rulling_Party'], total_killings_bd['Killed'], color='lightgreen')
plt.title('Total Killings by Ruling Party in Bangladesh')
plt.xlabel('Ruling Party in Bangladesh')
plt.ylabel('Total Killings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Calculate average killings per year for each ruling party in India
years_party_india = data_cleaned.groupby('Rulling_Party_India')['Years'].count().reset_index().rename(columns={'Years': 'Total_Years'})
total_killings_india = data_cleaned.groupby('Rulling_Party_India')['Killed'].sum().reset_index()
avg_killings_india = pd.merge(total_killings_india, years_party_india, on='Rulling_Party_India')
avg_killings_india['Avg_Killings_Per_Year'] = avg_killings_india['Killed'] / avg_killings_india['Total_Years']

# Plot average killings per year by ruling party in India
plt.figure(figsize=(10, 6))
plt.bar(avg_killings_india['Rulling_Party_India'], avg_killings_india['Avg_Killings_Per_Year'], color='orange')
plt.title('Average Killings per Year by Ruling Party in India')
plt.xlabel('Ruling Party in India')
plt.ylabel('Average Killings per Year')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate average killings per year for each ruling party in Bangladesh
years_party_bd = data_cleaned.groupby('Rulling_Party')['Years'].count().reset_index().rename(columns={'Years': 'Total_Years'})
total_killings_bd = data_cleaned.groupby('Rulling_Party')['Killed'].sum().reset_index()
avg_killings_bd = pd.merge(total_killings_bd, years_party_bd, on='Rulling_Party')
avg_killings_bd['Avg_Killings_Per_Year'] = avg_killings_bd['Killed'] / avg_killings_bd['Total_Years']

# Rename 'Awami League' to 'BAL'
avg_killings_bd['Rulling_Party'] = avg_killings_bd['Rulling_Party'].replace('Awami League', 'BAL')

# Plot average killings per year by ruling party in Bangladesh
plt.figure(figsize=(10, 6))
plt.bar(avg_killings_bd['Rulling_Party'], avg_killings_bd['Avg_Killings_Per_Year'], color='red')
plt.title('Average Killings per Year by Ruling Party in Bangladesh')
plt.xlabel('Ruling Party in Bangladesh')
plt.ylabel('Average Killings per Year')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Calculate the trend of killings over the years
trend_over_time = data_cleaned.groupby('Years')['Killed'].sum().reset_index()

# Plot the trend over time
plt.figure(figsize=(12, 6))
plt.plot(trend_over_time['Years'], trend_over_time['Killed'], marker='o')
plt.title('Trend of Killings Over the Years')
plt.xlabel('Years')
plt.ylabel('Total Killings')
plt.grid(True)
plt.tight_layout()
plt.show()
