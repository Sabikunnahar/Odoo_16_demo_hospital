from odoo import api, fields, models, _, tools

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = "Hospital appointment"
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    ref = fields.Char(string='Reference')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Datetime(string='Booking Date', default=fields.Date.context_today)
    # This gender is the relational filed
    gender = fields.Selection( related='patient_id.gender')

    @api.onchange('patient_id')
    def _onchange_reference(self):
        self.ref = self.patient_id.ref