from odoo import models, fields

class Seance(models.Model):
    _name = 'cineprex.seance'
    _description = 'Séance de cinéma'

    film_id = fields.Many2one('cineprex.film', string="Film", required=True)
    salle_id = fields.Char(string="Salle", required=True)  # Tu peux remplacer par un Many2one si tu as un modèle de salle
    date = fields.Date(string="Date", required=True)
    start_time = fields.Datetime(string="Heure de début", required=True)
    end_time = fields.Datetime(string="Heure de fin", required=True)
