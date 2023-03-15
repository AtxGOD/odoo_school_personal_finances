from odoo import fields, models


class FinanceHistory(models.Model):
    """Fields to control spending"""
    _name = 'finance.history'
    _description = 'Cost history'

    date = fields.Date(
        default=fields.Datetime.today,
    )
    sum = fields.Integer()
    currency = fields.Selection(
        selection=[('uah', 'UAH'),
                   ('usd', 'USD'),
                   ('eur', 'EUR')],
        default='uah',
    )
    shop_id = fields.Many2one(
        comodel_name='finance.shop',
    )
