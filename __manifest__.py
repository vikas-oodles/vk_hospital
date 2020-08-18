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
        'views/patient.xml',
        'views/appointment.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto-install': False,

}