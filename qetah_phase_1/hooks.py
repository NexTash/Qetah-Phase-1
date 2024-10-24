app_name = "qetah_phase_1"
app_title = "Qetah Phase 1"
app_publisher = "NexTash"
app_description = "This is related to ecommerece"
app_email = "support@nextash.com"
app_license = "NexTash(SMC.Pvt).Ltd."

# Includes in <head>
# ------------------

app_logo_url = "/assets/qetah_phase_1/images/qetah-browser-removebg-preview.png"
website_context = {
  "favicon": "/assets/qetah_phase_1/images/qetah-browser-removebg-preview.png",
  "splash_image": "/assets/qetah_phase_1/images/black-qetah-removebg-preview.png",
}

# include js, css files in header of desk.html
# app_include_css = "/assets/qetah_phase_1/css/qetah_phase_1.css"
# app_include_js = "/assets/qetah_phase_1/js/sale.js"

# include js, css files in header of web template
# web_include_css = "/assets/qetah_phase_1/css/qetah_phase_1.css"
# web_include_js = "/assets/qetah_phase_1/js/qetah_phase_1.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "qetah_phase_1/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Sales Person" : "public/js/sale.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "qetah_phase_1.utils.jinja_methods",
# 	"filters": "qetah_phase_1.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "qetah_phase_1.install.before_install"
# after_install = "qetah_phase_1.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "qetah_phase_1.uninstall.before_uninstall"
# after_uninstall = "qetah_phase_1.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "qetah_phase_1.utils.before_app_install"
# after_app_install = "qetah_phase_1.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "qetah_phase_1.utils.before_app_uninstall"
# after_app_uninstall = "qetah_phase_1.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qetah_phase_1.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways
permission_query_conditions = {
    "Sales Invoice": "qetah_phase_1.permission.sales_invoice_query",
    }

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"validate": "qetah_phase_1.events.sale.sale_person"
	}
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"qetah_phase_1.tasks.all"
# 	],
# 	"daily": [
# 		"qetah_phase_1.tasks.daily"
# 	],
# 	"hourly": [
# 		"qetah_phase_1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"qetah_phase_1.tasks.weekly"
# 	],
# 	"monthly": [
# 		"qetah_phase_1.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "qetah_phase_1.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qetah_phase_1.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "qetah_phase_1.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["qetah_phase_1.utils.before_request"]
# after_request = ["qetah_phase_1.utils.after_request"]

# Job Events
# ----------
# before_job = ["qetah_phase_1.utils.before_job"]
# after_job = ["qetah_phase_1.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"qetah_phase_1.auth.validate"
# ]
# website_route_rules = [
#     {
#         "from_route": "/blog-post/<path:slug>",
#         "to_route": "blog-post",
#     }

# ]
fixtures=[
    {
        "dt" : "Role",
        "filters": [
            [
                "name","in",
                [
                    "Sale Person",
                    "Blogger",
                ]
            ]
        ]
    },
     {
        "dt" : "Module Profile",
        "filters": [
            [
                "name","in",
                [
                    "Sale Person"
                ]
            ]
        ]
    },  
]