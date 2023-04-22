import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class Reservation:

    def __init__(self):
        self.__reservation = {}

    @property
    def reservation(self):
        return self.__reservation

    def ajout_chalet(self, nom):
        if nom in self.__chalet.keys():
            raise ValueError('Chalet existant')
        self.__chalet[nom] = []

    def ajout_animal(self, enclos, nom):
        if enclos not in self.__enclos.keys():
            raise ValueError('Enclos inexistant')
        self.__enclos[enclos].append(nom)

class TPBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    # variable de classe
    chalet = Chalet()
    def do_GET_reservationID(self):
        headers = self.headers
        path = self.path
        if path.startswith('/chalet/'):
            enclos = path.split('/')[2]
            content = 'Chalet: ' + chalet + ' -> ' + str(self.zoo.chalet[chalet])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        else:
            self.send_response(500, 'Chalet non trouve')
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