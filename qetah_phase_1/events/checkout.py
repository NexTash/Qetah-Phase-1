import frappe

@frappe.whitelist()
def checks(fullname,email,phone,address,city,province,area,code):
    doc = frappe.new_doc("Checkout")
    doc.full_name = fullname
    doc.email = email
    doc.phone = phone
    doc.address = address
    doc.city = city
    doc.province = province
    doc.area = area
    doc.code = code 
    # doc.append("email_ids", {
    #         'email_id' : email
    #     })
    doc.save()