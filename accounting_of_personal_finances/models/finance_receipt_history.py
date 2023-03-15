from odoo import fields, models


class FinanceReceiptHistory(models.Model):
    """Fields to control receipt"""
    _name = 'finance.receipt.history'
    _inherit = ['finance.history']
    _description = 'finance receipt history'

    source_id = fields.Many2one(
        comodel_name='finance.receipt.source',
    )
