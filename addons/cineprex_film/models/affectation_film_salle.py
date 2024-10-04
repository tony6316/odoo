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


class Reservation(models.Model):
    _name = 'cineprex.reservation'
    _description = 'Réservation de billets'

    film_id = fields.Many2one('cineprex.film', string="Film", required=True)
    salle_id = fields.Many2one('cineprex.salle', string="Salle", required=True)
    customer_name = fields.Char(string="Nom du client", required=True)
    seat_count = fields.Integer(string="Nombre de places", required=True)
    reservation_date = fields.Datetime(string="Date de réservation", default=fields.Datetime.now)
    session_id = fields.Many2one('cineprex.seance_film_salle', string="Séance", domain="[('salle_id', '=', salle_id), ('start_time', '<=', reservation_date), ('end_time', '>=', reservation_date)]")

    # Champ calculé pour vérifier la capacité restante
    remaining_capacity = fields.Integer(string="Capacité restante", compute='_compute_remaining_capacity', store=True)

    @api.depends('salle_id', 'session_id', 'seat_count')
    def _compute_remaining_capacity(self):
        for record in self:
            max_capacity = record.salle_id.capacity
            total_reserved = sum(self.env['cineprex.reservation'].search([
                ('film_id', '=', record.film_id.id),
                ('salle_id', '=', record.salle_id.id),
                ('session_id', '=', record.session_id.id)
            ]).mapped('seat_count'))
            record.remaining_capacity = max_capacity - total_reserved

    @api.constrains('seat_count')
    def _check_seat_availability(self):
        for record in self:
            if record.seat_count > record.remaining_capacity:
                raise ValidationError("Le nombre de places réservées dépasse la capacité restante de la salle.")
