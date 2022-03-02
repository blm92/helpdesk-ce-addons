# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ticket_line_count = fields.Integer("Tickets líneas", compute='_compute_ticket_line_count')
    ticket_order_count = fields.Integer("Tickets pedido", compute='_compute_ticket_order_count')
    ticket_so_count = fields.Integer("Tickets SO", compute='_compute_ticket_so_count')

    def _compute_ticket_line_count(self):
        for rec in self:
            task_ids = rec.order_line.mapped('task_id').ids
            rec.ticket_line_count = len(self.env['helpdesk.ticket'].search([('task_id','in',task_ids)]))

    def action_open_helpdesk_ticket_line(self):
        task_ids = self.order_line.mapped('task_id').ids
        action = self.env.ref('helpdesk_mgmt.helpdesk_ticket_action').read()[0]
        action['context'] = {}
        action['domain'] = [('task_id', 'in', task_ids)]
        return action

    def _compute_ticket_order_count(self):
        for rec in self:            
            rec.ticket_order_count = len(self.env['helpdesk.ticket'].search([('project_id','in',rec.project_ids.ids)]))

    def action_open_helpdesk_ticket_order(self):        
        action = self.env.ref('helpdesk_mgmt.helpdesk_ticket_action').read()[0]
        action['context'] = {}
        action['domain'] = [('project_id', 'in', self.project_ids.ids)]
        return action

    def _compute_ticket_so_count(self):
        for rec in self:            
            rec.ticket_so_count = len(self.env['helpdesk.ticket'].search([('sale_order_id','=',rec.id)]))

    def action_open_helpdesk_ticket_so(self):        
        action = self.env.ref('helpdesk_mgmt.helpdesk_ticket_action').read()[0]
        action['context'] = {}
        action['domain'] = [('sale_order_id', '=', self.id)]
        return action