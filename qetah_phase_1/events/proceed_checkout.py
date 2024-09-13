import frappe

@frappe.whitelist(allow_guest=True)
def checks(fullname, phone, address, city, state, code, email, stripe, cod, item_count, grand_total):
    if frappe.db.exists("Proceed Checkout", {"full_name": fullname, "phone": phone, "address": address}):
        frappe.throw("This user with the given name, phone, and address already exists.")
    doc = frappe.new_doc("Proceed Checkout")
    doc.full_name = fullname
    doc.phone = phone
    doc.address = address
    doc.city = city
    doc.state = state
    doc.code = code
    doc.save()
    # Delivery Information
    delivery_doc = frappe.new_doc("Delivery Information")
    delivery_doc.full_name = fullname
    delivery_doc.phone_no = phone
    delivery_doc.address = address
    delivery_doc.city = city
    delivery_doc.state = state
    delivery_doc.postal_code = code
    delivery_doc.email = email

    # Payment Method
    if stripe == '1':
        delivery_doc.payment_method = "Stripe"
    if cod == '1':
        delivery_doc.payment_method = 'Cash on Delivery'

    delivery_doc.total_price = grand_total
    delivery_doc.items = item_count
    delivery_doc.save()

    return "Created"
