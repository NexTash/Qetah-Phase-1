import frappe
import csv

@frappe.whitelist(allow_guest=True)
def get_translations(lang):
    translations = {}
    path = frappe.get_app_path('qetah_phase_1', 'translations', 'ar.csv')

    with open(path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            translations[row['id']] = row[lang]

    return translations
 
@frappe.whitelist(allow_guest=True)
def get_footer(language):
    footer_translations = {}
    path = frappe.get_app_path('qetah_phase_1', 'translations', 'ar.csv') 

    with open(path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            footer_translations[row['id']] = row[language]

    return footer_translations