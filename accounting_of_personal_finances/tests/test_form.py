from odoo import fields
from odoo.tests import tagged
from odoo.tests.common import Form
from odoo.addons.accounting_of_personal_finances.tests.common import TestCommon


@tagged('post_install', '-at_install', 'finance')
class TestForm(TestCommon):

    def test_finance_spending_date(self):
        spending_form = Form(self.spending_demo)

        self.assertEqual(spending_form.taken_date, fields.Date.today())

    def test_finance_receipt_date(self):
        receipt_form = Form(self.receipt_demo)

        self.assertEqual(receipt_form.taken_date, fields.Date.today())

    def test_finance_debt_date(self):
        debt_form = Form(self.debt_demo)

        self.assertEqual(debt_form.taken_date, fields.Date.today())
