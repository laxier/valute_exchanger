#CurrencyConverter.py
#Scrypted by: Laxier

import json
import requests
def first(dol):
    # gets RUB from USD
    return(dol * float(rate["RUB"]) / float(rate["USD"]))
def second(rub):
    # gets USD from RUB
    return(rub / float(rate["RUB"]) * float(rate["USD"]))
response = requests.get("https://api.exchangeratesapi.io/latest")
rate = response.json()['rates']
print("Hello! This is a Currency Converter")
print("What wold you like to convert?")
print("1 - dollar to rubble")
print("2 - rubble to dollar")
choice = input("> ")
currency = float(input("enter the ammount of money> "))
if(choice == "1"):
    print("{:.2f} RUB".format(first(currency)))
elif(choice == "2"):
    print("{:.2f} USD".format(second(currency)))
else: print("ERROR please try again.")
