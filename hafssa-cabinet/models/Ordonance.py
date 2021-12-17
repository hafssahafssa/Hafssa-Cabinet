from odoo import models, fields, api


class CabinetOrdonance(models.Model):
    _name = 'cabinet.ordonance'

    date_ordo = fields.Date('Date ordonance')

    patient_id = fields.Many2one('res.partner')
    medicament_ids = fields.One2many('ordonance.medicament.lines', 'ordonance_id')


class OrdonanceMedicamentLines(models.Model):
    _name = 'ordonance.medicament.lines'

    ordonance_id = fields.Many2one('cabinet.ordonance')
    medicament_id = fields.Many2one("cabinet.medicament")
    Dosa_medicament = fields.Char('Le dosage du médicament')
    Nbr_fois_Med = fields.Char('Nombre du fois médicament')
    Quantite = fields.Integer('Quantité')


