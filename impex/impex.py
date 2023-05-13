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
fichier_utilisateurs = open('data/utilisateurs.csv', 'rt')
fichier_utilisateurs.read()

# Lecture du fichier CSV contenant les chalets (point 3 consignes impex)
fichier_chalets = open('data/chalets.csv', 'rt')
fichier_chalets.read()

# Lecture du fichier XML contenant les disponibilités des chalets (point 4 consignes impex)
fichier_dispo_chalets = open('data/disponibilites.xml', 'rt')
fichier_dispo_chalets.read()

# Lecture du fichier XML contenant les réservations (point 5 consignes impex)
fichier_reservations = open('data/reservations.xml', 'rt')
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
        with open('./data/utilisateurs.csv', 'w', newline='') as csv_file:
            with open (nom_fichier, 'w'):
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(
                    ['Email', 'Mot de passe', 'Nom', 'Prénom', 'No. civique', 'Rue', 'Ville', 'Province', 'Pays','Code postal'])
                # Boucle for pour passer tout les utilisateurs
                for utilisateur in utilisateurs_json:
                    email, mot_de_passe, nom, prenom, adresse = utilisateur
                    no_civique, rue, ville, province, pays, code_postal = adresse
                    csv_writer.writerow(
                    [email, mot_de_passe, nom, prenom, no_civique, rue, ville, province, pays, code_postal])

    @staticmethod
    # Méthode statique pour exporter les données d'un objet JSON "reservation" dans un fichier "export_{timestamp}.xml" dans le format XML
    def exportJson(reservations_csv):
        # Pour créer le fichier
        timestamp = datetime.now()
        nom_fichier = f'export_{timestamp}.json'
        # Pour ouvrir le fichier en mode écriture
        with open(nom_fichier, 'w') as fichier_json:
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
