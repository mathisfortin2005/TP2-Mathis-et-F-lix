"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-05-10 10:58:39
Version 1
"""
# TODO: Tests unitaires pour chaque méthode
# TODO: Gestion de cache (abandon)
# TODO: Sauvegarde mot de passe par hachage (les mots de passe ne doivent pas être sauvegardés en clair)

# Importation des modules nécessaires au serveur
import json
import unittest
from http.server import HTTPServer, BaseHTTPRequestHandler


# Création de la classe SuperChalet() qui sert à mettre toutes les classes dans une même classe
class SuperChalet:
    Reservations.liste_reservations()
    Chalets.liste_chalets()
    Utilisateurs.liste_utilisateurs()
# FIXME: Ma référence ne semble pas bonne ici


# Création de la classe Réservation qui sert à créer des objets réservations
class Reservations:

    # Constructeur de la classe Reservations
    def __init__(self, id, chalet, utilisateur):
        if self.__reservations is None:
            self.__reservation = []
        self.__id = id
        self.__chalet = chalet
        self.__utilisateur = utilisateur
        self.__reservations = self.__reservations.append([self.__id, self.__chalet, self.__utilisateur])

    # Méthodes GET
    @property
    def id(self):
        return self.__id

    @property
    def chalet(self):
        return self.__chalet

    @property
    def utilisateur(self):
        return self.__utilisateur

    # Méthode pour obtenir les informations d'une réservation
    def obtenir_infosreservation(self, id):
        for x in range(len(self.__reservations)):  # La variable x sert d'itérateur
            infosreservation = self.__reservations[x]
            if infosreservation.index(id) != -1:
                print("La réservation est :" + infosreservation)
            elif inforeservation.index(id) == -1:
                print("Il n'y a pas de réservations")
            else:
                print("Les réservations sont" + inforeservation)
#

    # Méthode pour obtenir les informations sur toutes les réservations d'un utilisateur
    def obtenir_reservations(self, utilisateur):
        for x in range(len(self.__reservations)):  # La variable x sert d'itérateur
            infosreservation = self.__reservations[x]
            if infosreservation.index(utilisateur) != -1:
                print(infosreservation)

    # Méthode pour ajouter une réservation
    def ajout_reservation(self, id, chalet, utilisateur):
        if id not in self.__id.keys():
            raise ValueError('Cette réservation existe déjà')
        else:
            self.__reservations = self.__reservations.append([id, chalet, utilisateur])
# FIXME: Je ne sais pas si nous devons vérifier les disponibilités pour ajouter une réservation (ajouter plage horaire)

    # Méthode pour remplacer une réservation
    def remplacer_reservation(self, id_reservation_a_remplacer):
        for x in range(len(self.__reservations)):
            infosreservation = self.__reservations[x]
            if infosreservation.index(id) != id_reservation_a_remplacer:
                del(self.__reservations[x])
                infosreservation.append(id_reservation_a_remplacer)

    # Méthode pour supprimer une réservation
    def supprimer_reservation(self, id):
        for x in range(len(self.__reservations)):
            infosreservation = self.__reservations[x]
            if infosreservation.index(id) != -1:
                del(self.__reservations[x])

    # Méthode pour retourner la liste des réservations
    def liste_reservation(self):
        return self.__reservations


# Créations de la classe Chalets qui sert à créer des objets Chalet
class Chalets:

    # Constructeur de la classe Chalets
    def __init__(self, id, nom, url_image, geolocalisation):
        if self.__chalets is None:
            self.__chalets = []
        self.__id = id
        self.__nom = nom
        self.__url_image = url_image
        self.__geolocalisation = geolocalisation
        self.__chalets = self.__chalets.append([self.__id, self.__nom, self.__url_image, self.__geolocalisation])

    # Méthode GET
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

    # Méthode pour ajouter une objet Chalet
    def ajout_chalet(self, id, nom, url_image, geolocalisation):
        if id in self.__id and nom in self.__nom and geolocalisation in self.__geolocalisation:
            raise ValueError('Ce chalet existe déjà')
        else:
            self.__chalets = self.__chalets.append([id, nom, url_image, geolocalisation])
# FIXME: Je ne sais pas comment ajouter l'objet Géolocalisation dans la liste de la classe Chalet (Je comprends pas normalement de la façon que tu l'As fait c'est sensé fonctionner?)


# Création de la classe Geolocalisation_Chalet qui sert à créer des objets de position (latitude, longitude)
class GeolocalisationChalet:

    # Constructeur de la classe Geolocalisation_Chalet
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    # Méthodes GET
    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude


# Création de la classe Utilisateurs qui sert à créer des objets Utilisateur
class Utilisateurs:

    # Constructeur de la classe Utilisateurs
    def __init__(self, email, mot_de_passe, nom, prenom, adresse):
        if self.__utilisateurs is None:
            self.__utilisateurs = []
        self.__email = email
        self.__mot_de_passe = mot_de_passe
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        self.__utilisateurs = self.__utilisateurs.append([email, mot_de_passe, nom, prenom, [no_civique, rue, ville, province, pays, code_postal]])
        adresse = Adresses(no_civique, rue, ville, province, pays, code_postal)
# FIXME : Je ne sais pas comment ajouter l'objet Adresse dans le liste de la classe objet Adresse

    # Méthodes GET
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

    # Méthode pour ajouter un objet Utilisateur
    def ajout_utilisateur(self, email, mot_de_passe, nom, prenom, no_civique, rue, ville, province, pays, code_postal):
        if email in self.__email and nom in self.__nom and prenom in self.__prenom:
            raise ValueError('Cet utilisateur existe déjà')
        else:
            self.__utilisateurs = self.__utilisateurs.append([email, mot_de_passe, nom, prenom, [no_civique, rue, ville, province, pays, code_postal]])
            adresse = Adresses(no_civique, rue, ville, province, pays, code_postal)
# FIXME: Je ne sais pas comment ajouter l'objet Adresse dans le liste de la classe objet Adresse

    # Méthode pour obtenir les informations d'un utilisateur
    def obtenir_infosutilisateur(self, email):
        if email not in self.__utilisateurs:
            raise ValueError("Aucun utilisateur n'a le courriel suivant:" + email)
        else:
            for x in range(len(self.__utilisateurs)):  # La variable x sert d'itérateur
                infosutilisateur = self.__utilisateurs[x]
                if infosutilisateur.index(email) != -1:
                    print(infosutilisateur)


# Création de la classe Adresses qui sert à créer des objets Adresse
class Adresses:

    #Constructeur de la classe Adresses
    def __init__(self, no_civique, rue, ville, province, pays, code_postal):
        self.__no_civique = no_civique
        self.__rue = rue
        self.__ville = ville
        self.__province = province
        self.__pays = pays
        self.__code_postal = code_postal
        self.__adresse = [self.__no_civique, self.__rue, self.__ville, self.__province, self.__pays, self.__code_postal]

    #Méthodes GET
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


class TPBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    #Variable de classe
    super_chalet = SuperChalet()
#TODO: Il faudrait faire des if path.startswith('/enclos/') avec les différents trucs. Même chose pour le do_POST. Il faudrait faire un do_DELETE et un do_PUT aussi (pas eu le temps de travailler sur ça)

    # Point d'entrée pour toutes les requêtes de type GET
    def do_GET(self):
        # self.headers contient tous les entêtes de la requête
        headers = self.headers
        # contient le chemin d'accès de la ressource demandé ex: /enclos/...
        path = self.path
        # Gère les chemin d'accès (path) de type GET /enclos/{nom de l'enclos}
        if path.startswith('/reservation/'):
            # permet d'aller chercher le {nom de l'enclos}
            enclos = path.split('/')[2]
            # appelle l'objet zoo pour aller chercher le contenu de l'enclos
            content = 'Enclos: ' + enclos + ' -> ' + str(self.zoo.enclos[enclos])
            # Renvoyer le code 200 pour dire au client que c'est un succès
            self.send_response(200)
            # Si on avait des entêtes à renvoyer au client, on les ajouterait avant la prochaine ligne
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        if path.startswith('/enclos/'):
            # permet d'aller chercher le {nom de l'enclos}
            enclos = path.split('/')[2]
            # appelle l'objet zoo pour aller chercher le contenu de l'enclos
            content = 'Enclos: ' + enclos + ' -> ' + str(self.zoo.enclos[enclos])
            # Renvoyer le code 200 pour dire au client que c'est un succès
            self.send_response(200)
            # Si on avait des entêtes à renvoyer au client, on les ajouterait avant la prochaine ligne
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        if path.startswith('/enclos/'):
            # permet d'aller chercher le {nom de l'enclos}
            enclos = path.split('/')[2]
            # appelle l'objet zoo pour aller chercher le contenu de l'enclos
            content = 'Enclos: ' + enclos + ' -> ' + str(self.zoo.enclos[enclos])
            # Renvoyer le code 200 pour dire au client que c'est un succès
            self.send_response(200)
            # Si on avait des entêtes à renvoyer au client, on les ajouterait avant la prochaine ligne
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        if path.startswith('/enclos/'):
            # permet d'aller chercher le {nom de l'enclos}
            enclos = path.split('/')[2]
            # appelle l'objet zoo pour aller chercher le contenu de l'enclos
            content = 'Enclos: ' + enclos + ' -> ' + str(self.zoo.enclos[enclos])
            # Renvoyer le code 200 pour dire au client que c'est un succès
            self.send_response(200)
            # Si on avait des entêtes à renvoyer au client, on les ajouterait avant la prochaine ligne
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        else:
            # Gère le cas ou le chemin d'accès n'est pas trouvé
            # On pourrait aussi gérer les erreurs
            self.send_response(500, 'enclos non trouve')
            self.end_headers()

    # Permet de gérer l'ajout d'enclos ou l'ajout d'animaux dans un enclos
    def do_POST(self):
        # Chemin d'accès retourné par la requête
        path = self.path
        # Cas d'ajout un enclos POST /enclos
        if path == '/enclos':
            # L'entête content-length contient la longueur du contenu du corps de la requête POST
            content_length = int(self.headers['Content-Length'])
            # lecture entiere du corps du POST
            body = self.rfile.read(content_length)
            # Lecture du body json vers un dictionnaire Python
            json_str = json.loads(body)
            try:
                # Appel de la méthode de zoo pour ajouter un enclos
                self.zoo.ajout_enclos(json_str['nom'])
                self.send_response(200)
            except ValueError:
                # La méthode de zoo a fait un raise d'une exception
                self.send_response(500, 'Enclos existant')
            self.end_headers()
        # Cas ajout d'animal dans un enclos POST /enclos/{nom enclos}
        elif path.startswith('/enclos/'):
            # Aller chercher le nom de l'enclos
            enclos = path.split('/')[2]
            # Entête indiquant le nombre d'octets (bytes) à lire
            content_length = int(self.headers['Content-Length'])
            # lecture entiere du corps du POST
            body = self.rfile.read(content_length)
            # Lecture du body json vers un dictionnaire Python
            json_str = json.loads(body)
            # Appel de la méthode de zoo pour ajouter un animal
            self.zoo.ajout_animal(enclos, json_str['nom'])
            # HTTP status 200 OK
            self.send_response(200)
            self.end_headers()


class ServeurTest:

    @staticmethod
    def run(serveur_class=HTTPServer, serveur_port=8000, handler_class=TPBaseHTTPRequestHandler):
        serveur_adresse = ('', serveur_port)
        httpd = serveur_class(serveur_adresse, handler_class)
        httpd.serve_forever()


serveur = ServeurTest.run()
