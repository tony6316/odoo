{
    'name': 'CinéPrex Salle/Site Management',
    'version': '1.0',
    'category': 'Management',
    'summary': 'Gestion des salles et sites pour CinéPrex',
    'depends': ['base'],  # Ajoute ici d'autres dépendances si nécessaire
    'data': [
        'views/site_salle_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,  # Assure-toi que ceci est bien présent
    'application': True,
}
