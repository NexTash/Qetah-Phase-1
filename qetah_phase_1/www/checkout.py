import frappe
from frappe.utils import formatdate

def get_context(context):
    products = frappe.get_all('Product', fields=['*'])

    # Convert datetime fields to string for each product
    for product in products:
        if 'creation' in product:
            product['creation'] = product['creation'].strftime('%Y-%m-%d %H:%M:%S')
        if 'modified' in product:
            product['modified'] = product['modified'].strftime('%Y-%m-%d %H:%M:%S')
    
    context.update({
        "products": products,
    })
