# -*- coding: utf-8 -*-
{
    'name': "Cabinet Test",

    'summary': """
        """,

    'descriptison': """
        Une appliation qui permet de gérer une cabinet médiale
    """,

    'author': "HAFSSA",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management','board'],
    # always loaded
    'data': [
        'reports/reports.xml',
        'reports/reports_templates.xml',

        'security/cabinet_security.xml',
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/ordonance_view.xml',
        'views/consultation_view.xml',
        'views/medicament_view.xml',
        'views/paiement.xml',
        'views/appoitement_view.xml',
        'views/dashboard.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}