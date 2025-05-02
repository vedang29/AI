from experta import *

# Define the Stock Fact
class Stock(Fact):
    """Stock details"""
    name: str
    current_price: float
    pe_ratio: float
    volatility: str  # high, medium, low
    trend: str       # bullish, bearish, sideways
    sector: str
    risk_tolerance: str  # low, medium, high
    holding: bool    # already holding the stock or not

# Expert System for Stock Trading
class StockTradingAdvisor(KnowledgeEngine):

    @Rule(Stock(trend='bullish', pe_ratio=P(lambda x: x < 25), volatility='low',
                risk_tolerance='low', holding=False))
    def buy_low_risk_stock(self):
        print("Advice: BUY the stock - Low-risk bullish opportunity with good valuation.")

    @Rule(Stock(trend='bullish', pe_ratio=P(lambda x: x < 40), volatility='high',
                risk_tolerance='high', holding=False))
    def buy_aggressive_stock(self):
        print("Advice: BUY the stock - High potential for return, suitable for high-risk appetite.")

    @Rule(Stock(trend='bearish', holding=True))
    def sell_on_downtrend(self):
        print("Advice: SELL the stock - Market is bearish and you're holding the stock.")

    @Rule(Stock(trend='sideways', holding=True))
    def hold_in_uncertainty(self):
        print("Advice: HOLD the stock - No clear trend, wait for a signal.")

    @Rule(Stock(trend='bullish', holding=True))
    def hold_during_bull_run(self):
        print("Advice: HOLD the stock - Already in a bullish trend, ride the wave.")

    @Rule(Stock(pe_ratio=P(lambda x: x > 50), volatility='high', risk_tolerance='low'))
    def avoid_overvalued_stock(self):
        print("Advice: AVOID the stock - Highly volatile and overvalued, not suitable for low risk tolerance.")

    @Rule(Stock(volatility='medium', trend='bullish', risk_tolerance='medium'))
    def moderate_buy(self):
        print("Advice: BUY the stock - Balanced risk and good growth potential.")

# Run function
def run_trading_expert():
    engine = StockTradingAdvisor()
    engine.reset()
    
    print("\n--- Enter Stock Details ---")
    name = input("Stock Name: ")
    current_price = float(input("Current Price: "))
    pe_ratio = float(input("P/E Ratio: "))
    volatility = input("Volatility (low/medium/high): ").lower()
    trend = input("Market Trend (bullish/bearish/sideways): ").lower()
    sector = input("Sector: ")
    risk_tolerance = input("Your Risk Tolerance (low/medium/high): ").lower()
    holding = input("Are you currently holding this stock? (yes/no): ").lower() == "yes"

    engine.declare(Stock(
        name=name,
        current_price=current_price,
        pe_ratio=pe_ratio,
        volatility=volatility,
        trend=trend,
        sector=sector,
        risk_tolerance=risk_tolerance,
        holding=holding
    ))

    print("\n🔍 Analyzing Market Conditions...\n")
    engine.run()

if __name__ == "__main__":
    run_trading_expert()
