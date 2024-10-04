from odoo import models, fields

class Site(models.Model):
    _name = 'cineprex.site'
    _description = 'Site de cinéma'

    name = fields.Char(string="Nom du Site", required=True)
    city = fields.Char(string="Ville", required=True)
    number_of_rooms = fields.Integer(string="Nombre de salles")

class Salle(models.Model):
    _name = 'cineprex.salle'
    _description = 'Salle de cinéma'

    name = fields.Char(string="Nom de la Salle", required=True)
    capacity = fields.Integer(string="Capacité", required=True)
    site_id = fields.Many2one('cineprex.site', string="Site associé", required=True)
