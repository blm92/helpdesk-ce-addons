# -*- coding: utf-8 -*-
{
    'name': 'B92 Cambiar el tipo de facturación en las imputaciones de solicitudes',
    'version': '14.0.1.0.0',
    'summary': 'Cambia el tipo de facturación en las imputaciones de solicitudes.',
    'description': 'Cambia el tipo de facturación en las imputaciones de solicitudes.',
    'category': 'Operations/Helpdesk',
    'author': 'Balmes92',
    'company': 'Balmes92',
    'contributors':  ['Juan Pablo Garza <jp@balmes92.com>'],
    'website': 'https://www.balmes92.com',
    'license': 'AGPL-3',
    'depends': [
            'helpdesk_mgmt_timesheet',
            'hr_timesheet',
            'sale_timesheet',],
    'data': [
            'views/helpdesk_ticket_view.xml',
            # 'views/account_analytic_line_view.xml',
            ],
    'installable': True,
    'auto_install': False,
}
