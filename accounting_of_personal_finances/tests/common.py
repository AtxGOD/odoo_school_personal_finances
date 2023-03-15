from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_debt_user = self.env.ref(
            'accounting_of_personal_finances.group_debt_user')
        self.group_debt_admin = self.env.ref(
            'accounting_of_personal_finances.group_debt_admin')
        self.finance_user = self.env['res.users'].create({
            'name': 'Finance User',
            'login': 'finance_user',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_debt_user.id)],
        })
        self.finance_admin = self.env['res.users'].create({
            'name': 'Finance Admin',
            'login': 'finance_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_debt_admin.id)],
        })
        self.reader = self.env['res.partner'].create({'name': 'Demo Debt'})
        self.spending_demo = self.env['finance.history'].create({
            'sum': 1000})
        self.receipt_demo = self.env['finance.receipt.history'].create({
            'sum': 1000})
        self.debt_demo = self.env['finance.debt.history'].create({
            'sum': 1000})

