import frappe

def get_context(context):
    blog_id = frappe.form_dict.id
    context.doc = frappe.get_all("Blog Post", blog_id)
    
    blogs = frappe.get_all("Blog Post", filters={}, fields=["*"]
    )

    context["blogs"] = blogs
    return context
