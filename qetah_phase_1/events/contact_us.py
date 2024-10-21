import frappe

from frappe.model.document import Document


@frappe.whitelist()
def contacts(fullname, email, phone, message):
    if not frappe.db.exists("Customer", {"customer_name": fullname}):
        customer = frappe.new_doc("Customer")
        customer.customer_name = fullname
        customer.insert()
        frappe.db.commit()

    qetah_family = frappe.new_doc("Qetah Faimly")
    qetah_family.customer_name = fullname

    if not email and frappe.session.user != "Guest":
        user_email = frappe.db.get_value("User", frappe.session.user, "email")
        qetah_family.email = user_email
    else:
        qetah_family.email = email

    qetah_family.insert()
    frappe.db.commit()
    # send_custom_email()


    return f"Hello {fullname}, your email has been received. Thanks for visiting!"
# def send_custom_email():
#     # Static recipient email
#     recipient_email = "7ahmed8raza6@nextashgmail.com"
#     # Use static sender email instead of session user
#     sender_email = "7ahmed8raza6@gmail.com"
#     subject = "Subject of the email"
#     message = "This is the body of the email."

#     # Send the email
#     frappe.sendmail(
#         recipients=recipient_email,
#         sender=sender_email,  # Static sender email
#         subject=subject,
#         message=message,
#         header=[subject, "green"],
#         delayed=False,
#         retry=3
#     )

# frappe.msgprint("send the mail successfuly")
