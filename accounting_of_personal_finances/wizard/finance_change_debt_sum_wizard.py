from odoo import fields, models


class FinanceChaneDebtSumWizard(models.TransientModel):
    """Wizard fields to change sum"""
    _name = "finance.change.debt.sum.wizard"
    _description = "Finance debt wizard"

    sum = fields.Integer()

    def action_change_sum(self):
        """change sum in all chosen records"""
        for rec_id in self._context['active_ids']:
            domain = [('id', '=', rec_id)]
            res = self.env['finance.debt.history'].search(domain, limit=1)
            res.sum = self.sum
