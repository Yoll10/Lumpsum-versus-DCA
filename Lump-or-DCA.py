import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def lumpsum_or_dca(ticker, start_date, end_date, investment):
    data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)['Close']
    data = data.squeeze().astype(float)
    if data.empty:
        return "Error : No data found."
    
    price_start = data.iloc[0]
    shares_lump = investment/price_start
    end_lump = shares_lump*data.iloc[-1]
    
    monthly_data = data.resample('MS').first().astype(float)
    monthly_investment = investment/len(monthly_data)
    total_dca_shares = 0
    for price in monthly_data:
        total_dca_shares += monthly_investment/price
    end_dca = total_dca_shares*data.iloc[-1]

    perf_lump = (end_lump - investment) / investment
    perf_dca = (end_dca - investment) / investment

    print("")
    print("Results for ", ticker, "from", start_date, "to", end_date)
    print("Total investment :", investment, "€")
    print("Lump Sum :", round(end_lump, 2), "€")
    print("DCA      :", round(end_dca, 2), "€")
    print(f"Rendement Lump Sum : {perf_lump:.2%}")
    print(f"Rendement DCA      : {perf_dca:.2%}")
    if(perf_lump>perf_dca):
        print("In this timeframe, the best strategy was to Lumpsum.")
    elif(perf_lump<perf_dca):
        print("In this timeframe, the best strategy was to DCA.")
    else:
        print("In this timeframe, both strategies gave the same rendment.")

    data.plot(title=ticker)
    plt.ylabel("Price")
    plt.show()

lumpsum_or_dca("NDX", "2022-01-01", "2026-04-19", 10000)
