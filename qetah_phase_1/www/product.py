import frappe

def get_context(context):
    # Retrieve filter values from the request
    search_query = frappe.form_dict.get('q', None)
    categories = frappe.form_dict.get('category', [])
    min_price = frappe.form_dict.get('min_price', None)
    max_price = frappe.form_dict.get('max_price', None)
    rating = frappe.form_dict.get('rating', None)
    discounts = frappe.form_dict.get('discount', [])

    # Prepare filters dictionary
    filters = {}

    if search_query:
        filters['name'] = ['like', f'%{search_query}%']  # Adjust the field and filter type based on your needs

    if categories:
        filters['category'] = ['in', categories]

    if min_price and max_price:
        filters['price'] = ['between', [min_price, max_price]]

    if rating:
        filters['rating'] = rating

    if discounts:
        filters['discount'] = ['in', discounts]


    
    id = frappe.form_dict.id
    # context.doc = frappe.get_all('Product', )

    products = frappe.get_all('Product',filters={"name": id})
    products = frappe.get_all('Product',filters=filters , fields=['*'])

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
