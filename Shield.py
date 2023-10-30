from Player import*

class Armure:
    def __init__(self):
        self.armures = {'PetitBouclier': 2, 'LeBouclierSamere': 6}

    def getArmure(self, nomArmure):
        if nomArmure in self.armures:
            return self.armures[nomArmure]
        else:
            return 0

    def defense(self, personnage, nomArmure, degats):
        if nomArmure in self.armures:
            personnage.PerteVie(Degat)