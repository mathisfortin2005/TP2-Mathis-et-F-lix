"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-05-10 10:58:39
Version 1
"""
#FIXME: Pourquoi importer .client.client.py et pickle
from client import client # Importation module client (point 1 consignes impex)
import datetime
#import pickle
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

'''
@staticmethod
def export_csv(utilisateurs_json):
    #Pour déserialiser utilisateurs_json en un objet Python contenant un document JSON
    utilisateur = csv.dumps(utilisateurs_json)
    #Pour créer un nom de fichier en fonction du temps
    timestamp = datetime.time().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f'export_{timestamp}.csv'
    #Pour ouvrir le fichier en mode écriture
    with open(nom_fichier, 'w', newline=' ') as fichier_csv:
        #Pour créer un objet pour écrire dans un fichier csv
        csv_writer = csv.writer(fichier_csv, delimiter=',')
        #Pour écrire les en-têtes de colonne
        csv_writer.writerow = ([''])
        #Pour écrire les données des réservations
        csv_writer.writerow = ([utilisateur[''], utilisateur['']])
#TODO: Compléter lignes 43 et 45
'''

class impex:
    # utilisateurs = [['m@g.com', 'z', 'MF', 'CK', [26, 'rue des Cavaliers', 'St-Simon', 'QC', 'Canada', 'G3V 2V4']],['email', 'mot_de_passe', 'nom', 'prenom', ['no_civique', 'rue', 'ville', 'province', 'pays', 'code_postal']]]
    # Méthode pour exporter les données d'un objet JSON "utilisateur" dans un fichier "export_{timestamp}.csv" dans le format CSV (point 7 consignes impex)
    @staticmethod
    def export_csv(utilisateurs_json):
        # Pour créer un nom de fichier en fonction du temps
        timestamp = datetime.time().strftime("%Y-%m-%d_%H-%M-%S")
        nom_fichier = f'export_{timestamp}.csv'
        # Pour ouvrir le fichier en mode écriture
        with open('./data/reservations.xml', 'w', newline='') as fichier_csv:
            # Pour créer un objet pour écrire dans un fichier csv
            csv_writer = csv.writer(fichier_csv, delimiter=',')
            # Pour écrire les en-têtes de colonne
            csv_writer.writerow = ([''])
            for x in len(fichier_utilisateurs):
                fichier_utilisateurs[x].open(fichier_csv)
                #Pour écrire les données des réservations
                csv_writer.writerow = (fichier_utilisateurs[x])


    # Méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.json" dans le format JSON (point 8 consignes impex)
    @staticmethod
    def export_json(reservations_csv):
        # Pour sérialiser reservations_csv en une string formatée en JSON
        reservation = json.dumps(reservations_csv)
        # Pour créer un nom de fichier en fonction du temps
        timestamp = datetime.time().strftime("%Y-%m-%d_%H-%M-%S")
        nom_fichier = f'export_{timestamp}.json'
        # Pour ouvrir le fichier en mode écriture
        with open(nom_fichier, 'w', newline=' ') as fichier_csv:
            # Pour créer un objet pour écrire dans un fichier csv
            json_writer = json.writer(fichier_csv, delimiter=',')
            # Pour écrire les en-têtes de colonne
            json_writer.writerow = ([''])
            # Pour écrire les données des réservations
            json_writer.writerow = ([reservation[''], reservation['']])
# FIXME: Il ne faudrait pas mettre les 2 dernières méthodes dans une classe? (jcrois pas) (Oui car méthode statique)

# Pour que le code se réalise
impex.export_json(fichier_utilisateurs)
impex.export_json(fichier_reservations)
