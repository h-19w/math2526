import matplotlib.pyplot as plt
import pandas as pd

# Data for shootings of gang members
data_gang = {
    'Year': [2006, 2007, 2008, 2009, 2010],
    'Shootings of Gang Members': [30, 22, 3, 4, 3]
}

# Create DataFrame
df_gang = pd.DataFrame(data_gang)

# Sort by shootings of gang members in descending order
df_gang = df_gang.sort_values(by='Shootings of Gang Members', ascending=False)

# Calculate cumulative percentage
df_gang['Cumulative Percentage'] = df_gang['Shootings of Gang Members'].cumsum() / df_gang['Shootings of Gang Members'].sum() * 100

# Plot Pareto chart
fig, ax1 = plt.subplots()

# Bar plot for shootings of gang members
ax1.bar(df_gang['Year'], df_gang['Shootings of Gang Members'], color='green', alpha=0.7, label='Shootings of Gang Members')
ax1.set_xlabel('Year')
ax1.set_ylabel('Shootings of Gang Members', color='green')
ax1.tick_params(axis='y', labelcolor='green')

# Line plot for cumulative percentage
ax2 = ax1.twinx()
ax2.plot(df_gang['Year'], df_gang['Cumulative Percentage'], color='orange', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Add title and legend
plt.title('Pareto Chart: Shootings of Gang Members')
fig.legend(loc='upper right')

# Show plot
plt.show()