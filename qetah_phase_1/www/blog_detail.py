import frappe

def get_context(context):
    blogs = frappe.get_all("Blog Post", filters={"custom_is_featured": 1}, fields=["*"]
    )
    context.update({
        "blogs": blogs
    })