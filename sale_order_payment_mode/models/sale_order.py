from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    payment_mode = fields.Selection(
        string="Payment Mode",
        selection=[
            ("cash", "Cashm"),
            ("bank", "Bankn"),
            ("electronic", "Electronico"),
        ],
        default="electronic",
    )
