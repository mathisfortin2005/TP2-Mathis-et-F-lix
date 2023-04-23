#Lecture du fichier CSV contenant les utilisateurs, leur type d'utilisateur et leur mot de passe
with open('data/Utilisateur.CSV', 'rt') as fichier_utilisateur:
    fichier_utilisateur.read()

#Lecture du fichier CSV contenant les chalets
with open('data/Chalet.CSV', 'rt') as fichier_chalets:
    fichier_chalets.read()

#Lecture du fichier XML contenant les disponibilités des chalets
with open('data/Disponibilités chalet.XML', 'rt') as fichier_dispo_chalets:
    fichier_dispo_chalets.read()

#Lecture du fichier XML contenant les réservations
with open('data/Réservations.XML', 'rt') as fichier_reservations:
    fichier_reservations.read()

#Méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.csv" dans le format CSV

#Méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.json" dans le format JSON