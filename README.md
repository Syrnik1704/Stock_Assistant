# Stock_Assistant
`Authors`  | Marcin Krawiec, Konrad Syrnik
------------- | -------------
`Subject`  | Języki Programowania Wysokiego Poziomu

Stock Assistant as an application that allows a user to create and analyse a fictional portfolio with real stock market data without taking a real investment risk.
It also provides plots and reports that base on historical data and allow long term market analysis.
In times of high inflation, it is resonable to look for various investment possibilities and compere them in terms od potencial profit and risk. And this is where our application comes in handy!
Addictionaly it allows the user to deepen knowledge about the stock market, understand its main mechanisms and give confidence before taking a real investment.

## Features
Stock Assistant provides various features.
User can access historical data of multiple stock tickers and cryptos and see various plot types:
- Line plots that show open and close prices, but also bollinger bands which are a profesional indicator wheter to sell or buy an asset. 
- Candlestick plots that not only show open and close prices but also low and high prices. Bollinger bands are also provided. Candlestick plots are commonly known and fully proffesional.
- RSI (Relative Strength Index) plots, which are another indicator wheter to sell or buy an asset.
- Correlation bar plots that show the degree to which two stock tickers or cryptos move in relation to each other

User can also create a financial portfolio with multiple components and edit it if the solution for increase of portfolio returns is found. 
Portfolio can also be analysed. The user is provided with:
- Table in which all the components and profit/loss are listed.
- Cumulative returns line plot that shows the growth of each 1$ invested into portfolio.
- Correlation values and matrix for all the components.
- Volatility values that are used to masure the risk.
- Share ratio value and optimization with efficient frontier plot and weights plot.

Finally user is also provided with currencies plots and bond returns analysis in which different bond investments options can be checked.

## Modules
- yfinance
- pyqt5
- mysql
- plotly

## Links
- https://www.tutorialspoint.com/pyqt5/pyqt5_hello_world.html
- https://doc.qt.io/qt-5/classes.html
- https://www.riverbankcomputing.com/static/Docs/PyQt5/
- https://pypi.org/project/yfinance/
- https://analyzingalpha.com/yfinance-python
- https://algotrading101.com/learn/yfinance-guide/
- https://pypi.org/project/yfinance/
