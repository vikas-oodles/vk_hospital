from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"
    _rec_name = "patient_id"

    name_seq = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    doctor_name = fields.Many2one('hospital.doctor', string='For Doctor', required=True)
    # doctor_speciality = fields.Text(string='Speciality', related='doctor_id.doctor_speciality')
    notes = fields.Text(string='Registration Note')
    urgency_level = fields.Selection([
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
    ], string='Urgency Level', sort=False, default="a")
    appointment_date = fields.Date(string='Date', required=True, default=fields.date.today())
    appointment_end = fields.Date(string="Appointment End", required=True)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')

        result = super(HospitalAppointment, self).create(vals)
        for rec in self:
            # odoo search method
            patients = rec.env['hospital.patient'].search([])
            print("patients...", patients)
        return result



