import frappe

@frappe.whitelist()
def contacts(fullname,email,phone,message):
    doc = frappe.new_doc("Contact us")
    doc.full_name = fullname
    doc.email = email
    doc.phone = phone
    doc.message = message
    doc.insert()

    return "Created"