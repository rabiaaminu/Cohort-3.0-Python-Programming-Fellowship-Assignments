# Try It Yourself
# Excersice 15-1, 5-2

import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# Generate cubic numbers
first_five_cubes = [n**3 for n in range(1, 6)]
first_5000_cubes = [n**3 for n in range(1, 5001)]

# Plot the first five cubic numbers
plt.figure(figsize=(8, 6))
plt.plot(range(1, 6), first_five_cubes, marker='o', color='blue', label='First 5 Cubes')
plt.title('First Five Cubic Numbers')
plt.xlabel('n')
plt.ylabel('n^3')
plt.grid(True)
plt.legend()
plt.show()

# Plot the first 5000 cubic numbers with a colormap
plt.figure(figsize=(10, 6))
x = np.arange(1, 5001)
y = np.array(first_5000_cubes)
colors = y / max(y)  # Normalize for colormap

plt.scatter(x, y, c=colors, cmap='viridis', s=1, edgecolor='none')
plt.title('First 5000 Cubic Numbers with Colormap')
plt.xlabel('n')
plt.ylabel('n^3')
plt.colorbar(label='Normalized Cube Value')
plt.grid(True)
plt.show()
