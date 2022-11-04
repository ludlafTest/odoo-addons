# -*- coding: utf-8 -*-
{
    'name': "Modo de pago en Sale Order",

    'summary': """
        Modulo de prueba para el curso de Odoo 14
        """,
    'description': """
        Modulo de curso para el prueba de Odoo 14
    """,

    'author': "Lvis",
    'website': "http://www.lvis.com",

    'category': 'Tools',
    'version': '1.0.0',

    'depends': ['sale'],

    # always loaded
    'data': [
        "views/sale_order_view.xml"
    ],
    'license': 'AGPL-3',
}
