import matplotlib.pyplot as plt
import pandas as pd

# Data for total annual shootings
data_total = {
    'Year': [2006, 2007, 2008, 2009, 2010],
    'Total Shootings': [37, 30, 4, 5, 4]
}

# Create DataFrame
df_total = pd.DataFrame(data_total)

# Sort by total shootings in descending order
df_total = df_total.sort_values(by='Total Shootings', ascending=False)

# Calculate cumulative percentage
df_total['Cumulative Percentage'] = df_total['Total Shootings'].cumsum() / df_total['Total Shootings'].sum() * 100

# Plot Pareto chart
fig, ax1 = plt.subplots()

# Bar plot for total shootings
ax1.bar(df_total['Year'], df_total['Total Shootings'], color='blue', alpha=0.7, label='Total Shootings')
ax1.set_xlabel('Year')
ax1.set_ylabel('Total Shootings', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Line plot for cumulative percentage
ax2 = ax1.twinx()
ax2.plot(df_total['Year'], df_total['Cumulative Percentage'], color='red', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add title and legend
plt.title('Pareto Chart: Total Annual Shootings')
fig.legend(loc='upper right')

# Show plot
plt.show()