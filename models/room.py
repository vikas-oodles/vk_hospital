from odoo import models, fields, api, _


class HospitalRoom(models.Model):
    _name = 'hospital.room'
    _description = 'Room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'
    _rec_name = 'room_no'

    room_no = fields.Char(string="Room No", required=True,)
    room_type = fields.Selection([
        ('a', 'A Class'),
        ('b', 'B Class'),
        ('c', 'C Class'),
    ], default='a', required=True,)
    status = fields.Boolean(string="IsEmpty", default='True', required=True)