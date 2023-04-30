"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-04-29 12:12:03
Version 1
"""
#FIXME: Les méthodes de la classe ClientServeurChalet me semblent trop simples non? (JE PENSE QUE C'EST CORRECT)

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
#FIXME: Pas certain de celui-là (il est correct)
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

    #our ajouter un utilisateur (point 6 consignes client)
    def ajout_utilisateur(self, utilisateur):
        json_body = '{"nom": "' + utilisateur + '" }'
        req = requests.post(self.__url_base + '/utilisateur/' + utilisateur, data=json_body)
        print(req.status_code)
        print(req.content)

#TODO: @Félix: Faire les 3 méthodes restantes (FAIT, il reste juste à confirmer que ça fonctionne)

    def liste_reservations(self): #Pas sur de ça
        req = requests.get(self.__url_base + '/reservations/' + reservation)
        items = req.json()
        print(items.sort())

    def ajout_chalet(self, chalet):
        json_body = '{"nom": "' + chalet + '" }'
        req = requests.post(self.__url_base + '/chalet/' + chalet, data=json_body)
        print(req.status_code)
        print(req.content)

    def informations_chalet(self, chalet):
        req = requests.get(self.__url_base + '/chalet/' + chalet)
        print(req.status_code)
        print(req.content)

    def disponibilité_chalet(self, plage): #Pas sur de savoir comment faire, mais je pense que ça te donne les différentes plages horaire
        req = requests.get(self.__url_base + '/plage/' + plage)
        print(req.status_code)
        print(req.content)

#Code de test
client = ClientServeurChalet('http://localhost:8000')
