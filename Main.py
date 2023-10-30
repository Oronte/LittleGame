from Player import*
from Weapon import*
from Shield import*

p1 = Personnage("Oronte", 50)
s1 = Armure()
w1 = Armes()
p1.setPosition(1, 1)
p1.setArme(w1.getDegats('Epee'))
p1.setShield(s1.getArmure('PetitBouclier'))


p2 = Personnage("Soler", 50)
p2.setPosition(1, 1)
s2 = Armure()
w2 = Armes()
p2.setArme(w1.getDegats('MmeCorneille'))
p2.setShield(s1.getArmure('LeBouclierSamere'))

w1.attaque(p2,p1,'MmeCorneille')

p1.Soins()

p2.deplacement(-1,1)

p1.setArme(w1.getDegats('EpeeDeOrtonce'))

w1.attaque(p1,p2,'EpeeDeOrtonce')