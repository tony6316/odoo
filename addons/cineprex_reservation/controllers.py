from odoo import http
from odoo.http import request

class ReservationController(http.Controller):

    @http.route('/reservation', type='http', auth="public", website=True)
    def reservation_form(self, **kwargs):
        # Récupération des films, salles et séances pour afficher dans le formulaire
        films = request.env['cineprex.film'].sudo().search([])
        salles = request.env['cineprex.salle'].sudo().search([])
        seances = request.env['cineprex.seance_film_salle'].sudo().search([])

        # Rendu de la page avec les éléments requis pour le formulaire
        return request.render('cineprex_reservation.reservation_form_template', {
            'films': films,
            'salles': salles,
            'seances': seances,
            'error': kwargs.get('error')
        })
        
@http.route('/create_reservation', type='http', auth="public", methods=['POST'], website=True)
def create_reservation(self, **post):
    try:
        # ... (récupération des données comme avant)

        # Création de la réservation
        request.env['cineprex.reservation'].sudo().create({
            'film_id': film_id,
            'salle_id': salle_id,
            'session_id': session_id,
            'seat_count': seat_count,
            'customer_name': customer_name,
        })

        # Rediriger vers la page de succès
        return request.render('cineprex_reservation.reservation_success_template')

    except Exception as e:
        # Log l'erreur pour le débogage
        _logger.error("Erreur lors de la création de la réservation: %s", e)
        return request.redirect('/reservation?error=' + str(e))