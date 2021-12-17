# -*- coding: utf-8 -*-


from odoo import models, fields, api


class CabinetMedicament(models.Model):

    _name = 'cabinet.medicament'

    _rec_name = 'NomMed'

    NomMed = fields.Char('Nom médicament')
    Description = fields.Char('Description')
    ordonance_ids = fields.One2many('ordonance.medicament.lines', "medicament_id")
