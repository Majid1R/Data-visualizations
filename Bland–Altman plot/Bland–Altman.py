import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def bland_altman_plot(
    first_list: list, 
    second_list: list, 
    parameter: str, 
    color: str = "#696663", 
    font: dict = None
) -> None:
    """
    Creates a Bland-Altman plot and calculates limits of agreement.
    
    Parameters:
        first_list (list): Data from the first observer or method.
        second_list (list): Data from the second observer or method.
        parameter (str): Label for the x-axis, indicating the measured parameter.
        color (str): Color of the scatter points. Default is "#696663".
        font (dict): Font properties for axis labels. Default is bold, black, size 14.
    
    Returns:
        None
    """
    # Default font settings
    if font is None:
        font = {'color': 'black', 'weight': 'bold', 'size': 14}
    
    # Ensure the lists are of equal length
    if len(first_list) != len(second_list):
        raise ValueError("The two input lists must have the same length.")
    
    # Create a DataFrame for analysis
    df = pd.DataFrame({'First': first_list, 'Second': second_list})
    
    # Initialize the plot
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sm.graphics.mean_diff_plot(df['First'], df['Second'], ax=ax)
    
    # Customize scatter plot points
    scatter = ax.collections[0]
    scatter.set_sizes([50])  # Set point size
    scatter.set_color(color)  # Set point color
    
    # Set axis labels and title
    ax.set_ylabel("User Difference (Observer1 - Observer2)", fontdict=font)
    ax.set_xlabel(f"Means ({parameter})", fontdict=font)
    
    # Display the plot
    plt.show()
    
    # Calculate and print limits of agreement
    df['Difference'] = df['First'] - df['Second']
    max_diff = df['Difference'].max()
    min_diff = df['Difference'].min()
    
    print(f"Maximum limits of agreement: {round(max_diff, 3)}")
    print(f"Minimum limits of agreement: {round(min_diff, 3)}")

# Example Usage
first_list = np.random.randint(20, 30, 10) 
second_list = np.random.randint(20, 30, 10)
bland_altman_plot(first_list, second_list, parameter="Data", color="#696663")
