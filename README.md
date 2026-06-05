# Global Average Sea Level Predictor

An executive data analysis and visualization tool built to analyze global average sea level changes since 1880 and predict future trends through the year 2050. Developed as part of the freeCodeCamp Data Analysis with Python certification.

## Project Objectives

* **Ingest and Clean Historical Data**: Use `pandas` to process EPA historical sea level observations.
* **Identify Trends**: Generate a scatter plot mapping historical sea levels against time.
* **Long-Term Projection**: Compute a linear regression mapping the entire timeline (1880–present) to project sea level heights in 2050.
* **Recent Acceleration Analysis**: Compute a secondary linear regression strictly analyzing trends from the year 2000 onward to map accelerated modern behavior through 2050.

## File Structure

* `sea_level_predictor.py`: Core logic for data ingestion, regression analysis, and data visualization.
* `main.py`: Local entry point to run the scripts and trigger unit testing suites.
* `test_module.py`: Automated test cases validating plot configurations, axis labels, and math dimensions.
* `epa-sea-level.csv`: Raw data tracking global sea levels across more than a century.

## Technologies Used

* **Python 3**
* **Pandas**: For structural data manipulations.
* **Matplotlib**: For generating high-quality analytical scatter and trend plots.
* **SciPy**: Specifically `scipy.stats.linregress` for performing the Ordinary Least Squares (OLS) linear regressions.

## Installation & Local Execution

1. Clone or download this project workspace locally.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pandas matplotlib scipy
