# Stock Trading Expert System using Experta

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


# Airline Cargo Management Expert System using Experta

# from experta import *

# class Flight(Fact):
#     """Flight details"""
#     flight_id: str
#     aircraft_type: str
#     available: bool
#     pilot_available: bool
#     destination: str

# class Cargo(Fact):
#     """Cargo details"""
#     cargo_id: str
#     weight: float
#     category: str  # e.g., perishable, fragile, standard
#     priority: str  # high, medium, low
#     destination: str

# # Define the Expert System
# class AirlineExpertSystem(KnowledgeEngine):

#     @Rule(Cargo(weight=P(lambda x: x > 10000)))
#     def reject_heavy_cargo(self):
#         print("Cargo rejected: Weight exceeds limit (10,000kg).")

#     @Rule(
#         Flight(available=True, pilot_available=True, destination=MATCH.dest),
#         Cargo(destination=MATCH.dest, priority='high')
#     )
#     def schedule_high_priority(self, dest):
#         print(f"High priority cargo scheduled to {dest} on available flight.")

#     @Rule(
#         Flight(available=True, pilot_available=True, destination=MATCH.dest),
#         Cargo(destination=MATCH.dest, category='perishable')
#     )
#     def schedule_perishable(self, dest):
#         print(f"Perishable cargo assigned to next available flight to {dest}.")

#     @Rule(
#         Flight(available=True, pilot_available=True, destination=MATCH.dest),
#         Cargo(destination=MATCH.dest)
#     )
#     def schedule_standard(self, dest):
#         print(f"Standard cargo scheduled to {dest}.")

#     @Rule(Flight(available=False))
#     def no_flight(self):
#         print("No flight available currently.")

#     @Rule(Flight(pilot_available=False))
#     def no_pilot(self):
#         print("No pilot available for the flight.")

# # Function to get user input and run the system
# def run_system():
#     engine = AirlineExpertSystem()
#     engine.reset()

#     print("\nEnter Flight Details")
#     flight_id = input("Flight ID: ")
#     aircraft_type = input("Aircraft Type: ")
#     available = input("Is Flight Available? (yes/no): ").lower() == 'yes'
#     pilot_available = input("Is Pilot Available? (yes/no): ").lower() == 'yes'
#     destination = input("Destination: ")

#     flight_fact = Flight(
#         flight_id=flight_id,
#         aircraft_type=aircraft_type,
#         available=available,
#         pilot_available=pilot_available,
#         destination=destination
#     )
#     print(f"Declaring Flight Fact: {flight_fact}")
#     engine.declare(flight_fact)

#     print("\nEnter Cargo Details")
#     cargo_id = input("Cargo ID: ")
    
#     # Input validation for weight
#     while True:
#         try:
#             weight = float(input("Weight (in kg): "))
#             if weight <= 0:
#                 raise ValueError("Weight must be a positive number.")
#             break
#         except ValueError as e:
#             print(e)

#     category = input("Category (perishable/fragile/standard): ").lower()
#     priority = input("Priority (high/medium/low): ").lower()
#     cargo_destination = input("Destination: ")

#     cargo_fact = Cargo(
#         cargo_id=cargo_id,
#         weight=weight,
#         category=category,
#         priority=priority,
#         destination=cargo_destination
#     )
#     print(f"Declaring Cargo Fact: {cargo_fact}")
#     engine.declare(cargo_fact)

#     print("\nRunning Expert System...\n")
#     try:
#         engine.run()
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     run_system()


