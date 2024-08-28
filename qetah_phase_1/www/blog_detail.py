import frappe

def get_context(context):
    id = frappe.form_dict.get("id")

    blogs = frappe.get_all("Blog Post", filters={"custom_is_featured": 1, "name": id}, fields=["*"]
    )
    context.update({
        "blogs": blogs
    })