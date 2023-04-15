#Importation de impex
from impex import impex

#Définition de la classe Reservation
class Reservation():

    #Constructeur de la classe Reservation
    def __init__(self):
        Reservation.__id = ''
        Reservation.__chalet = ''

    #Méthode qui retourne l'information sur la réservation
    def do_GET_reservation(self):
        with open('', 'rt'):
            return()

    #Méthode qui retourne toutes les réservations de l'utilisateur
    def do_GET_reservations(self):
        pass

    #Méthode qui ajoute une réservation
    def do_POST_reservation(self):
        with open('reservationId', 'w'):
            pass

    #Méthode qui remplace une réservation
    def do_PUT_reservation(self):
        pass


    #Méthode qui supprime une réservation
    def do_DELETE_reservation(self):
        pass


    #Méthode qui renvoie toutes les réservations triées par ordre de reservationld (pour les administrateurs)
    def do_GET_reservations(self):
        pass


#Définition de la classe Utilisateur
class Utilisateur():

    #Constructeur de la classe Utilisateur
    def __init__(self):


    #Méthode qui ajoute un utilisateur:
    def do_POST_utilisateur(self):
        pass



#Code pour les tests

