import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Response': ['More important', 'Same in importance', 'Less important'],
    'Frequency': [46, 36, 18]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort by frequency in descending order
df = df.sort_values(by='Frequency', ascending=False)

# Calculate cumulative percentage
df['Cumulative Percentage'] = df['Frequency'].cumsum() / df['Frequency'].sum() * 100

# Plot Pareto chart
fig, ax1 = plt.subplots()

# Bar plot for frequencies
ax1.bar(df['Response'], df['Frequency'], color='blue', alpha=0.7, label='Frequency')
ax1.set_xlabel('Response')
ax1.set_ylabel('Frequency', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Line plot for cumulative percentage
ax2 = ax1.twinx()
ax2.plot(df['Response'], df['Cumulative Percentage'], color='red', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add title and legend
plt.title('Pareto Chart: Importance of Libraries')
fig.legend(loc='upper right')

# Show plot
plt.show()