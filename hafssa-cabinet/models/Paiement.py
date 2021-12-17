from odoo import models, fields, api


class CabinetPaiement(models.Model):

    _inherit = 'sale.order'

    mode_du_paiement = fields.Selection([('cheque', 'Chéque'), ('espece', 'Espéce')])
    diagnostic = fields.Text()
    prix = fields.Integer()
    tax = fields.Integer()






