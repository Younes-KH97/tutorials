from odoo import models, fields, api


class PropertyType(models.Model):
    _name = "property.type"
    _order = "sequence, name"

    property_ids = fields.One2many("property", "property_type_id")
    offer_ids = fields.One2many('property.offer',
                                "property_type_id",
                                "offers")

    name = fields.Char()

    offer_count = fields.Integer("Offers",compute='_compute_total_offers')
    offer_count_text = fields.Char("Offers",compute='_get_total_offers_text', store=False)
    sequence = fields.Integer('Sequence', default=1)

    @api.depends("offer_ids")
    def _compute_total_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    @api.depends("offer_count")
    def _get_total_offers_text(self):
        for record in self:
            record.offer_count_text = str(record.offer_count)+" \n offers "


