from odoo import models, fields

class Film(models.Model):
    _name = 'cineprex.film'
    _description = 'Film disponible au cinéma'

    title = fields.Char(string="Titre", required=True)
    duration = fields.Integer(string="Durée (minutes)", required=True)
    genre = fields.Char(string="Genre", required=True)
    release_date = fields.Date(string="Date de sortie", required=True)
    description = fields.Text(string="Description")

    def name_get(self):
        result = []
        for film in self:
            name = f"{film.title}"
            result.append((film.id, name))
        return result
