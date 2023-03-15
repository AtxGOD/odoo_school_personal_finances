from odoo import fields, models


class FinanceShop(models.Model):
    """Fields to control shops"""
    _name = 'finance.shop'
    _description = 'Shops'

    name = fields.Char()
    costs_ids = fields.One2many(
        comodel_name='finance.history',
        inverse_name='shop_id',
    )
