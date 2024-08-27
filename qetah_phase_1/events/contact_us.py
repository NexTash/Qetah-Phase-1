import frappe

@frappe.whitelist()
def contacts(fullname,email,phone,message):
    doc = frappe.new_doc("Contact us")
    doc.name1 = fullname
    doc.email = email
    doc.phone = phone
    doc.message = message
   
    # doc.append("email_ids", {
    #         'email_id' : email
    #     })
    doc.insert()

    return "Created"