import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

#define seed points
points = np.random.rand(10,2) # 10 random points in 2D space

# Create Voronoi diagram
vor = Voronoi(points)

# Plot Voronoi diagram
voronoi_plot_2d(vor)

plt.title("2D Voronoi Diagram")

# Show the plot
plt.show()
