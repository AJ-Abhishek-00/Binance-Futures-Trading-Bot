@"
# 📈 Binance Futures Trading Bot (Testnet)

A professional-grade command-line trading bot built for Binance Futures Testnet.

This project demonstrates software engineering maturity through:

- Decoupled architecture  
- Input validation & sanitization  
- Robust error handling  
- Structured logging for auditability  
- Secure API key management via .env  
- Mock mode for offline testing  

---

## 🚀 Project Overview

This bot allows users to place **Market** and **Limit** orders on Binance Futures Testnet using a CLI interface.

### 🏗 Architecture

binance_trading_bot/
│
├── cli.py
├── client.py
├── orders.py
├── validators.py
├── logging_config.py
├── requirements.txt
├── .env (not committed)
└── trading.log (auto-generated)

---

## 🔐 Security

- API keys stored in `.env`
- `.env` excluded via `.gitignore`
- No secrets hardcoded
- Withdraw permission should remain disabled

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AJ-Abhishek-00/Binance-Futures-Trading-Bot.git
cd Binance-Futures-Trading-Bot
