import frappe

@frappe.whitelist()
def checks(fullname, phone, address, city, state, code,email,stripe,item_count,grand_total,cod):
    doc = frappe.new_doc("Delivery Information")
    doc.full_name = fullname
    doc.phone_no = phone
    doc.address = address
    doc.city = city
    doc.state = state
    doc.postal_code = code 
    doc.email = email 
    doc.payment_method = stripe 
    doc.payment_method = cod 
    doc.total_price = grand_total 
    doc.items = item_count 
    doc.save()
    return "Created"