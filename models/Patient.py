# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api


class CabinetPatient(models.Model):
    _name = 'cabinet.patient'
    # _inherit = 'hr.employee'
    _rec_name = 'f_name'

    f_name = fields.Char(required=True)
    l_name = fields.Char('Last Name')
    date_naissance = fields.Date('Date de naissance')
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
    CIN = fields.Char("CIN")
    assure = fields.Boolean()
    phone = fields.Char()
    image = fields.Binary()
    prix = fields.Integer(default=300)
    tax = fields.Float(computed="calc_tax" ,store=True)
    net_prix = fields.Float(computed="calc_tax")
    statut=fields.Selection([
        ('client','Client'),
        ('premiere_visite','Premiére visite')
    ],default='client')

    _sql_constraints = [
        ("uniquel_name", "unique (l_name)","Ce patient est déja exist"),
        #("uniquelCIN", "unique (CIN)", "Ce patient est déja exist"),

        ]


    @api.depends("prix")
    def calc_tax(self):
        for patient in self:
            patient.tax = patient.prix * 0.20
            patient.net_prix = patient.prix - patient.tax


    def premiere_visite(self):
        self.statut='premiere_visite'



    @api.onchange("prix")
    def _on_change_sexe(self):
        if self.sexe == 'female':
            self.prix = 250
        else:
            self.prix = 300


