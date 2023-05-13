"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-05-12 21:01:36
Version 1
"""

from client import client  # Importation module client (point 1 consignes impex)
from datetime import datetime
import csv
import json

# Lecture du fichier CSV contenant les utilisateurs, leur type d'utilisateur et leur mot de passe (point 2 consignes impex)
with open('data/utilisateurs.csv', 'rt') as fichier_utilisateurs:
    fichier_utilisateurs.read()

# Lecture du fichier CSV contenant les chalets (point 3 consignes impex)
with open('data/chalets.csv', 'rt') as fichier_chalets:
    fichier_chalets.read()

# Lecture du fichier XML contenant les disponibilités des chalets (point 4 consignes impex)
with open('data/disponibilites.xml', 'rt') as fichier_dispo_chalets:
    fichier_dispo_chalets.read()

# Lecture du fichier XML contenant les réservations (point 5 consignes impex)
with open('data/reservations.xml', 'rt') as fichier_reservations:
    fichier_reservations.read()


# La classe Impex permet de définir les méthodes d'exportation d'un fichier d'un format vers un autre
class Impex:
    @staticmethod
    # Méthode statique pour exporter les données d'un objet JSON "utilisateur" dans un fichier "export_{timestamp}.csv" dans le format CSV
    def exportCsv(utilisateurs_json):
        # Pour créer un nom de fichier en fonction du temps
        timestamp = datetime.now()
        nom_fichier = f'export_{timestamp}.csv'
        # Pour ouvrir le fichier en mode écriture
        with open(nom_fichier, 'w', newline='') as fichier_csv:
            csv_writer = csv.writer(fichier_csv, delimiter=',')
            csv_writer.writerow(
                ['email', 'mot_de_passe', 'nom', 'prenom', 'no_civique', 'rue', 'ville', 'province', 'pays',
                 'code_postal'])
            # Boucle for pour passer tout les utilisateurs
            for utilisateur in utilisateurs_json:
                email, mot_de_passe, nom, prenom, adresse = utilisateur
                no_civique, rue, ville, province, pays, code_postal = adresse
                csv_writer.writerow(
                    [email, mot_de_passe, nom, prenom, no_civique, rue, ville, province, pays, code_postal])

    @staticmethod
    # Méthode statique pour exporter les données d'un objet JSON "reservation" dans un fichier "export_{timestamp}.xml" dans le format XML
    def exportJson(reservations_csv):
        # Pour créer un nom de fichier en fonction du temps
        timestamp = datetime.now()
        nom_fichier = f'export_{timestamp}.json'
        # Pour ouvrir le fichier en mode écriture
        with open(nom_fichier, 'w', newline='') as fichier_json:
            json.dump(reservations_csv, fichier_json)


# Fonction qui permet d'exporter les données en JSON vers le serveur
def executerJson(fichier_reservations):
    Impex.exportJson(fichier_reservations)


# Fonction qui permet d'exporter les données en CSV vers le serveur
def executerCsv(fichier_reservations):
    Impex.exportCsv(fichier_reservations)


# Fonction qui contient le code à appeler pour l'import des données vers le serveur
def executer(fichier_reservations):
    executerCsv(fichier_reservations)
    executerJson(fichier_reservations)


# Pour que le code se réalise
executer(fichier_reservations)
