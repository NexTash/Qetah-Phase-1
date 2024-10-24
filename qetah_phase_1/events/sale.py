import frappe

@frappe.whitelist()
def sale_person(doc, method=None):
    item_salespersons = {}
    all_sales_persons = set()

    for item in doc.items:
        invoice_item_code = item.item_code
        sales_person_names = find_sales_person(invoice_item_code)

        if sales_person_names:
            item_salespersons[item.item_name] = sales_person_names
            all_sales_persons.update([name.split(' (Name: ')[0] for name in sales_person_names])
        else:
            item_salespersons[item.item_name] = ['No Sales Person found']

    messages = []
    for item_name, salespersons in item_salespersons.items():
        salesperson_list = ", ".join(salespersons)
        messages.append(f'Sales Person(s) for item {item_name} (Item Code: {invoice_item_code}) are: {salesperson_list}')

    # frappe.msgprint("<br>".join(messages))

    unique_sales_persons_list = list(all_sales_persons)
    # frappe.msgprint(f'Unique Sales Persons: {", ".join(unique_sales_persons_list)}')

    if unique_sales_persons_list:
        allocated_percentage = 100 / len(unique_sales_persons_list)
    else:
        allocated_percentage = 0

    for sales_person in unique_sales_persons_list:
        doc.append("sales_team", {
            "sales_person": sales_person,
            "allocated_percentage": allocated_percentage
        })

def find_sales_person(item_code):
    sale_persons = frappe.get_all('Sale Person Assignment', fields=['name', 'sale_person'])
    sales_person_names = []
    sale_products = frappe.get_all('Sale Person Product', fields=['item_code', 'parent'])

    sale_person_product_map = {}
    for product in sale_products:
        if product.parent not in sale_person_product_map:
            sale_person_product_map[product.parent] = []
        sale_person_product_map[product.parent].append(product.item_code)

    for person in sale_persons:
        if item_code in sale_person_product_map.get(person['name'], []):
            sales_person_names.append(f"{person['sale_person']} (Name: {person['name']})")

    return sales_person_names

