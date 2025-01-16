from odoo import api, fields, models, _, tools

class HospitalPatients(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Hospital Patients Records"

    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is Child")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender", tracking=True)
