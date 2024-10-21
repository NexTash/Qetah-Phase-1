import frappe
from frappe.core.doctype.communication.email import make

@frappe.whitelist()  # This ensures the function is accessible
def send_custom_email():
    try:
        make(
            recipients=["7ahmed8raza6nextash@gmail.com"],
            sender="7ahmed8raza6@gmail.com",
            subject="Test Email",
            content="<p>This is a test email.</p>",
            send_email=True,
            communication_medium="Email",
            reference_doctype="Sales Order",
            reference_name="SO-0001"
        )
        return "Email sent successfully."
    except Exception as e:
        frappe.log_error(message=e, title="Email Sending Failed")
        return "An error occurred while sending the email."
