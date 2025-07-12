// Copyright (c) 2025, Santha Ashwin and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airplane Ticket', {
    refresh(frm) {  
        if (!frm.is_new() && frm.doc.docstatus < 1) {
            frm.add_custom_button('Assign Seat', () => {
                frappe.prompt([
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ], (values) => {
                    // Set the seat field with the value from dialog
                    frm.set_value('seat', values.seat_number);
                }, 'Assign Seat');
            });
        }
    }
});
