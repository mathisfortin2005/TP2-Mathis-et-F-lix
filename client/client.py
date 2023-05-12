"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-05-11 19:58:37
Version 1
"""

# TODO: @Felix - Test unitaire pour chaque méthode

import requests
import unittest as ut


# Création de la classe ClientServeurChalet qui contient l'ensemble des commandes que le client peut faire
class ClientServeurChalet:

    # Constructeur de la classe ClientServeurChalet
    def __init__(self, url_base):
        self.__url_base = url_base
        self.__post_headers = {'Content-Type': 'text/json'}

    # Pour obtenir l'information sur une réservation (point 1 des consignes client)
    def obtenir_infosreservation(self, reservation):
        req = requests.get(self.__url_base + '/reservation/' + reservation)
        print(req.status_code)
        print(req.content)

    # Pour obtenir les informations sur les réservations d'un utilisateur (point 2 des consignes client)
    def obtenir_reservations(self, utilisateur):
        req = requests.get(self.__url_base + '/utilisateur/' + utilisateur)
        print(req.status_code)
        print(req.content)

    # Pour ajouter une réservation (point 3 des consignes client)
    def ajout_reservation(self, nom):
        json_body = '{"nom": "' + nom + '"}'
        req = requests.post(self.__url_base + '/reservation', data=json_body)
        print(req.status_code)
        print(req.content)

    # Pour remplacer une réservation (point 4 des consignes client)
    def remplacer_reservation(self, nom):
        json_body = '{"nom": "' + nom + '"}'
        req = requests.put(self.__url_base + '/reservation', data=json_body)
        print(req.status_code)
        print(req.content)

    # Pour supprimer une réservation (point 5 des consignes client)
    def supprimer_reservation(self, nom):
        json_body = '{"nom": "' + nom + '"}'
        req = requests.delete(self.__url_base + '/reservation', data=json_body)
        print(req.status_code)
        print(req.content)

    # Pour ajouter un utilisateur (point 6 consignes client)
    def ajout_utilisateur(self, utilisateur):
        json_body = '{"nom": "' + utilisateur + '" }'
        req = requests.post(self.__url_base + '/utilisateur/' + utilisateur, data=json_body)
        print(req.status_code)
        print(req.content)

    # Pour obtenir toutes les réservations triées par ordre croissant de leur ID (point 7 consignes client)
    def liste_reservations(self, reservations):
        req = requests.get(self.__url_base + '/reservations/' + reservations)
        items = req.json()
        print(items.sort())

    def liste_chalets(self, chalets):
        req = requests.get(self.__url_base + '/chalets/' + chalets)
        items = req.json()
        print(items.sort())

    def liste_utilisateurs(self, utilisateurs):
        req = requests.get(self.__url_base + '/utilisateurs/' + utilisateurs)
        items = req.json()
        print(items.sort())

    # Pour ajouter un chalet (point 8 consignes client)
    def ajout_chalet(self, chalet):
        json_body = '{"nom": "' + chalet + '" }'
        req = requests.post(self.__url_base + '/chalet/' + chalet, data=json_body)
        print(req.status_code)
        print(req.content)

    # Pour retourner les informations d'un chalet (point 9 consignes client)
    def informations_chalet(self, chalet):
        req = requests.get(self.__url_base + '/chalet/' + chalet)
        print(req.status_code)
        print(req.content)

    # Pour créer une plage de disponibilité pour le chalet
    def disponibilite_chalet(self, plage):
        req = requests.get(self.__url_base + '/plage/' + plage)
        print(req.status_code)
        print(req.content)

#Tests unitaires
class Testobtenir_infosreservation(ut.TestCase):

    def test_split(self, req):
        s = req
        self.assertEqual(s.split(),req,'reservation')

        with self.assertRaises(TypeError) :
            s.split(2)
class Testinformationschalet(ut.TestCase):

    def test_split(self, req):
        s = req
        self.assertEqual(s.split(), req, 'chalet')

        with self.assertRaises(TypeError):
            s.split(2)

class Testdisponibilite_chalet(ut.TestCase):

    def test_split(self, req):
        s = req
        self.assertEqual(s.split(), req, 'plage')

        with self.assertRaises(TypeError):
            s.split(2)


# Code de test
client = ClientServeurChalet('http://localhost:8000')
