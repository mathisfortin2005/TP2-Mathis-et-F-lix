"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-04-22
Version 1
"""

import requests

#Création de la classe ClientServeurChalet
class ClientServeurChalet:

    #Constructeur de la classe ClientServeurChalet
    def __init__(self, url_base):
        self.__url_base = url_base
        self.__post_headers = {'Content-Type': 'text/json'}

    #Pour obtenir l'information sur une réservation (point 1 des consignes client)
    def obtenir_infosreservation(self, reservation):
        req = requests.get(self.__url_base + '/reservation/' + reservation)
        print(req.status_code)
        print(req.content)

    #Pour obtenir les informations sur les réservations d'un utilisateur (point 2 des consignes client)
    def obtenir_reservations(self, utilisateur):
        req = requests.get(self.__url_base + '/utilisateur/' + utilisateur)
        print(req.status_code)
        print(req.content)

    #Pour ajouter une réservation (point 3 des consignes client)
    def ajout_reservation(self, nom):
        json_body = '{"nom": "' + nom + '"}'
        req = requests.post(self.__url_base + '/reservation', data=json_body)
        print(req.status_code)
        print(req.content)

    #Pour remplacer une réservation (point 4 des consignes client)
    def remplacer_reservation(self, nom):
        json_body = '{"nom": "' + nom + '"}'
        req = requests.put(self.__url_base + '/reservation', data=json_body)
        print(req.status_code)
        print(req.content)

    #Pour supprimer une réservation (point 5 des consignes client)
    def supprimer_reservation(self, nom):
        json_body = '{"nom": "' + nom + '"}'
        req = requests.delete(self.__url_base + '/reservation', data=json_body)
        print(req.status_code)
        print(req.content)

    #Pour ajouter un utilisateur (point 6 consignes client)
    def ajout_utilisateur(self, reservation, utilisateur):
        json_body = '{"nom": "' + utilisateur + '" }'
        req = requests.post(self.__url_base + '/reservation/' + reservation, data=json_body)
        print(req.status_code)
        print(req.content)

    #MATHIS: Je ne comprend pas trop ce qu'il faut faire et comment reconnaitre un administrateur
    #Pour administrateur, pour renvoyer toutes les réservations
    def liste_reservation(self):
        pass

#Code de test
client = ClientServeurChalet('http://localhost:8000')

#MATHIS: Cette partie de code de test est à retravailler (mettre les bons paramètres)
client.obtenir_infosreservation('laurentien')
client.obtenir_reservations('antarctic')
client.ajout_reservation('laurentien', 'Bill le castor')
client.remplacer_reservation('laurentien', 'Paulette la belette')
client.supprimer_reservation('laurentien', 'Karen le furet')
client.ajout_utilisateur('antarctic', 'Sylvain le pingouin')
client.liste_reservation('laurentien')


"""
#Importation de impex
from impex import impex

#Définition de la classe Reservation
class Reservation():

    #Constructeur de la classe Reservation
    def __init__(self):
        Reservation.__id = ''
        Reservation.__chalet = ''

    #Méthode qui retourne l'information sur la réservation
    def do_GET_reservation(self):
        with open('', 'rt'):
            return()

    #Méthode qui retourne toutes les réservations de l'utilisateur
    def do_GET_reservations(self):
        pass

    #Méthode qui ajoute une réservation
    def do_POST_reservation(self):
        with open('reservationId', 'w'):
            pass

    #Méthode qui remplace une réservation
    def do_PUT_reservation(self):
        pass


    #Méthode qui supprime une réservation
    def do_DELETE_reservation(self):
        pass


    #Méthode qui renvoie toutes les réservations triées par ordre de reservationld (pour les administrateurs)
    def do_GET_reservations(self):
        pass


#Définition de la classe Utilisateur
class Utilisateur():

    #Constructeur de la classe Utilisateur
    def __init__(self):


    #Méthode qui ajoute un utilisateur:
    def do_POST_utilisateur(self):
        pass



#Code pour les tests
"""
