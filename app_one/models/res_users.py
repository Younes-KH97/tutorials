from odoo import fields, models


class Users(models.Model):
    _name = "res.users"
    _inherit = "res.users"

    def _property_ids_domain(self):
        return [('status', 'in', ['new', 'offer_received'])]

    property_ids = fields.One2many("property",
                                   "user_id",
                                   "properties",
                                   domain=_property_ids_domain)

