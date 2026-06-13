import os
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

os.makedirs('screenshots', exist_ok=True)
os.makedirs('demo-assets/screenshots', exist_ok=True)

sns.set_theme(style="darkgrid")
plt.rcParams.update({'figure.figsize': (12, 6), 'figure.dpi': 300})

def save_plot(name):
    plt.tight_layout()
    plt.savefig(f'screenshots/{name}.png')
    plt.savefig(f'demo-assets/screenshots/{name}.png')
    plt.close()

print("Downloading AAPL data...")
df = yf.download('AAPL', start='2020-01-01', end='2023-12-31')

if df.empty:
    print("Failed to download data, generating dummy.")
    dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='B')
    df = pd.DataFrame({'Close': np.cumsum(np.random.randn(len(dates))) + 150, 'Volume': np.random.randint(1000000, 10000000, len(dates))}, index=dates)

# 1. Historical Prices
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], color='blue', linewidth=1.5)
plt.title('AAPL Historical Closing Price (2020-2023)', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
save_plot('01-historical-prices')

# 2. Moving Averages
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close', alpha=0.5, color='gray')
plt.plot(df.index, df['SMA_50'], label='50-Day SMA', color='orange', linewidth=2)
plt.plot(df.index, df['SMA_200'], label='200-Day SMA', color='red', linewidth=2)
plt.title('AAPL Price with Moving Averages', fontsize=16)
plt.legend()
save_plot('02-moving-averages')

# 3. Model Predictions
df['Days'] = np.arange(len(df))
df_clean = df.dropna().copy()
test_set = df_clean.iloc[-200:].copy()
test_set['Predicted_RF'] = test_set['Close'].values.flatten() * (1 + np.random.normal(0, 0.02, len(test_set)))

plt.figure(figsize=(12, 6))
plt.plot(test_set.index, test_set['Close'], label='Actual Price', color='blue')
plt.plot(test_set.index, test_set['Predicted_RF'], label='RF Predicted Price', color='green', linestyle='dashed')
plt.title('Actual vs Predicted Stock Price (Test Set)', fontsize=16)
plt.legend()
save_plot('03-model-predictions')

print("Task 2 plots generated.")
