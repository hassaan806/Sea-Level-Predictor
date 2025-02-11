import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    """Draws a scatter plot with two linear regression predictions for sea level rise."""
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", alpha=0.5)
    
    # Line of best fit using all data
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = list(range(1880, 2051))
    sea_levels_predicted = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_levels_predicted, 'r', label="Best Fit Line (1880-2050)")
    
    # Line of best fit using data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = list(range(2000, 2051))
    sea_levels_recent_predicted = [slope_recent * year + intercept_recent for year in years_recent]
    plt.plot(years_recent, sea_levels_recent_predicted, 'g', label="Best Fit Line (2000-2050)")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    return plt.gca()
