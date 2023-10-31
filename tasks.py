# 3
# Create 3 functions, that are related to each other (one is being called in another), 
# and test all logger severity levels by your own design.

# import logging

# Configure the logging module
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w')

# def check_engine() -> None:
#     logging.info("Checking the engine...")
   
# def start_car() -> None:
#     logging.warning("Starting the car...")
#     check_engine()
   
# def drive_car() -> None:
#     logging.error("Driving the car...")
#     start_car()
    
# if __name__ == '__main__':
#     logging.debug("Main program is starting")
#     drive_car()
#     logging.critical("Main program finished driving the car")

# import logging
# import time

# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w')

# def consume_gas_level(starting_level: int = 50, engine_runing: bool = False) -> int:
#     if engine_runing:
#         logging.info(f"Consumin gas at this {starting_level} level")
#         return starting_level - 5
#     else:
#         logging.critical("Car cant consume gas, beciuse turned off")
#         raise ValueError("Engine is not runningcant consume gas")


   
# def car_toggle_switch(state: bool = False) -> bool:
#     if state:
#         logging.debug("Car was turned on")
#         print("Engine is on")
#     else:
#         logging.debug("Car was turned off")
#         print("Engin is shuting down")
#     return state

   
# def drive() -> None:
#     car_state = car_toggle_switch(True)
#     gas_level = 30
#     logging.debug(f"Car has {gas_level}% of fuel")
#     while gas_level > 0:
#        message = (f"Wroom, wroom, I have left {gas_level} in tank")
#        gas_level = consume_gas_level(gas_level, car_state)
#        print(message)
#        time.sleep(1)
#     print( "Out of the gas")   
#     car_state = car_toggle_switch(False)   

# drive()
 

# 4
# Create a program that takes 4 data types/structures: strings, numbers, list, dict. 
# Iterate 10 times with inputs and log what data type/structure and how many times was entered. 
# Handle all possible errors and log it.

# 5
# Setup accounting software , that would take annual income , expenses , 
# VAT rate (all values must be floats) and calculate profit, paid taxes 
# in 4 different currencies (USD, EU, JPY, CNY). 
# All calculations and results should be printed on screen. 
# All data and possible errors must be logged to a file.

import logging
from typing import List
import requests

API_KEY = "akdhflsadhflasfljssl"

logging.basicConfig(level=logging.DEBUG, filename='vmi.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def get_expenses() -> List[float]:    
    paid = []    
    while True:        
        expen = input("Please enter your expenses: ")
        if expen.isnumeric():
            paid.append(float(expen))            
            logging.debug(f"Expences entered: {expen}")        
        else:
            logging.debug(f"Expences in total entered: {paid}") 
            logging.debug(f"Sum of expences: {sum(paid)}")
            print(f"Sum of expences: {sum(paid)}")
            return sum(paid)
        

def get_anual_income()-> float:
    anual_income = input("Please enter your anual income: ")    
    if anual_income.isnumeric():
        return float(anual_income)   
    else:        
        raise ValueError("Bad value antered")
        
        
def calculate_profit(income: float, expenses: float, vat: int) -> float:    
    ebita = income - expenses    
    profit = ebita * (100 - vat) / 100    
    logging.info(f"The profit is: {profit}")    
    return profit


def exchange_curency(value: float, curency: str) -> float:    
    curency_rate = get_curency_exchange_rate(curency)    
    logging.info(f"Exchange rate for {curency}: {curency_rate}")    
    return value * curency_rate


def get_curency_exchange_rate(name: str) -> float:    
    result = requests.get(f"http://data.fixer.io/api/latest?access_key={API_KEY}&symbols={name}")    
    logging.info(f"Respond from API: {result.json()}")    
    if not result.json()["success"]:        
        raise ValueError("Please specify curency code")        
    return result.json()["rates"][name]

expences = get_expenses()
anual_income = get_anual_income()
requested_curency = input("Please enter curency name USD, EU, JPY, CNY: ")
profit = calculate_profit(anual_income, expences, 15)

try:    
    cur = exchange_curency(profit, requested_curency)    
    print(cur)
except ValueError:    
    print("Bad exchange code name")