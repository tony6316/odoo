{
    'name': 'Cineprex Reservation',
    'version': '1.0',
    'summary': 'Module pour la réservation de billets en fonction de la capacité des salles et des films',
    'depends': ['cineprex_film', 'website'],  # Dépendance au module website
    'data': [
        'views/reservation_views.xml',  # Fichier de vues Odoo incluant le formulaire du site web
        'security/ir.model.access.csv',  # Fichier de sécurité
    ],
    'application': True,
}
