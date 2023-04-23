"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-04-22
Version 1
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class Reservations:

    def __init__(self, id, chalet, utilisateur):
        self.__id = id
        self.__chalet = chalet
        self.__utilisateur = utilisateur

    @property
    def id(self):
        return self.__id

    @property
    def chalet(self):
        return self.__chalet

    @property
    def utilisateur(self):
        return self.__utilisateur

    def obtenir_infosreservation(self):
        pass

    def obtenir_reservations(self, utilisateur):
        pass

    #Pour administrateur seulement
    def ajout_reservation(self):
        pass

    def remplacer_reservation(self):
        pass

    def supprimer_reservation(self):
        pass

    def liste_reservation(self):
        pass

class Chalets:

    def __init__(self, id, nom, url_image, geolocalisation):
        self.__id = id
        self.__nom = nom
        self.__url_image = url_image
        self.__geolocalisation = geolocalisation

    @property
    def id(self):
        return self.__id

    @property
    def nom(self):
        return self.__nom

    @property
    def url_image(self):
        return self.__url_image

    @property
    def geolocalisation(self):
        return self.__geolocalisation

    def ajout_utilisateur(self):
        pass

class Geolocalisation_Chalet:

    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

class Utilisateurs:

    def __init__(self, email, mot_de_passe, nom, prenom, adresse):
        self.__email = email
        self.__mot_de_passe = mot_de_passe
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse

    @property
    def email_utilisateur(self):
        return self.__email

    @property
    def mot_de_passe_utilisateur(self):
        return self.__mot_de_passe

    @property
    def nom_utilisateur(self):
        return self.__nom

    @property
    def prenom_utilisateur(self):
        return self.__prenom

    @property
    def adresse_utilisateur(self):
        return self.__adresse

    def ajout_utilisateur(self):
        pass

    def obtenir_infosutilisateur(self):
        pass

class Adresses:

    def __init__(self, no_civique, rue, ville, province, pays, code_postal):
        self.__no_civique = no_civique
        self.__rue = rue
        self.__ville = ville
        self.__province = province
        self.__pays = pays
        self.__code_postal = code_postal

    @property
    def no_civique(self):
        return self.__no_civique

    @property
    def rue(self):
        return self.__rue

    @property
    def ville(self):
        return self.__ville

    @property
    def province(self):
        return self.__province

    @property
    def pays(self):
        return self.__pays

    @property
    def code_postal(self):
        return self.__code_postal

#MATHIS : Je n'ai rien touché dans cette partie mais c'est certain qu'il faudra la retravailler
class TPBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    # variable de classe
    zoo = Zoo()
#MATHIS: Il faudrait faire des if path.startswith('/enclos/') avec les différents trucs. Même chose pour le do_POST. Il faudrait faire un do_DELETE et un do_PUT aussi
    def do_GET(self):
        headers = self.headers
        path = self.path
        if path.startswith('/enclos/'):
            enclos = path.split('/')[2]
            content = 'Enclos: ' + enclos + ' -> ' + str(self.zoo.enclos[enclos])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        else:
            self.send_response(500, 'enclos non trouve')
            self.end_headers()

    def do_POST(self):
        path = self.path
        if path == '/enclos':
            content_length = int(self.headers['Content-Length'])
            # lecture entiere du corps du POST
            body = self.rfile.read(content_length)
            json_str = json.loads(body)
            try:
                self.zoo.ajout_enclos(json_str['nom'])
                self.send_response(200)
            except ValueError:
                self.send_response(500, 'Enclos existant')
            self.end_headers()
        elif path.startswith('/enclos/'):
            enclos = path.split('/')[2]
            content_length = int(self.headers['Content-Length'])
            # lecture entiere du corps du POST
            body = self.rfile.read(content_length)
            json_str = json.loads(body)
            self.zoo.ajout_animal(enclos, json_str['nom'])
            self.send_response(200)
            self.end_headers()


class ServeurTest:

    @staticmethod
    def run(serveur_class=HTTPServer, serveur_port=8000, handler_class=TPBaseHTTPRequestHandler):
        serveur_adresse = ('', serveur_port)
        httpd = serveur_class(serveur_adresse, handler_class)
        httpd.serve_forever()


serveur = ServeurTest.run()

"""
#Importation des modules nécessaires
from client import client
from http.server import HTTPServer
# Le serveur va ecouter sur localhost:8080
httpd = HTTPServer(('localhost', 8080), client)

#Définition de la classe Chalet
class Chalet():

    #Constructeur de la classe Chalet
    def __init__(self):
        pass

    #Méthode pour ajouter un chalet
    def do_POST_chalet(self):
        pass

    #Méthode pour retourner les informations d'un chalet
    def do_GET_chalet(self):
        pass

# Commence a 'servir' les connections
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass


#Code pour les tests
"""