from Player import*

class Armes:
    def __init__(self):
        self.armes = {'Gants': [1,1], 'Epee': [3,2], 'MmeCorneille': [7,10], 'Arc':[4,10], 'EpeeDeOrtonce': [60,3]}

    def getDegats(self, nomArme):
        if nomArme in self.armes:
            return self.armes[nomArme][0]
        else:
            return 0

    def attaque(self, agresseur, cible, nomArme):
        if agresseur.distance(cible) <= self.armes[nomArme][1]:
            cible.PerteVie(self.armes[nomArme][0])
            print(str(agresseur.getNom())+" a attaqué "+str(cible.getNom())+" avec "+str(nomArme)+" pour "+str(self.armes[nomArme][0])+" degats.")
        else:
            print("il n'y a pas la portée necessaire")