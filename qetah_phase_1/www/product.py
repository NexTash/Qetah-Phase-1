import frappe

def get_context(context):
    q = frappe.form_dict.q
    min_price = frappe.form_dict.min_price
    max_price = frappe.form_dict.max_price
    ratings = frappe.form_dict.ratings
    
    id = frappe.form_dict.id
    # context.doc = frappe.get_all('Product', )

    products = frappe.get_all('Product',filters={"name": id})
    products = frappe.get_all('Product',filters={} , fields=['*'])

    for product in products:
        product['variations'] = frappe.get_all(
            'Product Variation', 
            fields=['*'],
            filters={'parent': product['name']} 
        )
        
       
        product['images'] = frappe.get_all(
            'Product Images',  
            fields=['*'],
            filters={'parent': product['name']}  
        )




    context.update({
        "products": products
    })
