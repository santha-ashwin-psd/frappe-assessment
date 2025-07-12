import frappe

def execute():
    tickets = frappe.db.get_list("Airplane Ticket",plunk="name")
    for t in tickets:
        ticket = frappe.get_doc("Airplane Ticket",t)
        ticket.populate_seat()
        ticket.save()

    frappe.db.commit()