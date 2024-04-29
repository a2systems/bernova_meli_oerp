# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from unicodedata import name
from dateutil.relativedelta import relativedelta
from datetime import date,datetime,timedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import ValidationError

class ResCompany(models.Model):
    _inherit = 'res.company'

    def cron_meli_orders(self):
        res = super(ResCompany, self).cron_meli_orders()
        prods_me1_zip = self.env['product.template'].search([('default_code','=','ME1 - zip')])
        for prod_m1_zip in prods_me1_zip:
            prod_m1_zip.active = False
        prods_prioritario = self.env['product.template'].search([('name','=','Prioritario')])
        for prod_prioritario in prods_prioritario:
            prod_prioritario.active = False
        return res
