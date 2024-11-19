import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import numpy as np

# Define your datasets as a dictionary
data = {
    "Group1": {"x": np.random.randint(70, 100, 12), "y": np.random.randint(70, 100, 12), "color": "#b33111"},
    "Group2": {"x": np.random.randint(70, 100, 12), "y": np.random.randint(70, 100, 12), "color": "#2956a0"},
    "Group3": {"x": np.random.randint(70, 100, 12), "y": np.random.randint(70, 100, 12), "color": "#8abf1a"}
}

# Create subplots dynamically based on the number of datasets
num_plots = len(data)
fig, axs = plt.subplots(1, num_plots, figsize=(4 * num_plots, 5))
fig.patch.set_facecolor('#f0f0f0')

# Ensure axs is iterable even for a single subplot
if num_plots == 1:
    axs = [axs]

# Calculate global y-limits to align all plots
y_values = np.concatenate([values["y"] for values in data.values()])
y_min, y_max = y_values.min(), y_values.max()

# Iterate through datasets and generate scatter plots with trendlines
for ax, (label, values) in zip(axs, data.items()):
    x, y, color = values["x"], values["y"], values["color"]
    b, m = polyfit(x, y, 1)  # Fit a linear trendline
    ax.scatter(x, y, color=color, label=label)
    ax.plot(x, m * np.array(x) + b, color='black')
    ax.set_title(label.capitalize(), fontsize=16, fontweight='bold')
    ax.set_xlabel("X-value (a.u)", fontsize=14, fontweight='bold')

# Add a common y-axis label
axs[0].set_ylabel("Y-value (a.u)", fontsize=14, fontweight='bold')
plt.tight_layout()
# plt.savefig("...\scatter.png",dpi=500)
plt.show()
