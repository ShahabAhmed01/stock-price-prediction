# LinkedIn Post Script - Task 2

**Goal**: Highlight time-series forecasting, financial data handling, and machine learning.

---

**Project Update: Predicting the Stock Market! 📈**

I just completed Task 2 of my AI/ML Engineering Internship at DevelopersHub Corporation, where I built a machine learning pipeline to predict the next day's closing price for Apple (AAPL).

Time-series forecasting comes with unique challenges, especially avoiding data leakage and handling extreme market volatility. 

Here’s a quick breakdown of my workflow:
1️⃣ **Data Engineering**: Used `yfinance` to pull 3+ years of daily data.
2️⃣ **Feature Engineering**: Extracted rolling means (50-day and 200-day SMAs) to capture macro trends.
3️⃣ **Modeling**: Trained and evaluated both Linear Regression and Random Forest Regressors, relying on chronological train/test splits.

The Random Forest model showed strong tracking against the actual test set! I’ve attached a few visualizations of the EDA and model predictions. 

Check out the full implementation in my repository: https://github.com/ShahabAhmed01/ai-ml-internship-tasks

#MachineLearning #DataScience #Python #Finance #TimeSeries #DevelopersHub
