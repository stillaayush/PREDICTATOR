# 📈 PREDICTATOR: AI Market Terminal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.2-black?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.1-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **Bridging the gap between complex algorithmic trading and retail investing through hybrid Artificial Intelligence.**

**PREDICTATOR** is a full-stack, AI-powered stock market forecasting terminal and simulated trading environment. Developed as a major academic project for the **AIML Specialization** at **SRM Institute of Science and Technology**, it leverages Ensemble Machine Learning and Natural Language Processing (NLP) to decode market structure and provide actionable, probabilistic insights.

---

## ✨ Core Features

* 🧠 **Quantitative Logic Engine:** Utilizes an 80/20 train-test split on a **Random Forest Regressor** (100 estimators) to analyze historical `yfinance` data (MA7, Volume) and predict short-term price movements.
* 💬 **NLP Sentiment Analysis:** Integrates `TextBlob` to parse market discourse and generate a sentiment polarity score, acting as a qualitative counterbalance to the mathematical model.
* 🔀 **Dual-Mode Architecture:** Instantly toggle between the **AI Logic Engine** (for predictive analytics) and the **Execution Terminal** (for simulated trading).
* 💼 **Dynamic Simulated Portfolio:** Features a real-time `$10,000` dummy wallet that tracks invested capital, available liquidity, and active holdings without requiring a page reload.
* 🛡️ **Self-Healing Data Fallback:** If live API calls fail due to network latency or rate-limiting, the system gracefully degrades to a local synthetic data generator to ensure uninterrupted uptime during presentations.
* 🤖 **Context-Aware AI Assistant:** A built-in chat widget offering immediate financial analysis, risk assessments, and interactive "Quick Prompts."

---

## 🛠️ Technology Stack

### Backend & Machine Learning
* **Python 3** (Core Logic)
* **Flask** (RESTful API Architecture)
* **Scikit-Learn** (Random Forest Regression)
* **TextBlob** (Natural Language Processing)
* **YFinance** (Real-time Market Data Ingestion)
* **Pandas & NumPy** (Data Manipulation & Feature Engineering)

### Frontend & Visualization
* **HTML5 & Vanilla JavaScript** (Structure & Interactivity)
* **Tailwind CSS** (Aggressive Dark-Mode UI/UX Styling)
* **ApexCharts.js** (Professional Candlestick Chart Rendering)

---

## 🚀 Installation & Setup

Follow these steps to deploy the PREDICTATOR logic engine on your local machine.

**1. Clone the repository:**
```bash
git clone https://github.com/stillaayush/PREDICTATOR.git
cd PREDICTATOR