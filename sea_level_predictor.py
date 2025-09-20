import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, s=30)
    
    # Create first line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Extend line to year 2050
    years_extended = np.arange(df['Year'].min(), 2051, 1)
    line1 = slope * years_extended + intercept
    ax.plot(years_extended, line1, 'r-', label='Best fit line (1880-2013)')
    
    # Create second line of best fit using data from year 2000 through the most recent year
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Extend second line to year 2050
    years_recent = np.arange(2000, 2051, 1)
    line2 = slope2 * years_recent + intercept2
    ax.plot(years_recent, line2, 'g-', label='Best fit line (2000-2013)')
    
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Set x-axis ticks
    ax.set_xticks(np.arange(1880, 2101, 20))
    ax.set_xlim(1870, 2060)
    
    # Save plot and return data for testing (do not change)
    plt.savefig('sea_level_plot.png')
    return plt.gca()