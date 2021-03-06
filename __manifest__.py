{
    'name':'Hospital Management',
    'version':'12.0.1.0.0',
    'category':'Extra Tools',
    'summary': 'Module for managing the hospital',
    'sequence': '55',
    'author':'vikas kumar',
    'maintainer':'odoo mates',
    'website':'odoomate.com',
    'depends':["base","sale_management","stock","account","mail","sale"],
    'demo':[],
    'data':[
        'wizards/create_appointment.xml',
        'views/patient.xml',

        'views/appointment.xml',
        'views/doctor.xml',
        'views/inpatient.xml',
        'views/room.xml',
        'views/bill.xml',
        'views/disease.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/data.xml',

        
    ],
    'installable': True,
    'application': True,
    'auto-install': False,

}