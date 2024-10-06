{
    'name': 'Gestion des Films et Séances',
    'version': '1.0',
    'summary': 'Répertorier les films disponibles et gérer les séances de cinéma',
    'author': 'Ton Nom',
    'category': 'Management',
    'depends': ['base'],
    'data': [
        'views/film_views.xml',
        'views/seance_views.xml',
        'views/menu.xml',  # Assurez-vous que ce fichier est bien référencé ici
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
