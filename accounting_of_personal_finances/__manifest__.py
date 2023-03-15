# Copyright © 2022 Odoo School (<https://garazd.biz>)
# @author: Yurii Pustashinskii (<vista2990@gmail.com>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Personal finances',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Accounting of personal finances""",
    'license': 'LGPL-3',
    'author': 'Yura Pustashinskii',
    'website': 'https://github.com/AtxGOD/',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/finance_debt_groups.xml',
        'security/ir.model.access.csv',
        'security/finance_debt_security.xml',
        'wizard/finance_change_debt_sum_wizard_view.xml',
        'views/finance_menus.xml',
        'views/finance_history_views.xml',
        'views/finance_receipt_history_views.xml',
        'views/finance_debt_history_views.xml',
        'views/invoicing_inherit_views.xml',
        'views/finance_receipt_source_views.xml',
        'views/finance_shop_views.xml',
        'views/res_partner_views.xml',
        'report/spending_report.xml',
        'report/report.xml',
    ],
    'demo': [
        'data/finance_receipt_source_demo.xml',
        'data/finance_receipt_history_demo.xml',
        'data/finance_shop_demo.xml',
        'data/finance_history_demo.xml',
        'data/finance_debt_history_demo.xml',
    ],
    'support': 'vista2990@gmail.com',
    'application': True,
    'installable': True,
    'auto_install': False,
}
