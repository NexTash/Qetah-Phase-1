import frappe

def get_context(context):
    blogs = frappe.get_all("Blog Post", filters={"custom_is_featured": 1}, fields=["*"])
    
    products = frappe.get_all("Product", ["*"] ,filters={"is_featured": 1}, order_by="modified asc")
    testimonials = frappe.get_all("Testimonial", ["*"] ,filters={"featured": 1}, order_by="modified asc")

    context.update({
        "blogs": blogs,
        "products":products,
        "testimonials":testimonials,
    })