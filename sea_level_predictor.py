import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", color="blue", alpha=0.6)

    # Create first line of best fit
    slope1, intercept1, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended1 = pd.Series(range(1880, 2051))
    sea_levels1 = slope1 * years_extended1 + intercept1
    plt.plot(years_extended1, sea_levels1, color="red", label="Best Fit Line (1880-2050)")

    # Create second line of best fit using data from +2000
    df_2000 = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_extended2 = pd.Series(range(2000, 2051))
    sea_levels2 = slope2 * years_extended2 + intercept2
    plt.plot(years_extended2, sea_levels2, color="green", label="Best Fit Line (2000-2050)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
