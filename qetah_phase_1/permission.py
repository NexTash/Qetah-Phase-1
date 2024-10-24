import frappe

def sales_invoice_query(user=None):
    user = user or frappe.session.user
    
    # Do nothing if Administrator
    if user == "Administrator":
        return


    to_do_records = frappe.get_all(
        "ToDo", 
        filters={'status': "Open", 'reference_type': "Sales Invoice", 'allocated_to': user},
        fields=["reference_name"]
    )

    # If no ToDo records, return early
    if not to_do_records:
        return None

    sales_invoice_refs = [todo['reference_name'] for todo in to_do_records]

    if not sales_invoice_refs:
        return None

    invoices_in_clause = ', '.join(frappe.db.escape(ref) for ref in sales_invoice_refs)

    return f"(`tabSales Invoice`.name IN ({invoices_in_clause}))"


