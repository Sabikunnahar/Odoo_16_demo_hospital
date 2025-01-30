from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError

class HospitalPatients(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Hospital Patients Records"

    name = fields.Char(string="Name", required=True, tracking=True) #tracking is use to show the changes values in the chatter
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is Child", default=False)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender", tracking=True)
    capitalized_name = fields.Char(string="Capitalized Name" , compute="_compute_capitalized_name")
    ref = fields.Char('Name', default=lambda self: _('New'), readonly=True, tracking=True)
    #This 'default=lambda self: _('New')' will the value New initially

    doctor_id=fields.Many2one('hospital.doctor', string="Doctor Name")
    tag_ids = fields.Many2many(
        'res.partner.category',  # Target model
        'hospital_patient_rel',  # Name of the relational table
        'patient_id',  # Column for the current model (`hospital.patient`)
        'tag_id',  # Column for the target model (`res.partner.category`)
        string="Tags"
    )
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                               ('ongoing', 'Ongoing'), ('done', 'Done'), ('cancel', 'Cancel')])

    # This is default/origin build in create function of odoo
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatients, self).create(vals_list)

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
