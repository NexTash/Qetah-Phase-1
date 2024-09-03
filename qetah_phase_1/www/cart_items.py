import frappe

def get_context(context):
    carts = frappe.get_all('Cart Items', fields=['*'])
    products = frappe.get_all('Product', fields=['*'])
    for product in products:
        product['variations'] = frappe.get_all(
            'Product Variation', 
            fields=['*'],
            filters={'parent': product['name']} 
        )
        
    context.products = products
    context.carts = carts

    return context