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