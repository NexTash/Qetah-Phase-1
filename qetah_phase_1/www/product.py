import frappe

def get_context(context):
    search_query = frappe.form_dict.get('q', None)
    categories = frappe.form_dict.get('category', [])
    min_price = frappe.form_dict.get('min_price', None)
    max_price = frappe.form_dict.get('max_price', None)
    rating = frappe.form_dict.get('rating', None)
    discounts = frappe.form_dict.get('discount', [])
    id = frappe.form_dict.get('id', None)

    filters = []
    values = {}

    # Handling search query
    if search_query:
        filters.append("name LIKE %(search_query)s")
        values['search_query'] = f"%{search_query}%"

    # Handling categories
    if categories:
        filters.append("category IN %(categories)s")
        values['categories'] = categories.split(",")
    
    # Handling discounts
    if discounts:
        filters.append("discount IN %(discounts)s")
        values['discounts'] = discounts.split(",")

    # Handling price range
    if min_price and max_price:
        filters.append("price BETWEEN %(min_price)s AND %(max_price)s")
        values['min_price'] = int(min_price)
        values['max_price'] = int(max_price)

    # Handling rating
    if rating:
        filters.append("rating = %(rating)s")
        values['rating'] = rating

    # Handling specific product id
    if id:
        filters.append("name = %(id)s")
        values['id'] = id

    # Construct the SQL query
    where_clause = " AND ".join(filters) if filters else "1 = 1"

    # # # Debugging
    # frappe.throw(f"""
    #     SQL Query: SELECT * FROM `tabProduct` WHERE {where_clause}
    #     Values: {values}
    # """)

    products = frappe.db.sql(f"""
        SELECT * FROM `tabProduct`
        WHERE {where_clause}
    """, values, as_dict=True)

    # Fetch variations and images for each product
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

    context.update({
        "products": products
    })
