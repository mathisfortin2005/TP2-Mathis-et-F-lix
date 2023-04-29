"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-04-28 à 22h00
Version 1
"""
#TODO: Tests unaires pour chaque méthode
#TODO: Gestion de cache
#TODO: @Mathis: Ajouter des commentaires

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SuperChalet():
    Reservations.liste_reservation()
    Chalets.liste_chalets()
    Utilisateurs.liste_utilisateurs()


class Reservations:

    def __init__(self, id, chalet, utilisateur):
        if self.__reservations == None:
            self.__reservation = []
        self.__id = id
        self.__chalet = chalet
        self.__utilisateur = utilisateur
        self.__reservations = self.__reservations.append([self.__id, self.__chalet, self.__utilisateur])

    @property
    def id(self):
        return self.__id

    @property
    def chalet(self):
        return self.__chalet

    @property
    def utilisateur(self):
        return self.__utilisateur

    def obtenir_infosreservation(self, id):
        for x in range(len(self.__reservations)):
            infosreservation = self.__reservations[x]
            if y.index(id) != -1:
                print(infosreservation)
#TODO: Ajouter cas si plusieurs et si aucune réservation

    def obtenir_reservations(self, utilisateur):
        for x in range(len(self.__reservations)):
            infosreservation = self.__reservations[x]
            if y.index(utilisateur) != -1:
                print(infosreservation)

    def ajout_reservation(self, id, chalet, utilisateur):
        if id not in self.__id :
            raise ValueError('Cette réservation existe déjà')
        else:
            self.__reservations = self.__reservations.append([id, chalet, utilisateur])
#FIXME: Je ne sais pas comment ajouter l'objet Chalet et l'objet Utilisateur dans le liste de la classe objet Réservation
#FIXME: Je ne sais pas si nous devons vérifier les disponibilités pour ajouter une réservation

    def remplacer_reservation(self, id_reservation_a_remplacer):
        pass
#TODO: @Mathis: Méthode pour remplacer une réservation


    def supprimer_reservation(self, id):
        for x in range(len(self.__reservations)):
            infosreservation = self.__reservations[x]
            if infosreservation.index(id) != -1:
                del(self.__reservations[x])

    def liste_reservation(self):
        return(self.__reservations)

class Chalets:

    def __init__(self, id, nom, url_image, geolocalisation):
        if self.__chalets == None:
            self.__chalets = []
        self.__id = id
        self.__nom = nom
        self.__url_image = url_image
        self.__geolocalisation = geolocalisation
        self.__chalets = self.__chalets.append([self.__id, self.__nom, self.__url_image, self.__geolocalisation])

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

    def ajout_chalet(self, id, nom, url_image, geolocalisation):
            if id in self.__id and if nom in self.__nom and if geolocalisation in self.__geolocalisation :
                raise ValueError('Ce chalet existe déjà')
            else:
                self.__chalets = self.__chalets.append([id, nom, url_image, geolocalisation])
#FIXME: Je ne sais pas comment ajouter l'objet Géolocalisation dans la liste de la classe Chalet

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
        if self.__utilisateurs == None:
            self.__utilisateurs = []
        self.__email = email
        self.__mot_de_passe = mot_de_passe
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        self.__utilisateurs = self.__utilisateurs.append([email, mot_de_passe, nom, prenom, [no_civique, rue, ville, province, pays, code_postal]])
        adresse = Adresses(no_civique, rue, ville, province, pays, code_postal)
#FIXME : Je ne sais pas comment ajouter l'objet Adresse dans le liste de la classe objet Adresse

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

    def ajout_utilisateur(self, email, mot_de_passe, nom, prenom, no_civique, rue, ville, province, pays, code_postal):
        if email in self.__email and if nom in self.__nom and if prenom in self.__prenom:
            raise ValueError('Cet utilisateur existe déjà')
        else:
            self.__utilisateurs = self.__utilisateurs.append([email, mot_de_passe, nom, prenom, [no_civique, rue, ville, province, pays, code_postal]])
            adresse = Adresses(no_civique, rue, ville, province, pays, code_postal)
#FIXME: Je ne sais pas comment ajouter l'objet Adresse dans le liste de la classe objet Adresse

    def obtenir_infosutilisateur(self, email):
        if email not in self.__utilisateurs:
            raise ValueError("Aucun utilisateur n'a le courriel suivant:" + email)
        else:
            for x in range(len(self.__utilisateurs)):
                infosutilisateur = self.__reservations[x]
                if infosutilisateur.index(email) != -1:
                    print(infosreservation)


class Adresses:

    def __init__(self, no_civique, rue, ville, province, pays, code_postal):
        self.__no_civique = no_civique
        self.__rue = rue
        self.__ville = ville
        self.__province = province
        self.__pays = pays
        self.__code_postal = code_postal
        self.__adresse = [self.__no_civique, self.__rue, self.__ville, self.__province, self.__pays, self.__code_postal]

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

#TODO: Toute cette partie est à regarder, je ne la comprends pas.
class TPBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    # variable de classe
SuperChalet = SuperChalet()
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
"""