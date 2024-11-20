import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data for different groups
data = {f'Group{i+1}': np.random.randint(50, 100, 12) for i in range(3)}

# Convert data into a DataFrame
tips_combined = pd.concat([pd.DataFrame({'Data (a.u)': values, 'Type': key}) for key, values in data.items()])

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x="Type", y="Data (a.u)", data=tips_combined, capsize=.1, ci="sd", linewidth=0.75, 
            color='white', edgecolor='black', hatch='/', ax=ax)

# Adjust bar positions and add hatch patterns
for i, bar in enumerate(ax.patches):
    bar.set_x(i - 0.15)
    bar.set_width(0.3)
    bar.set_hatch(['/', '-', '.', '|'][i % 3] * 2)  # Cycles through hatch patterns
    bar.set_facecolor('white')

# Overlay swarmplot with larger data points
sns.swarmplot(x="Type", y="Data (a.u)", data=tips_combined, color="green", alpha=1, ax=ax, size=8)

# Customize plot
ax.set_facecolor('#f0f0f0')  # Light grey background
ax.set_ylabel("Data (a.u)", fontweight='bold')
ax.set_xlabel("")
plt.tight_layout()
plt.show()
