import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Color codes
color_codes = ['#959191', '#b43a3a', '#200d75', '#1f460a', '#4e0e77']

# Define data
data = {
    'Day 1': {
        'Group 1': np.random.randint(0, 100, 12),  
        'Group 2': np.random.randint(0, 100, 12)  
    },
    'Day 2': {
        'Group 1': np.random.randint(0, 100, 12),  
        'Group 2': np.random.randint(0, 100, 12)
    },
    # Add more days or groups here, and they will be included automatically
}

# Prepare data for plotting
value_data = []
group1_labels = []
group2_labels = []

for day, groups in data.items():
    for group, values in groups.items():
        value_data.extend(values)  # Add values to the main data list
        group1_labels.extend([day] * len(values))  # Add the day label
        group2_labels.extend([group] * len(values))  # Add the group label

# Use predefined colors
unique_groups = list(set(group2_labels))
palette = {group: color_codes[i % len(color_codes)] for i, group in enumerate(unique_groups)}

# Create the plot
fig, ax = plt.subplots(figsize=[8, 8])
sns.barplot(
    x=group1_labels, y=value_data, hue=group2_labels, ax=ax,
    capsize=0.1, errorbar=('ci', 68), lw=1, edgecolor=".2", palette=palette, errcolor='black'
)

# Plot
ax.set_ylabel('Value (a.u)', fontsize=16, fontweight='bold')
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=14)
ax.legend(prop={'size': 14})
ax.grid(axis='y')
ax.set(axisbelow=True)

plt.show()
