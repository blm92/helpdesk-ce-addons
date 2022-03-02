# -*- coding: utf-8 -*-
{
    'name': 'b92_helpdesk_mgmt_sale',
    'version': '14.0.1.0.0',
    'summary': 'Vincula las APPs de Ventas y Helpdesk(OCA)',
    'description': 'Vincula las APPs de Ventas y Helpdesk(OCA)',
    'category': 'Operations/Helpdesk',
    'author': 'Balmes92',
    'company': 'Balmes92',
    'contributors':  ['Juan Pablo Garza <jp@balmes92.com>'],
    'website': 'https://www.balmes92.com',
    'license': 'AGPL-3',
    'depends': [
            'helpdesk_mgmt',
            'sale_management',
        ],
    'data': [
        'views/helpdesk_views.xml',
        ],        
    'installable': True,
    'auto_install': False,
}
