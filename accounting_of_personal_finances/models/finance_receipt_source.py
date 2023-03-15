from odoo import fields, models


class FinanceReceiptSource(models.Model):
    """Fields to control receipt sources"""
    _name = 'finance.receipt.source'
    _description = 'Receipt sources'

    name = fields.Char()
    costs_ids = fields.One2many(
        comodel_name='finance.receipt.history',
        inverse_name='source_id',
    )
