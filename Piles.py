class Pile :

    def __init__(self,TailleMaxPile):
        self.data = []
        self.TailleMaxPile = TailleMaxPile
        
    def est_vide(self):
        """
        Vérifie si la pile est vide
        
        Args:
        
        returns:
            Un booléen
        
        """
        return len(self.data) == 0 
    
    def empile(self,x):
        """
        Ajout d'element dans la pile
        
        Args x : l'élément à ajouter
        
        Returns:
            
        """
        if(self.est_pleine()):
            raise IndexError("La liste est pleine")
        self.data.append(x)
    
    def depile(self):
        """
        Suppression d'elements dans la pile
                
        Args x : 
        
        Returns: l'élément supprimé
        
        """
        if (self.est_vide() == True) :
            raise IndexError("Vous avez essayé de dépiler une pile vide !")
        return self.data.pop()
    
    def sommet(self):
        """
        Cherche le sommet de la pile
        
        Args :
        
        Returns :
            Le sommet de la pile
        
        """
        return self.data[-1]
    
    def longueur(self):
        """
        Calcul la longueur de la pile
        
        Args :
        
        Returns :
            La taille de la pile
        """
        return len(self.data)
    
    def __repr__(self):
        affichage = ""             
        for element in self.data :
            affichage = f"{affichage}[{element}]"
        return affichage
    
    def est_pleine(self):
        """
        Regarde si la pile est pleine
        
        Args :
        
        Returns:
            Booleen
        """
        if(self.longueur() == self.TailleMaxPile):
            return True
        else:
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
    print(MaPile)
    print(MaPile.depile())
    print(MaPile.depile())
    print("Sommet =",MaPile.sommet())
    print(MaPile)
    MaPile.empile(55)
    print(MaPile.est_pleine())
    print(MaPile)
    MaPile.empile(158)
    print(MaPile.est_pleine())
    print(MaPile)