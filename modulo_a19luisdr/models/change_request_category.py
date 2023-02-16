# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ChangeRequest(models.Model):
    _name = 'change.request.category'
    _description = 'Change Request Category'

    change_request_ids = fields.One2many('change.request', 'category_id', string='Child Change Requests')
