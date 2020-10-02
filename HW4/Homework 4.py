import random
import unittest

## Name : Ashwin Surapaneni
## People you worked with : Sreeram Panicker
## Github URL : Didn't work but submitted file

class Customer:
	def __init__(self, name, money = 50):
		self.name = name
		self.money = money
	def deposit_money(self, money_to_add):
		self.money += money_to_add
	def make_payment(self, driver, amount):
		driver.receive_payment(amount)
		self.money = self.money - amount	
	def order_medicine(self, driver, pharmacy, drug_name, quantity):
		if not(driver.know_pharmacy(pharmacy)):
			print("Sorry, this service doesn't deliver from that pharmacy. Please try a different pharmacy!")
		elif self.money < driver.estimated_cost(pharmacy):
			print("Don't have enough money for that :( Please add more money to your account!")
		elif not(pharmacy.has_medicine(drug_name, quantity)):
			print("Our pharmacy has run out of " + drug_name + " :( Please try a different pharmacy!")
		else:
			bill = driver.place_order(pharmacy, drug_name, quantity)
			self.make_payment(driver, bill)
			self.take_medicine()
	def take_medicine(self):
		print("I am starting to feel better!")
	def __str__(self):
		return "Hello! My name is " + self.name + ". I have $" + str(self.money) + " and I need to order some medicine."

class Driver:
	def __init__(self, name, money = 500, pharmacies = [], delivery_fee = 5):
		self.name = name
		self.money = money
		self.pharmacies = pharmacies[:] # makes a copy of the list
		self.delivery_fee = delivery_fee
	def add_pharmacy(self, new_pharmacy):
		self.pharmacies.append(new_pharmacy)
	def receive_payment(self, money):
		self.money += money	
	def estimated_cost(self, pharmacy, quantity):
		return (pharmacy.cost * quantity) + self.delivery_fee
	def place_order(self, pharmacy, drug_name, quantity):
		self.money = self.money - (pharmacy.cost * quantity)
		pharmacy.process_order(drug_name, quantity)
		return self.estimated_cost(pharmacy, quantity)
	def know_pharmacy(self, pharmacy):
		return pharmacy in self.pharmacies

	def __str__(self):
		return "Hello, my name is " + self.name + " I am a Medicine Express driver, who has saved up $" + str(self.money) + ". I charge $" + str(self.delivery_fee) + " and I can deliver from " + str(len(self.pharmacies)) + " pharmacys."

class Pharmacy:
	def __init__(self, name,  inventory, cost = 10, money = 500):
		self.name = name
		self.inventory = inventory
		self.cost = cost 
		self.money = money
	def process_order(self, drug_name, quantity):
		self.inventory = self.inventory - quantity
		self.money += (self.quantity * self.cost)
	def has_medicine(self, drug_name, quantity):
		if self.quantity > 0:
			return True
	def stock_up(self, drug_name, quantity):
		if drug_name not in self.inventory.keys():
			self.inventory[drug_name] = quantity
		else:
			self.inventory[drug_name] =  self.inventory[drug_name] + quantity
	def __str__(self):
		return "Hello, we are" + self.name + ". These are drugs that we currently have in stock" + self.inventory + ". We charge $" + self.cost +" per pill. We have $" + self.money + "in total."
    def test_has_medicine(self):        
        p5 = Pharmacy("Hi", dic = {"tylenol":10, "advil":30, "motrin": 1} , cost = 100, money = 100)
        self.assertEqual(self.p5.has_medicine("tylenol", 10), True)
        self.assertEqual(self.p5.has_medicine("advil", 1), True)
        self.assertEqual(self.p5.has_medicine("motrin" 0), False)
    def test_order_medicine(self):      
        c5 = Customer("Ashwin", 1)
        self.assertEqual(self.c5.order_medicine(self.d1, self.p1, "meijer", 5), "Don't have enough money for that :( Please add more money to your account!")
        self.assertEqual(self.p5.pharmacy.has_medicine("tylenol", 50), True)
        self.assertEqual(self.d1.know_pharmacy(p2), True)
def main():
	diction1 = {"tylenol" : "50", "advil" : "70"}
	diction2 = {"motrin" : "50", "vicodin" : "70"}
	c1 = Customer("zara",75)
	c2 = Customer("jason", 25)
	p1 = Pharmacy("Kroger", diction1, 700, 800)
	p2 = Pharmacy("Meijer", diction2, 100, 300)

	d = Driver("chait", 20, p1, 40)
	d2 = Driver("abhi", 50, p2, 100)
if __name__ == "__main__":
	main()
	print("\n")
	unittest.main(verbosity = 2)