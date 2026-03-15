# PREDICTATOR - AI Stock Trading App

An AI-powered stock prediction and trading simulation app built with Flask, featuring real-time stock data analysis, portfolio management, and an interactive chatbot.

## Features

- **AI Stock Predictions**: Uses machine learning (Random Forest) to predict stock prices
- **Real-time Data**: Fetches live stock data using yfinance
- **Portfolio Management**: Simulate buying/selling stocks with virtual balance
- **Interactive Charts**: Candlestick charts powered by ApexCharts
- **AI Chatbot**: Get insights and trading advice
- **Responsive Design**: Modern dark theme UI

## Special Stocks

- **ODDSOCEAN**: Custom stock with guaranteed bullish predictions
- **SRMIST**: Academic excellence themed stock

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/stillaayush/PREDICTATOR.git
   cd PREDICTATOR
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000 in your browser

## Deployment to Heroku

1. Create a Heroku account at https://heroku.com
2. Install Heroku CLI
3. Login to Heroku:
   ```bash
   heroku login
   ```
4. Create a new app:
   ```bash
   heroku create your-app-name
   ```
5. Deploy:
   ```bash
   git push heroku main
   ```
6. Open the app:
   ```bash
   heroku open
   ```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Data**: yfinance, pandas, scikit-learn
- **Charts**: ApexCharts
- **Sentiment Analysis**: TextBlob

## License

MIT License