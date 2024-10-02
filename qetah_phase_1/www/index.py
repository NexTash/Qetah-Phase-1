import frappe
import re
import copy

def get_context(context):
    blogs = frappe.get_all("Blog Post", filters={"custom_is_featured": 1}, fields=["*"])
    testimonials = frappe.get_all("Testimonial", ["*"] ,filters={"featured": 1})

    products = frappe.db.sql(f"""
        SELECT * FROM `tabProduct`
        WHERE is_featured=1        
        """, as_dict=True)

    for product in products:
        product_name = product['name']
        
        product['variations'] = frappe.db.sql("""
            SELECT * FROM `tabProduct Variation`
            WHERE parent = %(parent)s
        """, {'parent': product_name}, as_dict=True)
        
        product['images'] = frappe.db.sql("""
            SELECT * FROM `tabProduct Images`
            WHERE parent = %(parent)s
        """, {'parent': product_name}, as_dict=True)
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
        "blogs": blogs,
        "testimonials":testimonials,
    })
