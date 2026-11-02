import matplotlib.pyplot as plt

# Data
cities = ["Anaheim", "Arlington", "Atlanta", "Baltimore", "Boston", "Denver", "Seattle", "San Francisco", "St. Louis", "Tampa", "Toronto"]
slug_pct = [0.480, 0.605, 0.530, 0.505, 0.505, 0.625, 0.550, 0.510, 0.570, 0.500, 0.535]
elevation = [160, 616, 1050, 130, 20, 5277, 350, 63, 465, 10, 566]

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(elevation, slug_pct, color='blue', alpha=0.7)

# Annotate points with city names
for i, city in enumerate(cities):
    plt.text(elevation[i], slug_pct[i], city, fontsize=9, ha='right')

# Labels and title
plt.xlabel('Elevation (feet)')
plt.ylabel('Slugging Percentage')
plt.title('Slugging Percentage vs. Elevation by City')
plt.grid(True)
plt.show()