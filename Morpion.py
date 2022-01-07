class Morpion:

    joueur = 1
    grille = []

    def __init__(self):
        joueur = 1
        self.grille=[" "," "," "," "," "," "," "," "," "]

    def showGrid(self):
        print("     0   1   2 ")
        print("   -------------")
        print("0 ", end='')
        for i in range(3):
            print(" | "+str(self.grille[i]), end='')
        print(" |")
        print("   -------------")
        print("1 ", end='')
        for i in range(3):
            print(" | "+str(self.grille[i+3]), end='')
        print(" |")
        print("   -------------")
        print("2 ", end='')
        for i in range(3):
            print(" | "+str(self.grille[i+6]), end='')
        print(" |")
        print("   -------------")


    def newTurn(self):
        print("Tour du joueur "+str(self.joueur))
        colonne=input("Colonne : ")
        ligne=input("Ligne : ")
        print("Vous avez coché la case ("+colonne+","+ligne+")")
        while self.grille[int(colonne)+int(ligne)*3]!=" ":
            self.showGrid()
            print("Cette case est deja cochée ! Veuillez en choisir une autre.")
            colonne=input("Colonne : ")
            ligne=input("Ligne : ")
            print("Vous avez coché la case ("+colonne+","+ligne+")")

        if self.joueur==1 :
            self.grille[int(colonne)+int(ligne)*3]="X"
        if self.joueur==2 :
            self.grille[int(colonne)+int(ligne)*3]="O"
        self.showGrid()

    def hasWinner(self):
        if (self.grille[0]==self.grille[1]) and (self.grille[0]==self.grille[2]) and (self.grille[0]!=" "):
            return 1
        if (self.grille[3]==self.grille[4]) and (self.grille[3]==self.grille[5]) and (self.grille[3]!=" "):
            return 1
        if (self.grille[6]==self.grille[7]) and (self.grille[6]==self.grille[8]) and (self.grille[6]!=" "):
            return 1
        if (self.grille[0]==self.grille[3]) and (self.grille[0]==self.grille[6]) and (self.grille[0]!=" "):
            return 1
        if (self.grille[1]==self.grille[4]) and (self.grille[1]==self.grille[7]) and (self.grille[1]!=" "):
            return 1
        if (self.grille[2]==self.grille[5]) and (self.grille[2]==self.grille[8]) and (self.grille[2]!=" "):
            return 1
        if (self.grille[0]==self.grille[4]) and (self.grille[0]==self.grille[8]) and (self.grille[0]!=" "):
            return 1
        if (self.grille[2]==self.grille[4]) and (self.grille[2]==self.grille[6]) and (self.grille[2]!=" "):
            return 1


    def isDraw(self):
        for i in range(9):
            if self.grille[i]==" ":
                return 0
        return 1


jeuMorpion = Morpion()

jeuMorpion.joueur=1
print("Le joueur 1 joue avec les X et le joueur 2 avec les O")

jeuMorpion.showGrid()
gagne=0
while gagne==0:
    jeuMorpion.newTurn()
    if jeuMorpion.hasWinner():
        print("Le joueur "+str(jeuMorpion.joueur)+" a gagné !")
        gagne=1
    else:
        if jeuMorpion.isDraw():
            print("Match nul !")
            gagne=1
    if jeuMorpion.joueur==1:
        jeuMorpion.joueur=2
    else:
        jeuMorpion.joueur=1