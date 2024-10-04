from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SeanceFilmSalle(models.Model):
    _name = 'cineprex.seance_film_salle'
    _description = 'Séance des films dans les salles'

    film_id = fields.Many2one('cineprex.film', string="Film", required=True)
    salle_id = fields.Many2one('cineprex.salle', string="Salle", required=True)
    start_time = fields.Datetime(string="Heure de début", required=True)
    end_time = fields.Datetime(string="Heure de fin", required=True)

    # Ajout de la vérification de chevauchement de séances
    @api.constrains('salle_id', 'start_time', 'end_time')
    def _check_time_overlap(self):
        for record in self:
            overlapping_seances = self.env['cineprex.seance_film_salle'].search([
                ('salle_id', '=', record.salle_id.id),
                ('id', '!=', record.id),
                ('start_time', '<', record.end_time),
                ('end_time', '>', record.start_time)
            ])
            if overlapping_seances:
                raise ValidationError("Une autre séance est déjà programmée dans cette salle pour cet horaire.")
