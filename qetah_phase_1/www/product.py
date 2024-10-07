import frappe
import re
import copy

def get_context(context):
    search_query = frappe.form_dict.get('q', None)

    collections = frappe.form_dict.get('collections', '').split(',')
    collections = [collection.replace(" Collection", "") for collection in collections]
    min_price = frappe.form_dict.get('min_price', None)
    max_price = frappe.form_dict.get('max_price', None)
    rating = frappe.form_dict.get('rating', None)
    discounts = frappe.form_dict.get('discount', [])
    id = frappe.form_dict.get('id', None)

    filters = []
    values = {}

    if search_query:
        filters.append("name LIKE %(search_query)s")
        values['search_query'] = f"%{search_query}%"
   
    if discounts:
        filters.append("discount IN %(discounts)s")
        values['discounts'] = discounts.split(",")

    if min_price and max_price:
        filters.append("price BETWEEN %(min_price)s AND %(max_price)s")
        values['min_price'] = int(min_price)
        values['max_price'] = int(max_price)

    if rating:
        filters.append("rating = %(rating)s")
        values['rating'] = rating

    if id:
        filters.append("name = %(id)s")
        values['id'] = id

    
    where_clause = " AND ".join(filters) if filters else "1 = 1"

    # # # Debugging
    # frappe.throw(f"""
    #     SQL Query: SELECT * FROM `tabProduct` WHERE {where_clause}
    #     Values: {values}
    # """)

    collection = frappe.db.sql(f"""
        SELECT * FROM `tabProduct Collection`
        WHERE disable = 0
        """, values, as_dict=True)

    products = frappe.db.sql(f"""
        SELECT * FROM `tabProduct`
        WHERE {where_clause}
    """, values, as_dict=True)

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
    if collections[0] is not "":  
        for product in products:
            doc = product
            for variation in product.variations:
                if len(collections)>0:
                    if "product_collection" in variation:
                        if variation.product_collection != "" and variation.product_collection in collections :   
                            desc = variation.description
                            desc_arabic = variation.description_arabic
                            variation.desc = re.sub(r'<.*?>', '', desc).strip()
                            variation.desc_arabic = re.sub(r'<.*?>', '', desc_arabic).strip()
                            
                            doc["variations"]=[]
                            doc["variations"]=variation
                            product_list.append(copy.deepcopy(doc))
    else:
        for product in products:
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
        "collection":collection
    })
