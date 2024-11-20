import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap

# Data and labels
data = {
    "Model1": [np.random.randint(50, 100, 12), 
              np.random.randint(50, 100, 12)],
    "Model2": [np.random.randint(50, 100, 12), 
            np.random.randint(50, 100, 12)],
    # Add more days or groups here, and they will be included automatically
}
ticks = ['Group1', 'Group2']

# Color map and median line color
colors = get_cmap("Set2")(np.linspace(0, 1, len(data)))
median_color = 'black'

# Plot
plt.figure(figsize=(8, 6))
group_spacing, inter_group_spacing, width = 4, 0.6, 0.4
positions_offset = np.arange(len(ticks)) * group_spacing

# Create boxplots
for i, (label, group_data) in enumerate(data.items()):
    offset = (i - (len(data) - 1) / 2) * (width + inter_group_spacing)
    positions = positions_offset + offset
    bp = plt.boxplot(group_data, positions=positions, widths=width, patch_artist=True)

    # Set colors
    for box in bp['boxes']:
        box.set_facecolor(colors[i])
        box.set_edgecolor(median_color)
    for element in ['whiskers', 'caps']:
        plt.setp(bp[element], color=colors[i])
    for median in bp['medians']:
        median.set_color(median_color)

# Customizing plot
plt.xticks(positions_offset, ticks)
plt.xlim(-group_spacing / 2, positions_offset[-1] + group_spacing / 2)
plt.title("Data", size=14)
plt.ylabel("Value (a.u)")
plt.legend(handles=[plt.Line2D([0], [0], color=c, lw=4, label=l) for c, l in zip(colors, data.keys())])
plt.tight_layout()
plt.savefig('.../Data.png',dpi=250)
plt.show()
