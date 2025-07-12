# Copyright (c) 2025, Santha Ashwin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LeaseContract(Document):
    def on_submit(self):
        if not self.shop or not self.tenant:
            frappe.throw("Shop and Tenant must be selected.")

        # Fetch the Shop document
        shop_doc = frappe.get_doc("Shop", self.shop)

        # Mark it as occupied and assign tenant
        shop_doc.is_occupied = 1
        shop_doc.tenant = self.tenant
        shop_doc.save()
