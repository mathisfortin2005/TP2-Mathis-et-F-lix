"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-05-12 20:44:07
Version 1
"""

# Importation des modules nécessaires au serveur
import client
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import gzip

# Création de la classe Réservation qui sert à créer des objets réservations
import client
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


# Création de la classe SuperChalet() qui sert à mettre toutes les classes dans une même classe
class SuperChalet:
    def __init__(self):
        self.__utilisateurs = []
        self.__plages = []
        self.__chalets = []

    # Méthodes GETTER ET SETTER
    @property
    def chalets(self):
        return self.__chalets

    @chalets.setter
    def chalets(self, x):
        self.__chalets = x
        pass

    @property
    def utilisateurs(self):
        return self.__utilisateurs

    @property
    def plage(self):
        return self.__plages

    @plage.setter
    def plage(self, x):
        self.__plages = x

    # Méthode pour obtenir les informations d'une réservation
    def obtenirInfosReservation(self, id):
        id = None
        file = f'./voute/{id}.res.gz'
        if os.path.exists(file):
            with gzip.open(file, 'rb') as info:
                inforeservations = info.read()
                id = json.loads(inforeservations.decode('utf-8'))

        return id

    # Méthode pour obtenir le email d'un utilisateur associé à une réservation
    def obtenirEmailReservation(self, email):
        if email not in self.__utilisateurs:
            raise ValueError("Aucun utilisateur n'a le courriel suivant:" + email)
        else:
            for x in range(len(self.__utilisateurs)):  # La variable x sert d'itérateur
                infosutilisateur = self.__utilisateurs[x]
                if infosutilisateur.index(email) != -1:
                    pass

            return infosutilisateur

    # Méthode pour obtenir les informations sur toutes les réservations d'un utilisateur
    def obtenirReservations(self, utilisateur):
        for x in range(len(self.__reservations)):  # La variable x sert d'itérateur
            infosreservation = self.__reservations[x]
            if infosreservation.index(utilisateur) != -1:
                pass

            return infosreservation

    # Méthode pour ajouter une réservation
    def ajoutReservation(self, id, chalet, utilisateur, plage):
        if id not in self.__id.keys():
            raise ValueError('Cette réservation existe déjà')
        else:
            self.__reservations = self.__reservations.append([id, chalet, utilisateur, plage])

    # Méthode pour remplacer une réservation
    def remplacerReservation(self, id_reservation_a_remplacer):
        for x in range(len(self.__reservations)):
            infosreservation = self.__reservations[x]
            if infosreservation.index(id) != id_reservation_a_remplacer:
                del (self.__reservations[x])
                infosreservation.append(id_reservation_a_remplacer)

    # Méthode pour supprimer une réservation
    def supprimerReservation(self, id):
        for x in range(len(self.__reservations)):
            infosreservation = self.__reservations[x]
            if infosreservation.index(id) != -1:
                del (self.__reservations[x])

    # Méthode pour retourner la liste des réservations
    def listeReservation(self):
        return self.__reservations

    # Méthode pour ajouter une objet Chalet
    def ajoutChalet(self, id, nom, url_image, longitude, latitude):
        if id in self.__id and nom in self.__nom and latitude in self.__latitude and longitude in self.__longitude:
            raise ValueError('Ce chalet existe déjà')
        else:
            self.__chalets = self.__chalets.append([id, nom, url_image, [longitude, latitude]])

    # Méthode pour obtenir les informations sur un chalet
    def infoChalet(self, id):
        for chalet in self.chalets:
            if id == chalet["id"]:
                return chalet

# Classe permettant de gérer les requêtes envoyées par le client
class TPBaseHTTPRequestHandler(BaseHTTPRequestHandler):
    super_chalet = SuperChalet()
    chalets = super_chalet.chalets
    utilisateurs = super_chalet.utilisateurs

    # Point d'entrée pour toutes les requêtes de type GET
    def do_GET(self):
        headers = self.headers
        path = self.path

        if path.startswith('/reservation/'):
            path2 = path.split('/')[2]
            reservation = self.super_chalet.obtenirInfosReservation(path2)
            email = self.super_chalet.obtenirEmailReservation(path2)

            if reservation != None:
                body = json.dumps(reservation)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(str(body), 'utf-8'))
                print('Reservation trouve, Reservation : \n' + str(body))

            elif len(email) != 0:
                body = json.dumps(email)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(str(body), 'utf-8'))
                print("Adresse trouve,  Reservations : \n" + str(body))
            else:
                self.send_response(542, 'Chemin Non trouve')
                self.end_headers()

        elif path.startswith('/chalet/'):
            path2 = path.split('/')[2]
            body = self.super_chalet.infoChalet(path2)
            if body != None:
                body = json.dumps(body)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(str(body), 'utf-8'))
            else:
                self.send_response(542, 'Chalet non trouve')
                self.end_headers()

        elif path == '/reservation':
            body = json.dumps(self.super_chalet.listeReservation())
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(str(body), 'utf-8'))
            print(body)

        else:
            self.send_response(542, 'Chemin Non trouve')
            self.end_headers()

    # Permet de gérer l'ajout de réservations, de chalets et d'utilisateurs
    def do_POST(self):

        path = self.path

        if path == '/reservation':
            content_length = int(self.headers['Content-Length'])
            reservations = json.loads(self.rfile.read(content_length))
            if not self.super_chalet.reserveExists(reservations):
                self.super_chalet.postReservation(reservations)
                self.send_response(200, 'Plage Ajoute')
            else:
                self.send_response(542, 'Reservation Deja Existante')

        if path == '/utilisateur':
            try:
                content_length = int(self.headers['Content-Length'])
                utilisateur = json.loads(self.rfile.read(content_length))
                self.utilisateurs.append(utilisateur)
                self.send_response(200, 'Utilisateur Enregistre')
            except json.JSONDecodeError:
                self.send_response(542, 'mauvais format')

        if path == '/chalet':
            try:
                content_length = int(self.headers['Content-Length'])
                chalet = json.loads(self.rfile.read(content_length))
                self.chalets.append(chalet)
                self.send_response(200, 'chalet Enregistre')
            except json.JSONDecodeError:
                self.send_response(542, 'mauvais format')

        self.end_headers()


# Classe pour utiliser le serveur
class ServeurTest:
    @staticmethod
    def run(serveur_class=HTTPServer, serveur_port=8000, handler_class=TPBaseHTTPRequestHandler):
        serveur_adresse = ('', serveur_port)
        httpd = serveur_class(serveur_adresse, handler_class)
        httpd.serve_forever()


# Code pour l'exécution du test
serveur = ServeurTest.run()
