# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:50:28 2024

@author: User
"""

class CurrencyConverter:
    def __init__(self):
        # Define exchange rates manually (replace with current rates)
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.75,
            'JPY': 110.0,
            # Add more currencies and rates as needed
        }

    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            print("Invalid currency code. Please check your input.")
            return None

        rate_from = self.exchange_rates[from_currency]
        rate_to = self.exchange_rates[to_currency]

        converted_amount = round(amount * (rate_to / rate_from), 2)
        return converted_amount

if __name__ == "__main__":
    converter = CurrencyConverter()

    print("Welcome to the Simple Currency Converter!")

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    converted_amount = converter.convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"\n{amount} {from_currency} is approximately equal to {converted_amount} {to_currency}")
