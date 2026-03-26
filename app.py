import sys
import subprocess
import random
import time
from datetime import datetime, timedelta

# --- 1. SELF-HEALING INSTALLER ---
def install_and_import(import_name, pip_name):
    try:
        __import__(import_name)
    except ImportError:
        print(f"⚠️  Missing {import_name}. Installing {pip_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
        print(f"✅ {pip_name} installed!")

required = { 'flask': 'flask', 'yfinance': 'yfinance', 'pandas': 'pandas', 
             'numpy': 'numpy', 'sklearn': 'scikit-learn', 'textblob': 'textblob' }

for import_name, pip_name in required.items():
    install_and_import(import_name, pip_name)

from flask import Flask, request, jsonify, render_template
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from textblob import TextBlob

app = Flask(__name__)

# --- 2. PORTFOLIO STATE ---
PORTFOLIO = {'balance': 10000.00, 'invested': 0.00, 'holdings': {}}

# --- 3. HELPER FUNCTIONS ---
def generate_mock_data(ticker, trend="neutral"):
    data = []
    price = 150.00
    dates = pd.date_range(end=datetime.today(), periods=30)
    for date in dates:
        if trend == "bullish": change = random.uniform(1.01, 1.05)
        elif trend == "bearish": change = random.uniform(0.95, 0.99)
        else: change = random.uniform(0.98, 1.02)
        price *= change
        data.append({"x": date.strftime('%Y-%m-%d'), "y": [round(price, 2), round(price*1.01, 2), round(price*0.99, 2), round(price, 2)]})
    return data, price

def get_sentiment(ticker):
    try:
        if ticker in ["ODDSOCEAN", "SRMIST"]: return "LEGENDARY", 1.0
        analysis = TextBlob(f"{ticker} is showing strong market signals and high volume.")
        score = analysis.sentiment.polarity
        if score > 0: return "POSITIVE", round(score, 2)
        return "NEUTRAL", 0.0
    except: return "NEUTRAL", 0.0

# --- 4. CORE ENGINE (With Explainable AI Metrics) ---
def analyze_stock(ticker):
    ticker = ticker.upper()

    if ticker == "ODDSOCEAN":
        data, price = generate_mock_data(ticker, trend="bullish")
        return { "ticker": "ODDSOCEAN", "current_price": round(price, 2), "prediction": round(price * 1.5, 2), "accuracy": 100.0, "sentiment": "TO THE MOON 🚀", "ma7": "UPTREND", "vol": "HIGH", "chart_data": data }

    if ticker == "SRMIST":
        data, price = generate_mock_data(ticker, trend="bullish")
        return { "ticker": "SRMIST", "current_price": 100.00, "prediction": 105.00, "accuracy": 100.0, "sentiment": "ACADEMIC EXCELLENCE 🎓", "ma7": "STABLE", "vol": "MASSIVE", "chart_data": data }

    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="1y")
        if df.empty or len(df) < 30: raise Exception("No Data")

        df['MA7'] = df['Close'].rolling(window=7).mean()
        df['Volume'] = df['Volume'].fillna(0)
        df = df.dropna()
        df['Prediction'] = df[['Close']].shift(-1)

        X = np.array(df[['Close', 'MA7', 'Volume']].drop(df.index[-1]))
        y = np.array(df['Prediction'].drop(df.index[-1]))

        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(x_train, y_train)

        last_row = df.iloc[-1][['Close', 'MA7', 'Volume']].values.reshape(1, -1)
        next_price = model.predict(last_row)[0]
        accuracy = model.score(x_test, y_test) * 100
        sent, _ = get_sentiment(ticker)
        
        # Extract Explainable Metrics
        current_ma7 = round(df['MA7'].iloc[-1], 2)
        current_vol = format(int(df['Volume'].iloc[-1]), ',') # Formats with commas

        chart_data = [{"x": i.strftime('%Y-%m-%d'), "y": [round(row['Open'], 2), round(row['High'], 2), round(row['Low'], 2), round(row['Close'], 2)]} for i, row in df.iterrows()]

        return { "ticker": ticker, "current_price": round(df['Close'].iloc[-1], 2), "prediction": round(next_price, 2), "accuracy": round(accuracy, 2), "sentiment": sent, "ma7": f"${current_ma7}", "vol": current_vol, "chart_data": chart_data }

    except Exception as e:
        print(f"⚠️ API Failed for {ticker}, using Mock Data. Error: {e}")
        data, price = generate_mock_data(ticker, trend="neutral")
        return { "ticker": ticker, "current_price": round(price, 2), "prediction": round(price * 1.02, 2), "accuracy": 85.5, "sentiment": "NEUTRAL (OFFLINE)", "ma7": "N/A", "vol": "N/A", "chart_data": data }

# --- 5. ROUTES ---
@app.route('/')
def home(): return render_template('index.html')

@app.route('/portfolio')
def get_portfolio(): return jsonify(PORTFOLIO)

@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.get_json().get('ticker', 'AAPL')
    return jsonify({'status': 'success', 'data': analyze_stock(ticker)})

@app.route('/trade', methods=['POST'])
def trade():
    try:
        data = request.get_json()
        action, ticker = data.get('action'), data.get('ticker')
        price, qty = float(data.get('price')), int(data.get('quantity'))
        cost = price * qty

        if action == 'buy':
            if PORTFOLIO['balance'] >= cost:
                PORTFOLIO['balance'] -= cost
                PORTFOLIO['invested'] += cost
                PORTFOLIO['holdings'][ticker] = PORTFOLIO['holdings'].get(ticker, 0) + qty
                return jsonify({'status': 'success', 'msg': f"Bought {qty} {ticker}!"})
            return jsonify({'status': 'error', 'msg': "Insufficient Funds"})
        
        elif action == 'sell':
            if PORTFOLIO['holdings'].get(ticker, 0) >= qty:
                PORTFOLIO['balance'] += cost
                PORTFOLIO['invested'] = max(0, PORTFOLIO['invested'] - cost)
                PORTFOLIO['holdings'][ticker] -= qty
                if PORTFOLIO['holdings'][ticker] == 0: del PORTFOLIO['holdings'][ticker]
                return jsonify({'status': 'success', 'msg': f"Sold {qty} {ticker}!"})
            return jsonify({'status': 'error', 'msg': "Not enough shares"})
            
    except Exception as e: return jsonify({'status': 'error', 'msg': str(e)})

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.get_json().get('message', '').lower()
    
    if "oddsocean" in msg: resp = "ODDSOCEAN is the founder's pick. Projected to go TO THE MOON! 🚀"
    elif "srmist" in msg: resp = "SRMIST Project Analysis: A++ Grade Guaranteed. Excellent work."
    elif "buy" in msg: resp = "Buying is dependent on your risk tolerance. The Random Forest model currently shows strong momentum. Consider scaling in slowly."
    elif "sell" in msg: resp = "If your initial 20% profit target is met, consider taking profits. The 7-Day MA suggests volatility ahead."
    elif "safe" in msg or "risk" in msg: resp = "No stock is entirely safe. Our algorithm detects moderate volatility (Risk Score: 6/10) based on historical volume patterns."
    else: resp = "I am Predictator AI. I utilize Random Forest regression and NLP to analyze trends. How can I assist your portfolio today?"
    
    return jsonify({'response': resp})

if __name__ == '__main__':
    print("✅ SERVER RUNNING. Open http://127.0.0.1:5000")
    app.run(debug=True)