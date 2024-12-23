# Copyright 2018 Daniel Campos <danielcampos@avanzosc.es> - Avanzosc S.L.
# Copyright 2021 Camptocamp SA
# @author: Simone Orsi <simone.orsi@camptocamp.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase

from odoo.addons.base.tests.common import DISABLED_MAIL_CONTEXT


class CommonCase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, **DISABLED_MAIL_CONTEXT))
        cls.product = cls.env["product.product"].create({
            "name": "Test Product",
            "type": "product",
            "default_code": "TEST_0001",
            "standard_price": 500.0,
            "weight": 0.01,
        })
        cls.supplier = cls.env["res.partner"].create({
            "name": "Test supplier",
            "is_company": True,
            "street": "77 Santa Barbara Rd",
            "city": "Pleasant Hill",
            "state_id": cls.env.ref("base.state_us_5").id,
            "country_id": cls.env.ref("base.us").id,
            "zip": "94523",
            "email": "test_supplier@yourcompany.example.com",
            "phone": "(603)-996-3829",
            "vat": "US12345673",
        })
        cls.product_brand_obj = cls.env["product.brand"]
        cls.product_brand = cls.product_brand_obj.create(
            {
                "name": "Test Brand",
                "description": "Test brand description",
                "partner_id": cls.supplier.id,
            }
        )
