# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ChangeRequest(models.Model):
    _name = 'change.request.category'
    _description = 'Change Request Category'

    name = fields.Char('Request Title', required=True)
    date_release = fields.Date('Request Date')
    author_id = fields.Many2one('applicant', string='Applicants')
    category_id = fields.Many2one('library.book.category', string='Category')