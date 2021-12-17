import json
from odoo import http
from odoo.http import request, Response


class MxCMedicale(http.Controller):
    
    @http.route('/api/hello', methods=["GET"], auth='none', type='http', csrf=False)
    def hello_hafssa(self, **kw):
        return "Hello Hafssa"

    # API 
    @http.route('/api/patient', methods=["GET"], auth='none', type='json', csrf=False)
    def get_patient(self, **kw):
        patients = request.env['res.partner'].sudo().search([('type', '=', 'patient')])
        print("patients", patients)
        # pour retourner une data
        list_patients = []
        for patient in patients:
            list_patients.append({
                "name": patient.name,
                "sexe": patient.sexe,
                "CIN": patient.CIN,
                "status": patient.statut
            })
        print("patients", list_patients, type(list_patients))    
        return list_patients
    