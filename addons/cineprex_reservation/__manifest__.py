{
    'name': 'Cineprex Reservation',
    'version': '1.0',
    'summary': 'Module pour la réservation de billets en fonction de la capacité des salles et des films',
    'depends': ['cineprex_film'],  # Dépendance au module cineprex_film
    'data': [
        'views/reservation_views.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
}
