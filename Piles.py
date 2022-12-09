class Pile :
    #une pile sous forme de liste chaînée
    def __init__(self,TailleMaxPile):
        self.data = []
        self.TailleMaxPile = TailleMaxPile
        
    def est_vide(self):
        return len(self.data) == 0 
    
    def empile(self,x):
        if(self.est_pleine()):
            raise IndexError("La liste est pleine")
        else:
            self.data.append(x)
    
    def depile(self):
        if self.est_vide() == True :
            raise IndexError("Vous avez essayé de dépiler une pile vide !")
        else :
            return self.data.pop()
    
    def sommet(self):
        return self.data[-1]
    
    def longueur(self):
        return len(self.data)
    
    def __repr__(self):
        affichage = "|"             
        for element in self.data :
            affichage = f"|{element}{affichage}"
        return affichage
    
    def est_pleine(self):
        if(self.longueur() == self.TailleMaxPile):
            return True
        return False
    
if __name__ =='__main__':
    MaPile = Pile(5)
    print(MaPile.est_vide())
    print(MaPile)
    MaPile.empile(5)
    MaPile.empile(4)
    MaPile.empile(3)
    MaPile.empile(2)
    MaPile.empile(1)
    print(p)
    print(p.depile())
    print(p.depile())
    print("Sommet =",p.sommet())
    print(p)
    p.empile(55)
    print(p.est_pleine())
    print(p)
    p.empile(158)
    print(p.est_pleine())
    print(p)