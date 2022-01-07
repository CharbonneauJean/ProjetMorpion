class Morpion:

    currentPlayer = 1
    grid = []

    def __init__(self):
        joueur = 1
        self.grid=[" "," "," "," "," "," "," "," "," "]

    def showGrid(self):
        print("     0   1   2 ")
        print("   -------------")
        print("0 ", end='')
        for i in range(3):
            print(" | "+str(self.grid[i]), end='')
        print(" |")
        print("   -------------")
        print("1 ", end='')
        for i in range(3):
            print(" | "+str(self.grid[i+3]), end='')
        print(" |")
        print("   -------------")
        print("2 ", end='')
        for i in range(3):
            print(" | "+str(self.grid[i+6]), end='')
        print(" |")
        print("   -------------")


    def newTurn(self):
        print("Tour du joueur "+str(self.currentPlayer))
        column=input("Colonne : ")
        line=input("Ligne : ")
        print("Vous avez coché la case ("+column+","+line+")")
        while self.grid[int(column)+int(line)*3]!=" ":
            self.showGrid()
            print("Cette case est deja cochée ! Veuillez en choisir une autre.")
            column=input("Colonne : ")
            line=input("Ligne : ")
            print("Vous avez coché la case ("+column+","+line+")")

        if self.currentPlayer==1 :
            self.grid[int(column)+int(line)*3]="X"
        if self.currentPlayer==2 :
            self.grid[int(column)+int(line)*3]="O"
        self.showGrid()

    def hasWinner(self):
        if (self.grid[0]==self.grid[1]) and (self.grid[0]==self.grid[2]) and (self.grid[0]!=" "):
            return 1
        if (self.grid[3]==self.grid[4]) and (self.grid[3]==self.grid[5]) and (self.grid[3]!=" "):
            return 1
        if (self.grid[6]==self.grid[7]) and (self.grid[6]==self.grid[8]) and (self.grid[6]!=" "):
            return 1
        if (self.grid[0]==self.grid[3]) and (self.grid[0]==self.grid[6]) and (self.grid[0]!=" "):
            return 1
        if (self.grid[1]==self.grid[4]) and (self.grid[1]==self.grid[7]) and (self.grid[1]!=" "):
            return 1
        if (self.grid[2]==self.grid[5]) and (self.grid[2]==self.grid[8]) and (self.grid[2]!=" "):
            return 1
        if (self.grid[0]==self.grid[4]) and (self.grid[0]==self.grid[8]) and (self.grid[0]!=" "):
            return 1
        if (self.grid[2]==self.grid[4]) and (self.grid[2]==self.grid[6]) and (self.grid[2]!=" "):
            return 1


    def isDraw(self):
        for i in range(9):
            if self.grid[i]==" ":
                return 0
        return 1


jeuMorpion = Morpion()

jeuMorpion.currentPlayer=1
print("Le joueur 1 joue avec les X et le joueur 2 avec les O")

jeuMorpion.showGrid()
gagne=0
while gagne==0:
    jeuMorpion.newTurn()
    if jeuMorpion.hasWinner():
        print("Le joueur "+str(jeuMorpion.currentPlayer)+" a gagné !")
        gagne=1
    else:
        if jeuMorpion.isDraw():
            print("Match nul !")
            gagne=1
    if jeuMorpion.currentPlayer==1:
        jeuMorpion.currentPlayer=2
    else:
        jeuMorpion.currentPlayer=1