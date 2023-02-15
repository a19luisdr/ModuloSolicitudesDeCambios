# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    change_request_ids = fields.One2many('change.request', 'applicant_id', string='Published Change Requests')