# Copyright (c) 2025, Santha Ashwin and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def validate(self):
		self.full_name = f"{self.first_name} {self.last_name}"
