// Copyright (c) 2025, Santha Ashwin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane", {
	refresh(frm) {
        const isAirportAuthority = frappe.user.has_role("Airport Authority Personnel");

        frm.set_df_property('initial_audit_completed', 'hidden', !isAirportAuthority);
        frm.set_df_property('initial_audit_completed', 'read_only', !isAirportAuthority);
	},
});
