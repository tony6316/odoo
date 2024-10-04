{
    'name': 'CinéPrex Salle/Site gestion',
    'version': '1.0',
    'category': 'Management',
    'summary': 'Gestion des salles et sites pour CinéPrex',
    'depends': ['base'],  # Ajoute d'autres dépendances si nécessaire
    'data': [
        'views/site_salle_views.xml',  # Assure-toi que ce fichier est bien inclus
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
