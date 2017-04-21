# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api

#Created diffrent fields for our assets model.
class assets(models.Model):
    _name = 'assets.assets'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    # Relation
    responsible_id = fields.Many2many('res.users',
        ondelete='set null', string="Responsible", index=True)

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

# Realtions between models
class assests_session(models.Model):
    _name = 'assets.session'
    name = fields.Char(required=True)
    start_date = fields.Date()
    last_modified = fields.Date(onchange='_last_modified')
    instructor_id = fields.Many2one('res.partner', string="Instructor")
 
    @api.onchange('start_date')
    def _last_modified(self):
        self.last_modified = self.start_date
        # Can optionally return a warning and domains


class Partner(models.Model):
    _inherit = 'assets.session'

    # Add a new column to the assets.session, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor",default=True)

class Assets(models.Model):
    _name = 'asset.view'
    _inherit = 'account.asset.asset'
  
    # Add a new column to the assets.session, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor",default=True)



