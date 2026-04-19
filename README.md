# 📈 Investment Simulator: Lump Sum vs. DCA

This Python project compares two popular investment strategies—**Lump Sum** and **Dollar Cost Averaging (DCA)**—using real-world historical data from Yahoo Finance.

## 🧐 The Concept

The goal is to determine which strategy would have been more profitable for a specific asset over a given time period:
* **Lump Sum (LS):** Investing the entire capital immediately on Day 1.
* **Dollar Cost Averaging (DCA):** Dividing the capital into equal monthly installments to smooth out market volatility.

## 🚀 Features

* **Real-time Data:** Fetches historical price data automatically via the `yfinance` API.
* **Smart Calculations:** Computes final portfolio value and total return percentage (%) for both methods.
* **Volatility Analysis:** Demonstrates how "buying the dip" during DCA affects the average share price.
* **Data Visualization:** Generates an interactive price chart using `matplotlib`.

## 🛠️ Installation

Ensure you have Python installed, then install the required dependencies:

```bash
pip install pandas yfinance matplotlib
