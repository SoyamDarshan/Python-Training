# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 02:00:59 2018

@author: soyam


Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter

BASICALLY ASKING FOR AN EXCEPTION HANDLING SYNTAX TO CHECK FOR INTEGER VALUE

"""

class CreditCard:

    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):

        
        """Create a new credit card instance.
        The initial balance is zero.
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank s name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self,price):
        """Charge given price to the card, assuming sufficient credit limit.

	 Return True if charge was processed; False if charge was denied.
	 """
        if type(price)==int:
            if price + self._balance > self._limit: # if charge would exceed limit,
                return False # cannot accept charge
            else:
                self._balance += price
                return True
        else:
            raise TypeError("price should be integer")
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if type(amount)==int:
            self._balance -= amount
            return self._balance
        else:
            raise TypeError('amount should be integer')
            
            
            
            
            
if __name__ == '__main__':
    v=CreditCard('hello','inr','1232132132',435)            
    print(CreditCard.charge(v,50))
    print(CreditCard.make_payment(v,16.0))        
            
            
            
            
          
            
            
            
            
            
            
            