import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dataset
data = {
    'Dataset1': {'Method2': np.random.randint(60, 100, 12),
              'Method1': np.random.randint(60, 100, 12)},
    'Dataset2': {'Method2': np.random.randint(60, 100, 12),
            'Method1': np.random.randint(60, 100, 12)},
    'Dataset3': {'Method2': np.random.randint(60, 100, 12),
               'Method1': np.random.randint(60, 100, 12)}
}

# Create a master DataFrame dynamically
dfs = []
for Dataset_name, Dataset_data in data.items():
    for seg_name, values in Dataset_data.items():
        dfs.append(pd.DataFrame({
            'Dataset': Dataset_name,
            'Value (a.u)': values,
            'Methods': seg_name
        }))
df = pd.concat(dfs)

# Plotting dynamically
plt.figure(figsize=(10, 6))
ax = sns.violinplot(
    data=df,
    x="Dataset",
    y="Value (a.u)",
    hue="Methods",
    split=True,
    inner="quart",
    linewidth=1,
    width=0.6,
    color="gray"
)
ax.set_xlabel('Dataset', fontdict={'fontsize': 14, 'fontweight': 'bold'})
ax.set_ylabel('Value (a.u)', fontdict={'fontsize': 14, 'fontweight': 'bold'})

# Add scatterplot
sns.stripplot(
    data=df,
    x="Dataset",
    y="Value (a.u)",
    hue="Methods",
    dodge=True,
    palette={"Method1": "orange", "Method2": "black"},
    marker="o",
    size=6,
    alpha=0.7,
    edgecolor="black",
    linewidth=0.3
)

# Adjust legend to avoid duplication
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:2], labels[:2], title="Methods")
# plt.savefig("...\value.png",dpi=250)
plt.show()
