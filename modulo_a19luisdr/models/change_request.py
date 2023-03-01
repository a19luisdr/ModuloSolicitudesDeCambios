# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ChangeRequest(models.Model):
    _name = 'change.request'
    _description = 'Change Request'

    name = fields.Char('Request Title', required=True)
    request_date = fields.Date('Request Date')
    description = fields.Char('Request Description', required=True)
    done = fields.Boolean('Done')
    applicant_id = fields.Many2one('res.partner', string='Applicants')
    category_id = fields.Many2one('change.request.category', string='Category')

class ResPartner(models.Model):
    _inherit = 'res.partner'

    change_request_ids = fields.One2many('change.request', 'applicant_id', string='Published Change Requests')