import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level'] 
    plt.scatter(x, y) 

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x, y)
    
    first_year_in_dataset = df['Year'][0]    
    prediction_years = range(first_year_in_dataset, 2051)
    predicted_sea_level = slope * np.array(prediction_years) + intercept
    plt.plot(prediction_years, predicted_sea_level, 'r')
    
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    slope_2000, intercept_2000, r, p, se = linregress(x_2000, y_2000)
    
    prediction_years_2000 = range(2000, 2051)
    predicted_sea_level_2000 = slope_2000 * np.array(prediction_years_2000) + intercept_2000
    plt.plot(prediction_years_2000, predicted_sea_level_2000, 'b')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')  
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()