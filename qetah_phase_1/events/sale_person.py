import frappe

@frappe.whitelist()
def get_sales_person_by_user():
    user = frappe.session.user    
    sales_person = frappe.db.get_value('Sales Person', {'custom_sale_person_user': user})
    return sales_person if sales_person else None

@frappe.whitelist()
def get_sales_invoice_count(filters):
    frappe.msgprint(filters)
    user = frappe.session.user
    si={}
    sp_filter = {}
    sales_person=""
    if user != "Administrator":
        sales_person = frappe.db.get_value('Sales Person', {'custom_sale_person_user': user},['name'])
        sp_filter={'sales_person': sales_person }
    
    si_list = frappe.db.get_all('Sales Team', sp_filter, ["parent"])
    for row in si_list:
        si_doc = frappe.get_doc("Sales Invoice",row.parent)
        if si_doc.docstatus!=2:
            flag = False
            if sales_person:
                for item in si_doc.sales_team:
                    if item.sales_person == sales_person:
                        flag=True
                        break
                if flag==True:
                    if si_doc.name not in si:
                        si[si_doc.name] = si_doc.name
            else:
                if si_doc.name not in si:
                    si[si_doc.name] = si_doc.name

    length= len(si)
    
    return length