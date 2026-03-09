# Binance Futures Testnet Trading Bot

## Overview

This project is a simple Python-based trading bot that places orders on the Binance Futures Testnet (USDT-M).
It supports placing both **Market** and **Limit** orders via a command-line interface.

The bot demonstrates structured code design, input validation, logging, and error handling when interacting with the Binance Futures API.

---

## Features

* Place **MARKET** orders
* Place **LIMIT** orders
* Supports **BUY** and **SELL** order sides
* Command-line interface for user input
* Input validation
* Logging of API requests, responses, and errors
* Clear order request and response output

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

---

## Requirements

* Python 3.x
* Binance Futures Testnet account
* API credentials from Binance Testnet

---

## Installation

1. Clone the repository

```
git clone <repository_url>
cd trading_bot
```

2. Create a virtual environment

```
python -m venv .binance
```

3. Activate the environment

Windows:

```
.binance\Scripts\activate
```

Mac/Linux:

```
source .binance/bin/activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root and add your Binance Testnet API credentials:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

API keys must be generated from:

https://testnet.binancefuture.com

---

## Usage

Run the CLI script with the required arguments.

### Market Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example output:

```
Order Request Summary
----------------------
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.001
Price: Market Price
```

---

### Limit Order Example

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

Example output:

```
Order Request Summary
----------------------
Symbol: BTCUSDT
Side: SELL
Order Type: LIMIT
Quantity: 0.001
Price: 70000
```

---

## Logging

All API requests, responses, and errors are logged to a log file:

```
logs/trading_bot.log
```

Example log entry:

```
2026-03-09 14:10:22 - INFO - Order Request: BTCUSDT BUY MARKET 0.001
2026-03-09 14:10:23 - INFO - Order Response: {...}
```

---

## Assumptions

* The bot interacts only with the Binance Futures Testnet environment.
* Only **USDT-M Futures pairs** are supported.
* Supported order types are **MARKET** and **LIMIT**.

---

## Dependencies

Main libraries used:

* python-binance
* python-dotenv

---

## Author

Saiyyam Agrawal
