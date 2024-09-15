import frappe
  
@frappe.whitelist(allow_guest=True)

def get_latest_order_summary():
    # Fetch the latest 'Delivery Information' record
    latest_delivery = frappe.db.sql("""
        SELECT * FROM `tabDelivery Information` 
        ORDER BY creation DESC 
        LIMIT 1
    """, as_dict=True)

    if latest_delivery:
        latest_delivery = latest_delivery[0]
        # Fetch associated 'Order Items' for the latest 'Delivery Information' record
        latest_delivery['order_items'] = frappe.get_all(
            'Order Items',
            fields=['*'],
            filters={'parent': latest_delivery['name']}
        )
        return latest_delivery  # Return the latest delivery info and items
    else:
        return None  # Handle case where no records exist