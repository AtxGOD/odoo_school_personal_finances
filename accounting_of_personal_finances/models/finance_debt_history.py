from odoo import fields, models


class FinanceDebtsHistory(models.Model):
    """Fields to control debts"""
    _name = 'finance.debt.history'
    _inherit = ['finance.history']
    _description = 'Debts history'

    action = fields.Selection(
        selection=[('lend', 'Lend'),
                   ('borrow', 'Borrow')],
        default='lend',
    )
    person_id = fields.Many2one(
        comodel_name='res.partner',
    )
    done = fields.Boolean()
