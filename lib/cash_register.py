#!/usr/bin/env python3

class CashRegister:
    
    total = 0
    items = []

    def __init__(self, discount = 0):
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        CashRegister.total += (price * quantity)
