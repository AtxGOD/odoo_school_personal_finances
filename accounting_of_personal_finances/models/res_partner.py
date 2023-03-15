from odoo import fields, models


class ResPartner(models.Model):
    """Model to add telegram field to contacts"""
    _inherit = 'res.partner'

    telegram = fields.Char(
        string='Telegram Nickname',
    )
