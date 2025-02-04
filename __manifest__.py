{
    'name': 'Hospital Management System',
    'author': 'Sabikun Nahar Bristy',
    'summary': 'For Hospital Management System',
    'sequence': 2,
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/female_patient.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
