from odoo import models, fields

class Film(models.Model):
    _name = 'cineprex.film'
    _description = 'Film disponible'

    title = fields.Char(string="Titre", required=True)
    genre = fields.Selection([
        ('action', 'Action'),
        ('comedy', 'Comédie'),
        ('drama', 'Drame'),
        ('horror', 'Horreur'),
        ('sci_fi', 'Science-fiction')
    ], string="Genre", required=True)
    duration = fields.Float(string="Durée (en heures)", required=True)
    release_date = fields.Date(string="Date de sortie", required=True)
