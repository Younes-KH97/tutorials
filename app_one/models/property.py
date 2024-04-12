from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare


class Property(models.Model):
    _name = "property"
    _order = "id desc"

    property_type_id = fields.Many2one("property.type", string="Property type")
    partner_id = fields.Many2one("res.partner", string="Partner")
    user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user, copied=False)
    tag_ids = fields.Many2many("property.tag", string="Tags")
    offer_ids = fields.One2many("property.offer", "property_id")

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date('Available From',
                                    copy=False,
                                    default=lambda self: datetime.now() + timedelta(days=3*30))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West')
    ])
    active = fields.Boolean(default = True) # Reserved Field, make it false to filter out not needed records in the ui
    status = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled'),
    ], default = 'new')
    total_area = fields.Float(compute = '_compute_total_area')
    best_price = fields.Float(compute = '_compute_best_price')

    # It did not work, so I connected to postgresdb and made the constraint:
    # ALTER TABLE Property
    # ADD CONSTRAINT check_expected_price CHECK (expected_price > 0);

    # ALTER TABLE your_module_person
    # ALTER COLUMN salary SET NOT NULL;
    # _sql_constraints = [
    #     ('check_expected_price', 'CHECK(expected_price > 0)',
    #      'The percentage of an analytic distribution should be between 0 and 100.')
    # ]

    def set_sold_property(self):
        if self.status == 'canceled': raise UserError("Canceled properties cannot be sold")
        self.status = 'sold'

    def cancel_property(self):
        self.status = 'canceled'

    @api.constrains('selling_price')
    def _check_date_end(self):
        for record in self:
            if float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) == -1:
                raise ValidationError("it is not be possible to accept an offer lower than 90% of the expected price")

    @api.onchange("garden")
    def _onchange_garden(self):
        for record in self:
            if record.garden == True:
                record.garden_area = 10
                record.garden_orientation = "north"
            else:
                record.garden_area = 0
                record.garden_orientation = ""
    @api.depends("living_area","garden","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area # Compute function must return a value, if you comment this instruction it will bug since there are multiple record with no garden area
            if record.garden == True:
                record.total_area = record.total_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            record.best_price = 0
            if len(record.offer_ids) > 0:
                try:
                    record.best_price = max(offer.price for offer in record.offer_ids if offer.status == 'offer_accepted')
                except: pass

    @api.ondelete(at_uninstall=False)
    def _unlink_if_property_is_new_or_canceled(self):
        if any((property.status in ('new','canceled')) for property in self):
            raise UserError("Can't delete neither a new property nor a canceled one!")
        super(Property, self).unlink()
