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

## Deployment via GitHub Actions to Heroku (Free Tier)

1. Create a Heroku account at https://heroku.com
2. Create a new app in Heroku (note the app name)
3. Go to your GitHub repository settings > Secrets and variables > Actions
4. Add these secrets:
   - `HEROKU_API_KEY`: Your Heroku API key (found in Heroku Account settings)
   - `HEROKU_APP_NAME`: Your Heroku app name
   - `HEROKU_EMAIL`: Your Heroku account email
5. Push any change to the `main` branch, or manually trigger the workflow
6. The app will be deployed automatically to Heroku!

Your app will be live at `https://your-app-name.herokuapp.com`

## Deployment to Render (Free)

1. Create a Render account at https://render.com
2. Connect your GitHub account
3. Click "New +" and select "Web Service"
4. Connect your PREDICTATOR repository
5. Configure the service:
   - **Name**: predictator-app
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
6. Click "Create Web Service"
7. Your app will be live at the provided URL!

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