# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ChangeRequest(models.Model):
    _name = 'change.request'
    _description = 'Change Request'

    name = fields.Char('Request Title', required=True)
    request_date = fields.Date('Request Date')
    description = fields.Char('Request Description', required=True)
    done = fields.Boolean('Done')
    days_age = fields.Integer('Days since the request date', compute='_compute_days_age', store=False, compute_sudo=True)
    applicant_id = fields.Many2one('res.partner', string='Applicants')
    category_id = fields.Many2one('change.request.category', string='Category')

    @api.depends('request_date')
    def _compute_days_age(self):
        today = fields.Date.today()
        for request in self.filtered('request_date'):
            if request.request_date:
                delta = today - request.request_date
                request.days_age = delta.days
            else:
                request.days_age = 0

class ResPartner(models.Model):
    _inherit = 'res.partner'

    change_request_ids = fields.One2many('change.request', 'applicant_id', string='Published Change Requests')