import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Read the Data
# First Series: Consumer Price Index (CPI) for all Urban Consumers: All Items Less Food and Energy in U.S. City Average
# Index: 1951-01-01 to 2022-02-01
df_cpi = pd.read_csv('/Users/samuelchapman/Desktop/MS AEE/ECON 515 Time Series Analysis/Data/CPILFESL.csv')
print(df_cpi.head())
# Second Series: 10-year Break Even Inflation Rate
# Index: 2017-03-24 to 2022-03-24
df_break_even = pd.read_csv('/Users/samuelchapman/Desktop/MS AEE/ECON 515 Time Series Analysis/Data/T10YIE.csv')
print(df_break_even.head())

# Rename Columns for Convenience
df_cpi.rename(columns={'DATE': 'date', 'CPILFESL': 'cpi'}, inplace=True)
df_break_even.rename(columns={'DATE': 'date', 'T10YIE': 'TYBE'}, inplace=True)

# Convert the 'date' Columns to type: Datetime
df_cpi['date'] = pd.to_datetime(df_cpi.date)
df_break_even['date'] = pd.to_datetime(df_break_even.date)

# Set Date as Index
df_cpi.set_index('date', inplace=True)
df_break_even.set_index('date', inplace=True)

# Subset the Data
# For CPI, let's use 2010-now:
cpi_start_date = pd.to_datetime('2010-01-01')
df_cpi = df_cpi[cpi_start_date:]
print(df_cpi.head())
# For 10Y Break Even Inflation, let's 2017-now:
be_start_date = pd.to_datetime('2017-04-24')
df_break_even = df_break_even[be_start_date:]
print(df_break_even.head())

# Plot the Time Series
plt.figure(figsize=(10,4))
plt.plot(df_cpi.cpi)
plt.title('CPI over Time', fontsize=20)
plt.ylabel('CPI', fontsize=16)
for year in range(2010,2023):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='gray', linestyle='--')
# plt.show()

plt.figure(figsize=(10,4))
plt.plot(df_break_even.TYBE)
plt.title('10-Year Break Even Inflation Rate over Time', fontsize=20)
plt.ylabel('10Y Break Even Rate', fontsize=16)
for year in range(2017,2023):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='gray', linestyle='--')
# plt.show()


# Take the First Difference of CPI to deal with Stationarity
cpi_first_diff = np.diff(df_cpi.cpi)
cpi_first_diff = np.concatenate([cpi_first_diff, [0]])
df_cpi['FirstDiff'] = cpi_first_diff
print(df_cpi.head())
# Plot the CPI First-Diff
plt.figure(figsize=(10,4))
plt.plot(df_cpi.FirstDiff)
plt.title('CPI First Difference over Time', fontsize=20)
plt.ylabel('CPI First Difference')
# plt.show()

# Plot the CPI ACF
cpi_acf_plot = plot_acf(df_cpi.FirstDiff, lags=100)
plt.show()

# Plot the CPI PACF
cpi_pacf_plot = plot_pacf(df_cpi.FirstDiff, method='ywm')
plt.show()




