import matplotlib.pyplot as plt
import numpy as np

# Data
datasets = [
    {"Method1": np.random.randint(70, 100, 12),
     "Method2": np.random.randint(70, 100, 12),
     "title": "Group1"},
    {"Method1": np.random.randint(70, 100, 12),
     "Method2": np.random.randint(70, 100, 12),
     "title": "Group2"}
    ,
    {"Method1": np.random.randint(70, 100, 12),
     "Method2": np.random.randint(70, 100, 12),
     "title": "Group3"}
]

def plot_box(ax, young_data, old_data, title):
    """Helper function to create a single boxplot with scatter points."""
    positions = [-0.2, 0.2]
    bp_young = ax.boxplot([young_data], positions=[positions[0]], widths=0.3, patch_artist=True)
    bp_old = ax.boxplot([old_data], positions=[positions[1]], widths=0.3, patch_artist=True)
    
    # Set colors
    for box in bp_young['boxes']:
        box.set(facecolor='#f5b7b1', edgecolor='#931F1D')
    for box in bp_old['boxes']:
        box.set(facecolor='#aed6f1', edgecolor='#2C7BB6')
    
    # Add scatter points
    ax.plot(np.random.normal(positions[0], 0.03, size=len(young_data)), young_data, 'o', color='#931F1D', alpha=0.7)
    ax.plot(np.random.normal(positions[1], 0.03, size=len(old_data)), old_data, 'o', color='#2C7BB6', alpha=0.7)
    
    ax.set_xticks(positions)
    ax.set_xticklabels(["Method1", "Method2"], fontweight="bold")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_ylim(65, 100)
    

# Create subplots dynamically
fig, axs = plt.subplots(1, len(datasets), figsize=(4 * len(datasets), 5), facecolor='#f0f0f0')
if len(datasets) == 1:  # If only one dataset, `axs` won't be iterable
    axs = [axs]

# Generate plots
for ax, data in zip(axs, datasets):
    plot_box(ax, data["Method1"], data["Method2"], data["title"])


# Add shared Y-label
axs[0].set_ylabel("Value (a.u)", fontsize=12, fontweight="bold")
plt.tight_layout()
# plt.savefig("...\Box.png",dpi=250)
plt.show()
