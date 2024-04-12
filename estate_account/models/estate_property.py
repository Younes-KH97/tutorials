from odoo import models, fields, api, Command
from odoo.exceptions import UserError


class Property(models.Model):
    _inherit = "property"
    _name = "property"

    def set_sold_property(self):
        # ui-form check (I'm not sure!!!) And modif data to store (I'm sure!!!)
        super(Property, self).set_sold_property()
        print(dir(self))
        partner_id = self.partner_id.id
        name = self.name
        quantity = 1
        price_unit = self.selling_price * 6 / 100
        invoice_vals_list = {
            "partner_id": partner_id,
                             "invoice_line_ids": [
                                 Command.create({
                                     "name": name,
                                     "quantity": quantity,
                                     "price_unit": price_unit
                                 }),
                                 Command.create({
                                     "name": "Administrative fees",
                                     "quantity": quantity,
                                     "price_unit": 100
                                 }),
                            ]
                             }
        moves = self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice_vals_list)






