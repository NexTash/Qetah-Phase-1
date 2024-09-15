import frappe

def get_context(context):
    # Fetch the latest 'Delivery Information' record, which could include the one created in runtime
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
        context.latest_delivery = latest_delivery  # Pass the latest delivery info and items to the context
    else:
        context.latest_delivery = None  # Handle case where no records exist
    
    return context

