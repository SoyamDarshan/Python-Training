# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 02:15:32 2018

@author: soyam

Modify the declaration of the first for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?
"""


class CreditCard:

    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit,balance=0):

        
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
        self._balance = balance

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
            if(amount<0):
                raise ValueError('Amount should be greater than or equal to 0') 
            else:
                self._balance -= amount
                return self._balance
        else:
            raise TypeError('amount should be integer')
            
            
            
            
#            
#if __name__ == '__main__':
#    v=CreditCard('hello','inr','1232132132',435)            
#    print(CreditCard.charge(v,50))
#    print(CreditCard.make_payment(v,15))        
#            
if __name__ == "__main__" :
    wallet = [ ]
    wallet.append(CreditCard( 'John Bowman Sr.' , 'California Savings' ,5391037593875309 , 2500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Federal' ,3485039933951954 , 1500) )
    wallet.append(CreditCard( 'John Bowman Jr.' , 'California Finance' ,5391037593875309 , 5000) )
for val in range(1, 200): 
    if(wallet[0].charge(val*3)==False):
        print('The first to go over its credit limit ',wallet[0].get_customer(),wallet[0].get_balance(),"\n")
        break
    if(wallet[1].charge(val*1)==False):
        print('The first to go over its credit limit ',wallet[1].get_customer(),wallet[1].get_balance(),"\n")     
        break
    if(wallet[2].charge(val*1)==False):
        print('The first to go over its credit limit ',wallet[2].get_customer(),wallet[2].get_balance(),"\n")     
        break


for c in range(3):
    print(' Customer = ', wallet[c].get_customer())
    print(' Bank = ', wallet[c].get_bank())
    print(' Account = ', wallet[c].get_account())
    print(' Limit = ', wallet[c].get_limit())
    print(' Balance = ', wallet[c].get_balance())
    print()
    while wallet[c].get_balance( ) > 100:
        wallet[c].make_payment(100)
        print(' New balance = ', wallet[c].get_balance())
        print()       
                
            