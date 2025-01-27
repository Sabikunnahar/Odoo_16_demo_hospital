from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError

class HospitalPatients(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread']
    _description = "Hospital Doctors Records"

    name = fields.Char(string="Doctor Name")
    reference = fields.Char(string="Reference")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender", tracking=True)