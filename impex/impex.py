"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-04-30 20:07:04
Version 1
"""
#FIXME: Pourquoi importer .client.client.py
from client import client
import datetime
#import pickle
import csv
import json

#Lecture du fichier CSV contenant les utilisateurs, leur type d'utilisateur et leur mot de passe
with open('data/utilisateurs.csv', 'rt') as fichier_utilisateurs:
    fichier_utilisateurs.read()

#Lecture du fichier CSV contenant les chalets
with open('data/chalets.csv', 'rt') as fichier_chalets:
    fichier_chalets.read()

#Lecture du fichier XML contenant les disponibilités des chalets
with open('data/disponibilites.xml', 'rt') as fichier_dispo_chalets:
    fichier_dispo_chalets.read()

#Lecture du fichier XML contenant les réservations
with open('data/reservations.xml', 'rt') as fichier_reservations:
    fichier_reservations.read()

#Méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.csv" dans le format CSV
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

#utilisateurs = [['m@g.com', 'z', 'MF', 'CK', [26, 'rue des Cavaliers', 'St-Simon', 'QC', 'Canada', 'G3V 2V4']],['email', 'mot_de_passe', 'nom', 'prenom', ['no_civique', 'rue', 'ville', 'province', 'pays', 'code_postal']]]

#Pour créer un nom de fichier en fonction du temps
timestamp = datetime.time().strftime("%Y-%m-%d_%H-%M-%S")
nom_fichier = f'export_{timestamp}.csv'
#Pour ouvrir le fichier en mode écriture
with open('..data/reservations.xml', 'w', newline='') as fichier_csv:
#FIXME: C'est quoi le lien vers le fichier reservations.xml?
    #Pour créer un objet pour écrire dans un fichier csv
    csv_writer = csv.writer(fichier_csv, delimiter=',')
    #Pour écrire les en-têtes de colonne
    csv_writer.writerow = ([''])
    for x in len(utilisateurs):
#FIXME: Comment récupérer les utilisateurs du fichier reservations.xml?
        #Pour écrire les données des réservations
        csv_writer.writerow = (utilisateur[x])


#Méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.json" dans le format JSON
#@staticmethod
def export_json(reservations_csv):
    #Pour sérialiser reservations_csv en une string formatée en JSON
    reservation = json.dumps(reservations_csv)
    #Pour créer un nom de fichier en fonction du temps
    timestamp = datetime.time().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f'export_{timestamp}.json'
    #Pour ouvrir le fichier en mode écriture
    with open(nom_fichier, 'w', newline=' ') as fichier_csv:
        #Pour créer un objet pour écrire dans un fichier csv
        json_writer = json.writer(fichier_csv, delimiter=',')
        #Pour écrire les en-têtes de colonne
        json_writer.writerow = ([''])
        #Pour écrire les données des réservations
        json_writer.writerow = ([reservation[''], reservation['']])
# TODO: Compléter lignes 60 et 62
# FIXME: Il ne faudrait pas mettre les 2 dernières méthodes dans une classe?

#Pour que le code se réalise
export_json(fichier_utilisateurs)
export_csv(fichier_reservations)
