import frappe
import json
from datetime import datetime

@frappe.whitelist()
def carts(email, phone, address, state, city, postalcode, firstname, lastname ):
    fullname = firstname + " " + lastname
    
    if not frappe.db.exists("Customer", {"customer_name": fullname}):
        customer = frappe.new_doc("Customer")
        customer.customer_name = fullname
        customer.customer_type = "Individual"
        customer.insert()
        frappe.db.commit()
    else:
        customer = frappe.get_doc("Customer", {"customer_name": fullname})

    
    doc = frappe.new_doc("Address")
    doc.address_line1= address
    doc.address_type= "Billing"
    doc.address_title= address
    doc.email_id = email
    doc.state = state
    doc.city = city
    doc.phone = phone
    doc.pincode = postalcode

    doc.append("links", {
        "link_doctype": "Customer",
        "link_name": customer.name
    })

    doc.insert()
    return "Address created and linked to customer", firstname, lastname


@frappe.whitelist(allow_guest=True)
def create_invoice(cart, address):
    address = json.loads(address)
    cart = json.loads(cart)
    fullname = f"{address['firstname']} {address['lastname']}"
    if not frappe.db.exists("Customer", {"customer_name": fullname}):
        customer = frappe.new_doc("Customer")
        customer.customer_name = fullname
        customer.customer_type = "Individual"
        customer.insert()
        frappe.db.commit()
    else:
        customer = frappe.get_doc("Customer", {"customer_name": fullname})

    doc = frappe.get_doc({
        'doctype': 'Sales Invoice',
    })
    doc.customer = fullname
    for row in cart:
            doc.append("items", {
                "item_code": row.get('title'),
                "qty": row.get('qty', 1)
            })

    doc.insert()
    frappe.db.commit()


    