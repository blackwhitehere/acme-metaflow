from metaflow import FlowSpec, step, retry, kubernetes, project

def get_minute_data(ticker_symbol, days_back=1):
    """
    Fetch minute-level stock data for a given ticker symbol.
    
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL', 'MSFT')
        days_back (int): Number of trading days to look back (default: 1)
    
    Returns:
        pandas.DataFrame: Minute-level stock data
    """
    import yfinance as yf
    from datetime import datetime, timedelta
    # Create ticker object
    ticker = yf.Ticker(ticker_symbol)
    
    # Calculate start and end dates
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)
    
    # Fetch minute-level data
    # interval options: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h
    df = ticker.history(
        start=start_date,
        end=end_date,
        interval='1m'
    )
    return df


@project(name='acme_landing')
class LandingYfinanceSample(FlowSpec):
    """
    Lands minute resolution OHLC (+ Volume, Dividends, Stock Splits) AAPL data from yfinance.
    """
    @kubernetes(cpu=0.5, memory=128)
    @step
    def start(self):
        print("LandingYfinanceSample is starting.")
        self.next(self.land_data)

    @kubernetes(cpu=0.5, memory=258)
    @retry
    @step
    def land_data(self):
        """
        Fetch data from yfinance.
        """
        self.df = get_minute_data('AAPL', days_back=5)
        self.next(self.end)

    @kubernetes(cpu=0.5, memory=128)
    @step
    def end(self):
        print("LandingYfinanceSample is finished.")


if __name__ == "__main__":
    LandingYfinanceSample()
