import frappe

@frappe.whitelist()
def checks(fullname,phone,address,city,province,area,code):
    doc = frappe.new_doc("Checkout")
    doc.full_name = fullname
    doc.phone = phone
    doc.address = address
    doc.city = city
    doc.province = province
    doc.area = area
    doc.code = code 
    # doc.append("email_ids", {
    #         'email_id' : email
    #     })
    doc.insert()
    doc.save()