import frappe

@frappe.whitelist()
def get_delivery_details(product_name):
    # Fetch the Product document based on the name
    product = frappe.get_doc("Product", product_name)
    
    # Extract the delivery fee and discount from the product document
    delivery_fee = product.delivery_fee  # Adjust field names if needed
    delivery_discount = product.delivery_discount  # Adjust field names if needed

    return {
        'deliveryFee': delivery_fee,
        'deliveryDiscount': delivery_discount
    }
