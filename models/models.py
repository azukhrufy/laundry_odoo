# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _
 
class LaundryOrder(models.Model):
    _inherit = 'sale.order'
 
    laundry = fields.Boolean('Laundry')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('open', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')
    
    date_order = fields.Date(string='Order Date', required=True, readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Date.today)
    
    def tanggal_selesai(self):
        return fields.Date.to_string(datetime.now() + timedelta(2))
    
    commitment_date = fields.Date('Commitment Date', states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, oldname='requested_date', readonly=True, default=tanggal_selesai)
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, track_visibility='onchange', track_sequence=2, default=lambda self: self.env.user, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    
    def print_laundry_order(self):
        return self.env.ref('laundry_odoo.action_laundry_order').report_action(self)
    
    def print_laundry_label(self):
        return self.env.ref('laundry_odoo.action_laundry_label').report_action(self)
    
    @api.multi
    def action_confirm(self):
        super(LaundryOrder, self).action_confirm()
        if self.laundry:
            self.write({'state': 'open'})
        return True
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if vals.get('laundry'):
                vals['name'] = self.env['ir.sequence'].next_by_code('laundry.order')
            else:
                if 'company_id' in vals:
                    vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('sale.order') or _('New')
                else:
                    vals['name'] = self.env['ir.sequence'].next_by_code('sale.order') or _('New')
        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            addr = partner.address_get(['delivery', 'invoice'])
            vals['partner_invoice_id'] = vals.setdefault('partner_invoice_id', addr['invoice'])
            vals['partner_shipping_id'] = vals.setdefault('partner_shipping_id', addr['delivery'])
            vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist and partner.property_product_pricelist.id)
        
        result = super(LaundryOrder, self).create(vals)
        return result
    
    

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def print_receipt(self):
        return self.env.ref('laundry_odoo.action_report_receipt').report_action(self)