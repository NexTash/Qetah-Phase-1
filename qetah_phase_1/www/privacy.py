import frappe

def get_context(context):
    privacy = frappe.get_doc("Policy", ["*"])
    context.update({
        "privacy": privacy,
    })
