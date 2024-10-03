import frappe

def get_context(context):
    
    id = frappe.form_dict.get("product_name")
    varient_name=frappe.form_dict.get("varient_name")
   
    
    products = frappe.get_all('Product',filters={"name": id}, fields=['*'])
    testimonils = frappe.get_all('Testimonial',filters={}, fields=['*'])
    # bigimage = frappe.get_all('Big Images',filters={}, fields=['*'])

    
    for product in products:
        product['variation'] = frappe.get_all("Product Variation",filters={"parent": id,"name":varient_name}, fields=['*']) 
        product['variations'] = frappe.get_all("Product Variation",filters={"parent": id}, fields=['*']) 

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