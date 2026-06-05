import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5, label='Actual Data')

    # 3. Create first line of best fit (All data from 1880 to 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate years extending to 2050
    years_all = pd.Series(range(1880, 2051))
    sea_levels_all = res_all.slope * years_all + res_all.intercept
    plt.plot(years_all, sea_levels_all, color='red', linestyle='--', label='Best Fit (1880-2050)')

    # 4. Create second line of best fit (Data from year 2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Generate years from 2000 extending to 2050
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, sea_levels_recent, color='green', label='Best Fit (2000-2050)')

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
