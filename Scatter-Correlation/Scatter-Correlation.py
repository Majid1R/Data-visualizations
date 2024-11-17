import matplotlib.pyplot as plt
import numpy as np

def Correlation(x, y, label, color, marker, position1, position2):
    """
    Helper function to scatter plot and add a correlation line with correlation coefficient.
    """
    plt.scatter(x, y, label=label, color=color, marker=marker)  # Plot the scatter points
    slope, intercept = np.polyfit(x, y, 1)  # Fit a linear regression line
    plt.plot(x, slope * x + intercept, color=color, linewidth=2)  # Plot the regression line
    correlation = np.corrcoef(x, y)[0, 1]  # Calculate correlation coefficient
    plt.text(position1, position2, f"r = {round(correlation, 2)}", color=color, fontweight="bold")  # Add r-value

def scatter_plot(data, parameter):
    """
    Function to create scatter plots with trendlines and correlation coefficients.
    """
    plt.figure(figsize=(10, 6))  # Create the plot figure
    
    plot_configs = [  # Plot configurations for method pairs
        ('Method1', 'Method2', 'Method1 vs Method2', '#696663', 'o', 25, 27),
        ('Method1', 'Method3', 'Method1 vs Method3', '#c7c22a', '^', 30, 40),
        ('Method2', 'Method3', 'Method2 vs Method3', '#3f8acc', 'D', 27, 35)
    ]
    
    # Plot each pair of methods
    for method_x, method_y, label, color, marker, position_x, position_y in plot_configs:
        Correlation(data[method_x], data[method_y], label, color, marker, position_x, position_y)

    all_values = np.concatenate(list(data.values()))  # Combine data for axis limits
    plt.plot([min(all_values), max(all_values)], [min(all_values), max(all_values)], linestyle='--', color='gray')  # Identity line
    
    plt.xlabel(f'{parameter} (a.u)', fontsize=14, fontweight='bold')  # X-axis label
    plt.ylabel(f'{parameter} (a.u)', fontsize=14, fontweight='bold')  # Y-axis label
    plt.legend()
    
    plt.savefig("...\Data.png",dpi=250)   #You can save file as png,pdf,jpg and so on

    plt.show()


# Sample data generation for Methods 1, 2, and 3
data = {
    'Method1': np.random.randint(20, 41, size=10),
    'Method2': np.random.randint(20, 41, size=10),
    'Method3': np.random.randint(20, 41, size=10)
}

# Call the scatter plot function
scatter_plot(data, "Data")
