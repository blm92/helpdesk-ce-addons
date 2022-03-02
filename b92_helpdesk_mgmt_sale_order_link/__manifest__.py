# -*- coding: utf-8 -*-
{
    'name': 'B92 link entre ordenes de venta y tickets de helpdesk.',
    'version': '14.0.1.0.0',
    'summary': 'Permite navegar desde la orden de venta a los tickets asociados.',
    'description': 'Permite navegar desde la orden de venta a los tickets asociados.',
    'category': 'Operations/Helpdesk',
    'author': 'Balmes92',
    'company': 'Balmes92',
    'contributors':  ['Juan Pablo Garza <jp@balmes92.com>'],
    'website': 'https://www.balmes92.com',
    'license': 'AGPL-3',
    'depends': [
            'helpdesk_mgmt_project',
            'b92_helpdesk_mgmt_sale',
        ],
    'data': [
        'views/sale_order_views.xml',
        ],        
    'installable': True,
    'auto_install': False,
}
