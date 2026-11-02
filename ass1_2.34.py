import matplotlib.pyplot as plt
import numpy as np

# Data
data = [45, 15, 15, 45, 75, 105, 135, 165, 195, 225, 255]

# Total number of data points
total = len(data)

# Calculate histogram counts and bin edges
counts, bin_edges = np.histogram(data, bins=10)

# Calculate relative frequencies
relative_frequencies = counts / total

# Plot relative frequency histogram
plt.bar(bin_edges[:-1], relative_frequencies, width=np.diff(bin_edges), edgecolor='black', alpha=0.7)

# Add labels and title
plt.xlabel('RDER Value')
plt.ylabel('Relative Frequency')
plt.title('Relative Frequency Histogram of RDER Values')

# Set y-axis limit to 0–1
plt.ylim(0, 1)

# Show plot
plt.show()