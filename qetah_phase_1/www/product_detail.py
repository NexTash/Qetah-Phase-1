import frappe

def get_context(context):
    
    id = frappe.form_dict.get("id")
    min_price = frappe.form_dict.min_price
    max_price = frappe.form_dict.max_price
    ratings = frappe.form_dict.ratings
    
    products = frappe.get_all('Product',filters={"name": id}, fields=['*'])
    testimonils = frappe.get_all('Testimonial',filters={}, fields=['*'])
    # bigimage = frappe.get_all('Big Images',filters={}, fields=['*'])

    
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
    print(products)
    context.update({
        "products": products,
        "testimonils": testimonils,
    })