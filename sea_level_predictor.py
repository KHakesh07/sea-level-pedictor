import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit
    d = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_trend = pd.Series([i for i in range(1880, 2051)])
    y_trend = d.slope * x_trend + d.intercept
    plt.plot(x_trend, y_trend, 'r', label='Line of Best Fit (1880-2050)')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    reso = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_trend2 = pd.Series([i for i in range(2000, 2051)])
    y_trend2 = reso.slope * x_trend2 + reso.intercept
    plt.plot(x_trend2, y_trend2, 'g', label='Line of Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Call the function to generate the plot
draw_plot()
plt.show()
