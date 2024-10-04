from odoo import models, fields

class AffectationFilmSalle(models.Model):
    _name = 'cineprex.affectation_film_salle'
    _description = 'Affectation des films aux salles'

    film_id = fields.Many2one('cineprex.film', string="Film", required=True)
    salle_id = fields.Many2one('cineprex.salle', string="Salle", required=True)
    start_date = fields.Date(string="Date de début", required=True)
    end_date = fields.Date(string="Date de fin", required=True)
