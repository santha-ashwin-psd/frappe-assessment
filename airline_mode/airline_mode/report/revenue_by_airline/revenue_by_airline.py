# Copyright (c) 2025, Santha Ashwin and contributors
# For license information, please see license.txt

# import frappe

import frappe
from frappe.query_builder import DocType
from frappe.query_builder.functions import Sum, Coalesce
from pypika import Order

def execute(filters=None):
    Ticket = DocType("Airplane Ticket")
    Flight = DocType("Airplane Flight")
    Plane = DocType("Airplane")
    Airline = DocType("Airline")

    revenue_expr = Coalesce(Sum(Ticket.total_price), 0)

    query = (
        frappe.qb
        .from_(Airline)
        .left_join(Plane).on(Plane.airline == Airline.name)
        .left_join(Flight).on(Flight.airplane == Plane.name)
        .left_join(Ticket).on(Ticket.flight == Flight.name)
        .select(
            Airline.name.as_("airline"),
            revenue_expr.as_("revenue")
        )
        .groupby(Airline.name)
        .orderby(revenue_expr, order=Order.desc)
    )

    data = query.run(as_dict=True)

    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
    ]

    total_revenue = sum(row["revenue"] for row in data)

    chart = {
        "data": {
            "labels": [row["airline"] for row in data],
            "datasets": [{"values": [row["revenue"] for row in data]}]
        },
        "type": "donut"
    }

    summary = [
        {"label": "Total Revenue", "value": total_revenue, "indicator": "green"}
    ]

    return columns, data, None, chart, summary

