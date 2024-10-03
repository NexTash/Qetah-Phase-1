import frappe
import re
import copy

def get_context(context):
    carts = frappe.get_all('Cart Items', fields=['*'])
    products = frappe.get_all('Product', fields=['*'])
    for product in products:
        product['variations'] = frappe.get_all(
            'Product Variation', 
            fields=['*'],
            filters={'parent': product['name']} 
        )
    product_list=[]
    for product in products:
        print(product)
        doc = product
        for variation in product.variations:
            desc = variation.description
            desc_arabic = variation.description_arabic
            variation.desc = re.sub(r'<.*?>', '', desc).strip()
            variation.desc_arabic = re.sub(r'<.*?>', '', desc_arabic).strip()
            
            doc["variations"]=[]
            doc["variations"]=variation
            product_list.append(copy.deepcopy(doc))
        
    context.update({
        "products": product_list,
        "carts":carts
    })

    return context