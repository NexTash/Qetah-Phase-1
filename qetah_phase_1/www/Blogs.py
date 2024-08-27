import frappe

def get_context(context):
    blog_id = frappe.form_dict.id
    context.doc = frappe.get_all("Blog Post", blog_id)
    
    related_blogs = frappe.get_all("Blog Post", filters={}, fields=["*"]
    )

    context["blogs"] = related_blogs
    return context
