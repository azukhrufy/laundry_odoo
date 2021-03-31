# -*- coding: utf-8 -*-
from odoo import http

# class LaundryOdoo(http.Controller):
#     @http.route('/laundry_odoo/laundry_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/laundry_odoo/laundry_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('laundry_odoo.listing', {
#             'root': '/laundry_odoo/laundry_odoo',
#             'objects': http.request.env['laundry_odoo.laundry_odoo'].search([]),
#         })

#     @http.route('/laundry_odoo/laundry_odoo/objects/<model("laundry_odoo.laundry_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('laundry_odoo.object', {
#             'object': obj
#         })