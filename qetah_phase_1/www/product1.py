import frappe

def get_context(context):

    q = frappe.form_dict.q
    min_price = frappe.form_dict.min_price
    max_price = frappe.form_dict.max_price
    order_by = frappe.form_dict.order_by
    ratings = frappe.form_dict.ratings


    sql_query = """
        SELECT *
        FROM `tabFreelancers`
        WHERE 1=1
    """

    # Construct the WHERE clause based on filters
    if min_price and max_price:
        sql_query += f" AND `hourly_rate` BETWEEN '{min_price}' AND '{max_price}'"
    if q:
        sql_query += f" AND `title` LIKE '%{q}%'"
    if ratings:
        sql_query += f" AND `ratings` >= '{ratings}'"
    if order_by == "oldest":
        sql_query += " ORDER BY `creation` ASC"
    elif order_by == "latest" :
        sql_query += " ORDER BY `creation` DESC"

    # Execute the SQL query
    freelancers = frappe.db.sql(sql_query, as_dict=True)
    context["freelancers"] = freelancers
    parent_docs = frappe.get_all('Category', filters={'is_child': 0}, fields=["*"])
    child_docs = frappe.get_all('Category', filters={'is_child': 1}, fields=["*"])
    
    context['category'] = parent_docs
    context['child_category'] = child_docs
    return context
