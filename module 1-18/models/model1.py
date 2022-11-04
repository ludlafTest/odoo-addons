# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_mode = fields.Selection(
        string="Payment pech mode",
        selection=[
            ('cash', 'Cashg'),
            ('bank', 'Bankz'),
            ('electronic', 'Electronich'),
        ],
        default="electronic",
    )
