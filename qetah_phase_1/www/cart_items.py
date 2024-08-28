import frappe

def get_context(context):
    products = frappe.get_all('Product', fields=['*'])
    for product in products:
        product['cart_items'] = frappe.get_all(
            'Cart Items', 
            fields=['*'],
            filters={'parent': product['name']} 
        )
        product['variations'] = frappe.get_all(
            'Product Variation', 
            fields=['*'],
            filters={'parent': product['name']} 
        )
        
    context.products = products

    return context