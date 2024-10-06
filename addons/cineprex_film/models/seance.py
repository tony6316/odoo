from odoo import models, fields

class Seance(models.Model):
    _name = 'cineprex.seance'
    _description = 'Séance'

    film_id = fields.Many2one('cineprex.film', string="Film", required=True)
    salle_id = fields.Many2one('cineprex.salle', string="Salle", required=True)
    start_time = fields.Datetime(string="Heure de début", required=True)
    end_time = fields.Datetime(string="Heure de fin", required=True)
