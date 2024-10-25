import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    '''
    # Simple stock Price App
    
    Shown are the stock closing price and volume of Google!
    '''
)

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices for this ticker (note: removed 'period' argument)
tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2024-05-31')

# Display stock closing price and volume using line charts
st.line_chart(tickerDf['Close'])
st.line_chart(tickerDf['Volume'])
