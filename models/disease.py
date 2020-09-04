from odoo import models, fields, api, _


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'
    _rec_name = 'disease_name'

    disease_name = fields.Selection([
        ('fever', 'Fever'),
        ('cold', 'Cold'),
        ('corona', 'Corona'),
    ], default='fever', required=True)
    disease_severity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], required=True, default='low')
    patient_id = fields.Many2one('hospital.patient', string='Patient Id')



