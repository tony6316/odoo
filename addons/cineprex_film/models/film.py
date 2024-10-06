from odoo import models, fields

class CineprexFilm(models.Model):
    _name = 'cineprex.film'
    _description = 'Gestion des films et des séances'

    name = fields.Char(string="Nom du film", required=True)
    salle_id = fields.Many2one('cineprex.salle', string="Salle", required=True)
    start_time = fields.Datetime(string="Heure de début", required=True)
    end_time = fields.Datetime(string="Heure de fin", required=True)
