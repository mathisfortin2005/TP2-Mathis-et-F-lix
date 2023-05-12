"""
TP2
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-05-11 20:30:22
Version 1
"""

# Création d'une cache pour le serveur
class CacheServer:

    def __init__(self):
        self.__taillemaxentree = None
        self.__agemax = None
        self.__taillemaxespace = None
        self.__cache = {}

    def GET_objet(self, key):
        if key not in self.cache:
            value = None
        else:
            value = self.cache[key]
        return(value)

    def DEL_objet(self, key):
        del key

    def PUT_objet(self, key, obj):
        self.__cache[key] = obj

    def POST_objet(self, key, obj):
        self.__cache[key] = obj