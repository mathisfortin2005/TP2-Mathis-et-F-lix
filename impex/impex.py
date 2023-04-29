"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-04-22
Version 1
"""
#FIXME: Le prof a dit d'importer client.client.py mais comment?
import client.py

#Lecture du fichier CSV contenant les utilisateurs, leur type d'utilisateur et leur mot de passe
with open('data/utilisateurs.csv', 'rt') as fichier_utilisateur:
    fichier_utilisateur.read()

#Lecture du fichier CSV contenant les chalets
with open('data/chalets.csv', 'rt') as fichier_chalets:
    fichier_chalets.read()

#Lecture du fichier XML contenant les disponibilités des chalets
with open('data/disponibilites.xml', 'rt') as fichier_dispo_chalets:
    fichier_dispo_chalets.read()

#Lecture du fichier XML contenant les réservations
with open('data/reservations.xml', 'rt') as fichier_reservations:
    fichier_reservations.read()

#TODO: Méthodes pour exporter les données
#Méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.csv" dans le format CSV

#Méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.json" dans le format JSON