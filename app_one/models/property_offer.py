from odoo import models, fields, api
from datetime import datetime, timedelta

from odoo.exceptions import UserError


class PropertyOffer(models.Model):
    _name = "property.offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection( [('accepted', 'Accepted'),('refused','Refused')],
                               nocopy = True
                             )
    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(default = datetime.now() + timedelta(days=7),
                                compute = "_compute_date_deadline",
                                inverse = "_inverse_date_deadline")
    # create_date = fields.Date()#, We do not need to add this attr, since we can call it (see _compute_date_deadline and _reverse_date_deadline functions)
    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('property', required = True)
    property_type_id = fields.Many2one('property.type','Type', related="property_id.property_type_id", store=True)
    property_status = fields.Char(compute="_get_property_status", store=False)

    @api.model_create_multi
    def create(self, data_list):
        # ui-form check (I'm not sure!!!) And modif data to store (I'm sure!!!)
        offer_in = super(PropertyOffer, self).create(data_list)
        for offer in offer_in.property_id.offer_ids:
            if offer.price > offer_in.price:
                raise UserError("New offer price should be greater than old offers")
            if not offer_in.property_id.status == "offer_received":
                offer_in.property_id.status = "offer_received"
        return offer_in

    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            create_date = fields.Datetime.from_string(record.create_date)
            if record.create_date and record.validity:
                deadline = create_date + timedelta(days=record.validity)
                record.date_deadline = deadline.date()
            elif not record.create_date:
                deadline = datetime.now() + timedelta(days=record.validity)
                record.date_deadline = deadline.date()

    def _inverse_date_deadline(self):
        for record in self:
            deadline = fields.Datetime.from_string(record.date_deadline)
            create_date = fields.Datetime.from_string(record.create_date)
            if record.create_date and record.date_deadline:
                validity = (deadline - create_date).days
                record.validity = validity
            elif record.date_deadline and not record.create_date:
                record.validity = (deadline - datetime.now()).days

    @api.depends("property_id.status")
    def _get_property_status(self):
        for record in self:
            record.property_status = record.property_id.status

    #Why looping through self? In the documentation it says:
    #Always assume that a method can be called on multiple records; it’s better for reusability.
    #So self parameter can be a collection of objects
    #Imagine we want to delete the n selected record from the xml file, it will send
    #a collection of properties in the function will loop through.

    def accept_property_offer(self):
        for record in self:
            record.status = "accepted"
            record.property_id.status = "offer_accepted"
            record.property_id.selling_price = record.price
            record.property_id.partner_id = record.partner_id


    def refuse_property_offer(self):
        for record in self:
            record.status = "refused"


