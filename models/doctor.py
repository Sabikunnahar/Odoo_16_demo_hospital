from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError

class HospitalPatients(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread']
    _description = "Hospital Doctors Records"
    _rec_name = 'reference' #When we create many2one field by default it shows 'name' field but if I want to specify and field while creating the relation, we can do that by '_rec_name


    name = fields.Char(string="Doctor Name")
    reference = fields.Char(string="Reference")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender", tracking=True)