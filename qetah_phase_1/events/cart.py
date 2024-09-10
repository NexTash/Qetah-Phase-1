import frappe

@frappe.whitelist()
def carts(email,phone,address,state,city,postalcode):
    doc = frappe.new_doc("Address")
    doc.address_line1= address
    doc.address_type= "Billing"
    doc.address_title= address
    doc.email_id = email
    doc.state = state
    doc.city = city
    doc.phone = phone
    doc.pincode = postalcode
    doc.insert()
    return "Created"