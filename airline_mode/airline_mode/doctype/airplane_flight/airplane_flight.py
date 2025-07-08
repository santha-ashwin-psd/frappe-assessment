# Copyright (c) 2025, Santha Ashwin and contributors
# For license information, please see license.txt

#import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname


class AirplaneFlight(WebsiteGenerator):
	def before_submit(self):
		self.status = "Completed"