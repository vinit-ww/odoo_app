# -*- coding: utf-8 -*-
from odoo import http

# class Assets(http.Controller):
#     @http.route('/assets/assets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assets/assets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('assets.listing', {
#             'root': '/assets/assets',
#             'objects': http.request.env['assets.assets'].search([]),
#         })

#     @http.route('/assets/assets/objects/<model("assets.assets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assets.object', {
#             'object': obj
#         })