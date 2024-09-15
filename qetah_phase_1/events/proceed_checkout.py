import frappe

@frappe.whitelist(allow_guest=True)
def poceed_to_checkout(fullname, phone, address, city, state, code, email, stripe, cod, item_count1, grand_total1,title):
    # Check for duplicates in the Proceed Checkout doctype
    if frappe.db.exists("Proceed Checkout", {"full_name": fullname, "phone_no": phone, "address": address}):
        # If user exists in Proceed Checkout, display a warning message
        frappe.throw("This user with the given name, phone, and address already exists in Proceed Checkout.")
    
    # Check for duplicates in the Delivery Information doctype
    if frappe.db.exists("Delivery Information", {"full_name": fullname, "phone": phone, "address": address}):
        # If user exists in Delivery Information, display a warning message
        frappe.throw("This user with the given name, phone, and address already exists in Delivery Information.")

    # Create new record in Proceed Checkout if no duplicate found
    doc = frappe.new_doc("Proceed Checkout")
    doc.full_name = fullname
    doc.phone_no = phone
    doc.address = address
    doc.city = city
    doc.state = state
    doc.postal_code = code
    doc.email = email
    doc.total_price = grand_total1
    doc.items = item_count1
    
    # Set payment method
    if stripe == '1':
        doc.payment_method = "Stripe"
    elif cod == '1':
        doc.payment_method = 'Cash on Delivery'
    
    doc.save()

    # Create new record in Delivery Information
    delivery_doc = frappe.new_doc("Delivery Information")
    delivery_doc.full_name = fullname
    delivery_doc.phone = phone
    delivery_doc.address = address
    delivery_doc.city = city
    delivery_doc.state = state

    items = [
    {'title': title, 'qty': item_count1, 'item': title},

    ]

    for item in items:
    # Append a new row to the child table
        delivery_doc.append('order_items', {
        'title': item['title'],
        'qty': item['qty'],
        'title': item['title'],
         # If you have a total field per item
    })

    delivery_doc.save()
    frappe.db.commit()
    return "Created"