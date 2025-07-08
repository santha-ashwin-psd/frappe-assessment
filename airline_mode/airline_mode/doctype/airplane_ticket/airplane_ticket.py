# Copyright (c) 2025, Santha Ashwin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
	def before_insert(self):
		self.populate_seat()
	def validate(self):
		b=[]
		for i in self.add_ons:
			b.append(i.item)
		for j in b:
			c = b.count(j)
			if c > 1 :
				frappe.throw("You can't buy the same item twice")
	def before_save(self):
		total=0
		for i in self.add_ons:
			total += i.amount
		self.total_price = self.flight_price + total
	def before_submit(self):
		if self.status == "Boarded":
			pass
		else:
			frappe.throw("You can't submit without boarded")
	def populate_seat(self):
		ran_no = random.randint(10,99)
		ran_let = random.choice(["A","B","C","D","E","F"])
		self.seat = f"{ran_no}{ran_let}"