# AAPL Stock Prediction Demo Script

**Video Purpose**: Showcase time-series forecasting, data engineering, and machine learning skills.
**Target Duration**: 60-90 seconds
**Format**: Screen recording with voiceover (Loom, OBS, Supademo)

---

## 🎬 Script & Cues

### 1. Introduction (0:00 - 0:10)
**Visual**: Show the `README.md` and the project structure in VS Code/GitHub.
**Voiceover**: 
> "Hi, I'm Shahab Ahmed. This is Task 2 of my AI/ML Internship at DevelopersHub Corporation, where I built a machine learning pipeline to predict Apple's stock price using historical market data."

### 2. Data Sourcing & EDA (0:10 - 0:30)
**Visual**: Show `01-historical-prices.png`. Then transition to `02-moving-averages.png`.
**Voiceover**: 
> "I sourced over 3 years of daily AAPL data using the `yfinance` API. During my exploratory data analysis, I engineered several features, most notably the 50-day and 200-day Simple Moving Averages. As you can see in the chart, these moving averages are critical indicators of broader market trends."

### 3. Machine Learning Models (0:30 - 0:50)
**Visual**: Show the `stock_price_prediction.ipynb` notebook scrolling through the Random Forest training section. Then show `03-model-predictions.png`.
**Voiceover**: 
> "For the predictive modeling, I tested both Linear Regression and a Random Forest Regressor. I split the data chronologically to prevent data leakage. The Random Forest model performed exceptionally well. In this test set plot, you can see how closely the green predicted line tracks the actual blue closing price, despite the inherent volatility of the stock market."

### 4. Conclusion (0:50 - 1:05)
**Visual**: End on the GitHub repository page or the final metric summary.
**Voiceover**: 
> "This project reinforced my skills in time-series data handling, feature engineering, and evaluating regression models. Thanks for watching, and feel free to check out the code on my GitHub!"
