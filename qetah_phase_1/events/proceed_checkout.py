import frappe

@frappe.whitelist()
def checks(fullname, phone, address, city, state, ara, code):
    doc = frappe.new_doc("Proceed Checkout")
    doc.full_name = fullname
    doc.phone = phone
    doc.address = address
    doc.city = city
    doc.state = state
    doc.code = code 
    doc.save()
    return "Created"
