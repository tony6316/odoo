from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Reservation(models.Model):
    _name = 'cineprex.reservation'
    _description = 'Réservation de billets'

    film_id = fields.Many2one('cineprex.film', string="Film", required=True)
    salle_id = fields.Many2one('cineprex.salle', string="Salle", required=True)
    customer_name = fields.Char(string="Nom du client", required=True)
    seat_count = fields.Integer(string="Nombre de places", required=True)
    reservation_date = fields.Datetime(string="Date de réservation", default=fields.Datetime.now, required=True)

    # Nouveau champ Many2one pour choisir la séance (affectation film/salle)
    session_id = fields.Many2one('cineprex.affectation_film_salle', string="Séance", required=True, domain="[('salle_id', '=', salle_id), ('start_date', '<=', reservation_date), ('end_date', '>=', reservation_date)]")

    # Champ calculé pour vérifier la capacité restante
    remaining_capacity = fields.Integer(string="Capacité restante", compute='_compute_remaining_capacity', store=True)

    @api.depends('salle_id', 'seat_count', 'session_id')
    def _compute_remaining_capacity(self):
        for record in self:
            if record.session_id:
                max_capacity = record.session_id.salle_id.capacity
                # Rechercher toutes les réservations pour cette salle et cette séance
                domain = [
                    ('session_id', '=', record.session_id.id),
                ]
                if record.id:
                    domain.append(('id', '!=', record.id))  # Exclure la réservation en cours si elle est déjà en base

                # Rechercher les réservations pour cette séance
                reservations = self.env['cineprex.reservation'].search(domain)
                total_reserved = sum(reservations.mapped('seat_count'))
                record.remaining_capacity = max_capacity - total_reserved
            else:
                record.remaining_capacity = 0

    @api.constrains('seat_count', 'session_id')
    def _check_seat_availability(self):
        for record in self:
            if record.seat_count > record.remaining_capacity:
                raise ValidationError("Le nombre de places réservées dépasse la capacité restante de la salle pour cette séance.")
