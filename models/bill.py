from odoo import models, fields, api, _


class HospitalBill(models.Model):
    _name = 'hospital.bill'
    _description = 'Bill'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'
    _rec_name = 'bill_id'

    @api.onchange('doctor_fee', 'room_charge')
    def _onchange_price(self):
        self.total = self.doctor_fee + self.room_charge

    bill_id = fields.Integer(string='Bill No', required=True, copy=False)
    patient_id = fields.Many2one('hospital.patient', string='Patient name', )
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor Name',ondelete='cascade')
    doctor_fee = fields.Integer('Fee', related='doctor_id.doctor_charge')
    room_charge = fields.Integer('Room Charge', required=True, copy=False)
    total = fields.Integer("Total Charge")



