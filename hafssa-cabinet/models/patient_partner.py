# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api


class CabinetPatientPartner(models.Model):
    _inherit = 'res.partner'


    l_name = fields.Char('Last Name')
    date_naissance = fields.Date('Date de naissance')
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
    CIN = fields.Char("CIN")
    assure = fields.Boolean()
    image = fields.Binary()
    statut = fields.Selection([
        ('client', 'Client'),
        ('premiere_visite', 'Premiére visite')
    ], default='client')
    type = fields.Selection(selection_add=[('patient', "Patient")])
    #type = fields.Selection(selection_add=[('patient', "Patient")],default='patient')
    mode_du_paiement = fields.Selection([('cheque', 'Chéque'), ('espece', 'Espece')])

    ordonance_ids = fields.One2many("cabinet.ordonance", "patient_id")
    appoitement_ids = fields.One2many("cabinet.appoitement", "patient_id")


