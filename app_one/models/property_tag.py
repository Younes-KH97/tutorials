from odoo import models, fields


class PropertyTag(models.Model):
    _name = "property.tag"
    _order = "name"

    color = fields.Integer()

    name = fields.Char()
