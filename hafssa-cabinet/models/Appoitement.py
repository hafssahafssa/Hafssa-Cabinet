from odoo import models, fields, api


class CabinetAppoitement(models.Model):

    _name = 'cabinet.appoitement'
    _rec_name = 'motif_consultation'

    patient_id = fields.Many2one('res.partner')
    date_appoi = fields.Date('Date RDV')
    motif_consultation = fields.Char('Motif consultation')







