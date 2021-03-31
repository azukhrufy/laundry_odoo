# -*- coding: utf-8 -*-
{
    'name': "Aplikasi Laundry Odoo",

    'summary': """
        Merupakan aplikasi management laundry untuk mengelola per laundry an indonesia""",

    'description': """
        Merupakan aplikasi management laundry untuk mengelola per laundry an indonesia
    """,

    'author': "Ananda Zukhruf Awalwi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Industries',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale', 'account', 'uom'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/LaundryOrder/order.xml',
        'views/actions/order_actions.xml',
        'views/views.xml',
        'views/actions/actions_report.xml',
        'views/actions/report_laundry_order.xml',
        'views/actions/report_laundry_label.xml',
        'views/actions/actions_invoice_button.xml',
        'report/report_laundry_receipt.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}