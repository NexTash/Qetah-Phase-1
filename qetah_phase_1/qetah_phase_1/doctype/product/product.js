frappe.ui.form.on('Product', {
    refresh: function(frm) {
    }
});

frappe.ui.form.on('Product Variation', {
    item_code: function(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        frappe.db.get_value('Bin', { item_code: row.item_code }, ['warehouse', 'stock_value'])
        .then((result) => {
            if (result && result.message) {
                row.warehouse = result.message.warehouse;
                row.remaining_items = result.message.stock_value;
                frm.refresh_field('variations');
            } else {
                console.error('No Bin document found for item code:', row.item_code);
            }
        })
    }
});
