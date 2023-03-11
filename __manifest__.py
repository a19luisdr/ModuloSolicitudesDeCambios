# -*- coding: utf-8 -*-
{
    'name': "Change Request Management",
    'summary': "Manage change requests easily",
    'description': """
Manage Change Requests
==============
With this module you can manage change requests for your application in development.
    """,
    'author': "Luís Doce Rodríguez",
    'website': "https://github.com/a19luisdr/modulo_odoo_a19luisdr",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/change_request.xml',
        'views/change_request_category.xml',
    ],
}
