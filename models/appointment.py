from odoo import api, fields, models, _, tools

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = "Hospital appointment"
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    ref = fields.Char(string='Reference', help="This is for appointment Reference") #Suppose when you hover into the button you want to show some msg, then you can do by 'help'
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Datetime(string='Booking Date', default=fields.Date.context_today)
    # This gender is the relational filed
    gender = fields.Selection( related='patient_id.gender')
    prescription = fields.Html(string='Prescription', tracking=True)
    # for priority widget batch
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('progress', 'Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], default='draft')


    @api.onchange('patient_id')
    def _onchange_reference(self):
        self.ref = self.patient_id.ref

    def test_object_button(self):
        print("Object Button Called")
        # This is for showing a rainbow msg in the UI
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Hey! Thank you for clicking',
                'type': 'rainbow_man',
            }
        }