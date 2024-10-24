import frappe

@frappe.whitelist()
def sale_person(doc, method=None):
    # Dictionary to hold item salespersons
    item_salespersons = {}
    all_sales_persons = set()  # Set to hold unique salespersons

    for item in doc.items:
        invoice_item_code = item.item_code
        sales_person_names = find_sales_person(invoice_item_code)

        if sales_person_names:
            item_salespersons[item.item_name] = sales_person_names
            # Add the sale_person part to the set (removes duplicates)
            all_sales_persons.update([name.split(' (Name: ')[0] for name in sales_person_names])
        else:
            item_salespersons[item.item_name] = ['No Sales Person found']

    # Prepare messages to display
    messages = []
    for item_name, salespersons in item_salespersons.items():
        salesperson_list = ", ".join(salespersons)
        messages.append(f'Sales Person(s) for item {item_name} (Item Code: {invoice_item_code}) are: {salesperson_list}')

    # Display all messages at once
    frappe.msgprint("<br>".join(messages))

    # Convert the set of unique salespersons to a list
    unique_sales_persons_list = list(all_sales_persons)
    frappe.msgprint(f'Unique Sales Persons: {", ".join(unique_sales_persons_list)}')

    # Calculate the allocated percentage per salesperson
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
    # Fetch both name and sale_person fields from Sale Person Assignment
    sale_persons = frappe.get_all('Sale Person Assignment', fields=['name', 'sale_person'])
    sales_person_names = []

    # Fetch all Sale Person Products at once
    sale_products = frappe.get_all('Sale Person Product', fields=['item_code', 'parent'])

    # Create a map for quick lookups
    sale_person_product_map = {}
    for product in sale_products:
        if product.parent not in sale_person_product_map:
            sale_person_product_map[product.parent] = []
        sale_person_product_map[product.parent].append(product.item_code)

    # Check against the map for all sales persons
    for person in sale_persons:
        if item_code in sale_person_product_map.get(person['name'], []):
            # Add both name and sale_person to the list
            sales_person_names.append(f"{person['sale_person']} (Name: {person['name']})")

    return sales_person_names  # Return the list of sales persons
