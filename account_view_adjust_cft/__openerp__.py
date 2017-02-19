# -*- coding: utf-8 -*-
# Copyright 2016 Ecosoft Co. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Account View Adjust CFT",
    "version": "8.0.1.5.1",
    "author": "Ecosoft Co. Ltd.",
    "license": "AGPL-3",
    "description": """
    """,
    "category": "Account",
    "depends": [
        'account_voucher',
        'product_price_visible',
        'account_billing',
    ],
    "data": [
        'views/account_voucher_pay_invoice.xml',
        'views/account_menuitem.xml',
        'views/account_billing.xml',
        'views/voucher_payment_receipt_view.xml',
        'views/report_invoice.xml',
    ],
    "js": [
    ],
    "css": [
    ],
    "auto_install": False,
    "installable": True,
    "external_dependencies": {
        'python': [],
    },
}
