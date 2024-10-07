import frappe
def get_context(context):
    
    id = frappe.form_dict.get("product_name")
    varient_name=frappe.form_dict.get("varient_name")
   
    
    products = frappe.get_all('Product',filters={"name": id}, fields=['*'])
    testimonils = frappe.get_all('Testimonial',filters={}, fields=['*'])
    # bigimage = frappe.get_all('Big Images',filters={}, fields=['*'])

    
    for product in products:
        product['variation'] = frappe.get_all("Product Variation",filters={"parent": id,"name":varient_name}, fields=['*'])
        var_images = product['variation'][0].get("product_images")

        if var_images:
            images_doc = frappe.db.sql("""
            SELECT * FROM `tabProduct Images`
            WHERE parent = %(parent)s
            """, {'parent': var_images}, as_dict=True)
            product['variation'][0]["images"] = images_doc
        else:
            product['variation'][0]["images"] = []
        print(var_images) 
        
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