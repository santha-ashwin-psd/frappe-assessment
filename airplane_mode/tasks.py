import frappe

def send_rent_reminders():
    if not frappe.db.get_single_value("Airplane Mode Settings", "enable_rent_reminders"):
        return

    tenants = frappe.get_all("Tenant", filters={"email": ["!=", ""]}, fields=["name", "email"])
    for tenant in tenants:
        frappe.sendmail(
            recipients=[tenant.email],
            subject="Monthly Rent Due Reminder",
            message=f"Dear {tenant.name},\n\nThis is a reminder that your monthly shop rent is due. Please make the payment at the earliest.\n\nRegards,\nAirport Management Team"
        )
