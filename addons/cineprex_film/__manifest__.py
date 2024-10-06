{
    'name': 'Cinéfilm Management',
    'version': '1.0',
    'category': 'Cinema',
    'summary': 'Gestion des films et des séances',
    'description': """
        Module pour gérer les films et les séances. Les films peuvent être associés à des séances
        qui sont tenues dans des salles spécifiques.
    """,
    'author': 'Votre Nom',
    'depends': ['cineprex'],  # Dépend du module Cineprex pour les salles
    'data': [
        'views/film_views.xml',
        'views/seance_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
