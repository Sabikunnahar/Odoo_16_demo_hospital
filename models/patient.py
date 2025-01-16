from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError

class HospitalPatients(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Hospital Patients Records"

    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is Child", default=False)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender", tracking=True)
    capitalized_name = fields.Char(string="Capitalized Name" , compute="_compute_capitalized_name")

    @api.depends('name')
    def _compute_capitalized_name(self):
        if self.name:
            self.capitalized_name = self.name.upper()
        else:
            self.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        if self.age<= 10:
            self.is_child = True
        else:
            self.is_child = False

    @api.constrains('is_child','age')
    def _check_age(self):
        if self.is_child and self.age == 0:
            raise ValidationError(_("Age must be greater than or equal to 10"))
