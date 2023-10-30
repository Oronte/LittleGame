from Shield import*
from Weapon import*
from math import sqrt

class Personnage:
    def __init__(self, nom, point_de_vie):
        self.__n = nom
        self.__pv = point_de_vie
        self.__position = (0,0)
        self.__arme = None
        self.__armure = None
        self.__alive = True

    def __repr__(self):
        return "Je suis "+str(self.__n)+", j'ai "+str(self.__pv)+" pts de vie, "+str(self.getPointsAttaque())+" de dégâts, et "+str(self.__armure)+" d'armure"

    def Soins(self):
        self.__pv+=2
        print(str(self.__n)+" a maintenant "+str(self.__pv)+" de vie")

    def PerteVie(self,Degat):
        if self.__armure==0:
            self.__pv-=Degat
        elif self.__armure>=Degat:
            self.__armure-=Degat
        else:
            self.__pv-=Degat-self.__armure
            self.__armure=0
        if self.__pv<=0:
            self.__alive=False
            print( str(self.__n)+" a perdu la partie")
        print("il lui reste "+str(self.__armure)+" d'armure et "+str(self.__pv)+" de vie")


    def distance(self, other_personnage):
        x1, y1 = self.__position
        x2, y2 = other_personnage.__position
        dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return dist

    def deplacement(self, x, y):
        assert -2<=x<2 and -2<=y<2,'mettez une valeur plus raisonable'
        self.__position = (self.__position[0]+x,self.__position[1]+y)
        print(str(self.__n)+" est en "+str(self.__position))

    def getPV(self):
        return self.__pv

    def getNom(self):
        return self.__n

    def getPointsAttaque(self):
        return self.__arme

    def getPointsDefense(self):
        return self.__armure

    def getPosition(self):
        return self.__position

    def setNom(self, nom):
        self.__n = nom

    def setPointsVie(self, pointsVie):
        self.__pv = pointsVie

    def setShield(self,a):
        self.__armure = a

    def setArme(self, arme):
        self.__arme = arme

    def setPosition(self,x,y):
        self.__position=(x,y)

    def check_if_alive(self):
        if not self.__alive:
            print(str(self.getNom())+" n'est plus en vie. La partie est terminée.")
            exit()
