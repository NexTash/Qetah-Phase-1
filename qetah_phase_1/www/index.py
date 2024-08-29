import frappe

def get_context(context):
    blogs = frappe.get_all("Blog Post", filters={"custom_is_featured": 1}, fields=["*"])
    testimonials = frappe.get_all("Testimonial", ["*"] ,filters={"featured": 1})
    products = frappe.get_all("Product", ["*"] ,filters={"is_featured": 1}, order_by="modified asc")
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
        "blogs": blogs,
        "products":products,
        "testimonials":testimonials,
    })