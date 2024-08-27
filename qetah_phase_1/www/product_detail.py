import frappe

def get_context(context):
    products = frappe.get_all("Product", ["*"] ,filters={"is_featured": 1}, order_by="modified asc")
    context.update({
        "products":products,
    })