from email.policy import default

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
    active = fields.Boolean(default=True) # Uses for archive option. Initially it will show in tree view. But it have to define in form view to show individually


    # When you want to combine two fields while access to many2one relation you can use this function and it has no decorator
    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.reference} - {rec.name}'
            res.append((rec.id, name))
        return res