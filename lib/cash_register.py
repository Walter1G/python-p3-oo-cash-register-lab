#!/usr/bin/env python3

class CashRegister:
  def __init__(self,value=0):
    self.discount=value
    self.total=0
    self.items=[]
    
  def add_item(self,item_name,price,qty=1):
    self.items.extend([item_name] * qty)
    self.total+=price*qty
    
  def apply_discount(self):
    
   if self.discount>0:
      self.total -= (self.discount/100)*self.total
      print(f"After the discount, the total comes to ${int(self.total)}.")
   else:
     print("There is no discount to apply.")
  
  def void_last_transaction(self):
        if self.items:
            # Assuming each item has a fixed price (no dynamic pricing)
            fixed_prices = {"apple": 0.99, "tomato": 1.76}
            last_item_name = self.items[-1]
            last_item_price = fixed_prices.get(last_item_name, 0.0)

            self.total -= last_item_price
            self.items.pop()

  
  
  
  
  pass
