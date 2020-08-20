from odoo import models, fields, api, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'doctor_name'
    _order = "id desc"

    # name_seq = fields.Char(string='Doctor ID', required=True, copy=False, readonly=True,
    #                        index=True, default=lambda self: _('New'))
    doctor_name = fields.Char(string='Doctor Name', required=True)
    doctor_image = fields.Binary(string="Image", required=False)
    doctor_age = fields.Integer(string="Age")
    doctor_charge = fields.Integer(string="Doctor Fee", required=True, default='200')
    doctor_speciality = fields.Selection([
        ('cardiology', 'Cardiology'),
        ('oncology', 'Oncology'),
        ('neurology', 'Neurology'),
        ('Urology', 'Urology'),
        ('surgeon', 'Surgical Gastroenterology'),
        ('general_physician', 'General Physician'),
    ], string='Speciality', sort=True, default='general_physician', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', sort=False, default="male", required=True)
    doctor_address = fields.Text(string="Address", required=False)
