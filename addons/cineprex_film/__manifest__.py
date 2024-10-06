{
    'name': 'CinéPrex Film Management',
    'version': '1.0',
    'category': 'Management',
    'depends': ['base','cineprex'],
    'data': [
        'views/film_views.xml',
        'views/affectation_film_salle_views.xml',  # Assurez-vous d'inclure ce fichier
        'views/film_affectation_menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
