// Copyright (c) 2024, NexTash and contributors
// For license information, please see license.txt

frappe.ui.form.on("Group Product Image", {
	onload(frm) {
      frm.set_query('variation', () => {
      return {
          filters: {
              "parent": frm.doc.product
          }
      }
    })
	},
});
