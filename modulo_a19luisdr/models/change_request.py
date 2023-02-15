# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ChangeRequest(models.Model):
    _name = 'change.request'
    _description = 'Change Request'

    name = fields.Char('Request Title', required=True)
    date_release = fields.Date('Request Date')
    applicant_ids = fields.Many2many('res.partner', string='Applicants')
    category_id = fields.Many2one('change.request.category', string='Category')