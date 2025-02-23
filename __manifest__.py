# -*- coding: utf-8 -*-
{
    'name': "Education Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','portal', 'contacts','web'],

    

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/create_student_view.xml',
        'views/student_view.xml',
        'views/owl.xml',
        'views/menu.xml',
    ],

    'assets': {
        'web.assets_backend': [
            '/edu_ms/static/src/component/**/*.js',
            '/edu_ms/static/src/component/**/*.scss',
             'edu_ms/static/src/**/*.css',
        ],
        'web.assets_qweb': [
            '/edu_ms/static/src/component/**/*.xml'
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
