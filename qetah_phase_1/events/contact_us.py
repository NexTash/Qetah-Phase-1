import frappe

@frappe.whitelist()
def contacts(fullname, email, phone, message):
    doc = frappe.new_doc("Contact us")
    doc.full_name = fullname
    doc.email = email
    doc.phone = phone
    doc.message = message
    doc.insert()
    
    # Return a success message
    return f"Hello {fullname}, your email {email} has been received. Thanks for visiting!"
