from odoo import models, fields, api, _


class HospitalInPatient(models.Model):
    _name = 'hospital.inpatient'
    _description = 'InPatient'
    _order = "id desc"
    _rec_name = "patient_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one('hospital.patient', string='Patient_name', required=True, duplicate=False)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor name', required=True)
    fee = fields.Integer('Doctor Fee', related="doctor_id.doctor_charge")
    room_id = fields.Many2one('hospital.room', string='Room number', required=True)
    admission_date = fields.Date(string='Admit Date', required=True, default=fields.date.today())



