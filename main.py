from tkinter import *  
from classes import *

class GameInterface:                                                        # Classe GameInterface 
                                                                
    def __init__(self, boardSize):                                          # Constructeur de la classe GameInterface                         
        self.boardSize = boardSize                                          # Taille du plateau               
        self.pion = Pion()                                                   # Pion du jeu
        self.jeu = Jeu(boardSize, self.pion)                                # Jeu                               
        self.nbCoups = 0                                                    # Nombre de coups                               
        self.lastButton1 = None                                             # Dernier bouton du joueur 1    
        self.lastButton2 = None                                             # Dernier bouton du joueur 2

        self.window = Tk()                                                  # Fenêtre du jeu                              
        self.window.title("Jeu de Puissance 5")                             # Titre de la fenêtre                                
        self.window.config(padx=20, pady=20, highlightthickness=0, bd=0, bg="black") # Configuration de la fenêtre

        self.__frame1 = Frame(self.window)                                  # Frame du plateau                            
        self.__frame1.grid(row=0, column=0, rowspan=2)                      # Configuration du frame du plateau                    
        self.__frame1.config(pady=20, bg="black")                           # Configuration du frame du plateau                        

        self.__frame2 = Frame(self.window)                                  # Frame du joueur                 
        self.__frame2.grid(row=boardSize, column=0)                         # Configuration du frame du joueur               
        self.__frame2.config(padx=2, pady=2)                                # Configuration du frame du joueur              

        self.__nbText = StringVar()                                         # Texte du joueur   
        self.__nbText.set("Player " + str(self.pion.getPlayer() + 1))       # Texte du joueur
        self.__text1 = Label(self.__frame2, textvariable=self.__nbText, width=10, height=2, bg='black', fg='white') # Configuration du texte du joueur
        self.__text1.pack()                                                 # Configuration du texte du joueur                           
        self.buttons = [[Button(self.__frame1, width=6, height=3, bg='black', command=lambda i=i, j=j: self.placePion(i, j)) for j  in range(boardSize)] for i in range(boardSize)] # Configuration des boutons du plateau
        for i in range(boardSize):                                          # Boucle qui parcourt les lignes du plateau
            for j in range(boardSize):                                      # Boucle qui parcourt les colonnes du plateau
                self.buttons[i][j].grid(row=i, column=j)                    # Configuration des boutons du plateau
        self.debutJeu()                                                     # Début du jeu  

        self.window.mainloop()                                              # Boucle principale de la fenêtre

    def debutJeu(self):                                                     # Méthode qui démarre le jeu
        print("Début du jeu. Les joueurs peuvent placer leur premier pion où ils veulent.") # Affiche le début du jeu
        
    def disableButtons(self):                                               # Méthode qui désactive les boutons
        for row in self.buttons:                                            # Boucle qui parcourt les lignes du plateau              
            for button in row:                                              # Boucle qui parcourt les boutons du plateau
                button.config(state=DISABLED)                               # Désactive les boutons du plateau

    def finJeu(self):                                                       # Méthode qui vérifie si un joueur a gagné
        if self.jeu.winCondition() == True:                                 # Si un joueur a gagné
            print("Player " + str(self.pion.getPlayer() + 1) + " wins !")   # Affiche le joueur qui a gagné
            self.disableButtons()                                           # Désactive les boutons

    def restoreColor(self, x, y):                                           # Méthode qui restaure la couleur des boutons
        self.buttons[x][y].config(bg='black')                               # Restaure la couleur des boutons

    def changeColorPlayer1(self):                                           # Méthode qui change la couleur du bouton du joueur 1
        self.lastButton1.config(bg='green')                                 # Change la couleur du bouton du joueur 1

    def changeColorPlayer2(self):                                           # Méthode qui change la couleur du bouton du joueur 2
        self.lastButton2.config(bg='blue')                                  # Change la couleur du bouton du joueur 2
    
    
    def placePion(self, x, y):                                              # Méthode qui place le pion
        currentPlayer = self.pion.getPlayer()                               # Joueur du pion
        coupValide = False                                                  # Variable qui vérifie si le coup est valide

        if self.nbCoups < 2:                                                # Si le nombre de coups est inférieur à 2 (pour le premier et deuxième coup)
            self.pion.setX(x)                                               # Met à jour l'abscisse du pion
            self.pion.setY(y)                                               # Met à jour l'ordonnée du pion
            if currentPlayer == 0:                                          # Si le joueur est le joueur 1
                self.buttons[x][y].config(bg='#3FEE3C')                     # Change la couleur du bouton du joueur 1
                self.lastButton1 = self.buttons[x][y]                       # Dernier bouton du joueur 1
            else:                                                           # Sinon
                self.buttons[x][y].config(bg='#2ddff3')                     # Change la couleur du bouton du joueur 2
                self.lastButton2 = self.buttons[x][y]                       # Dernier bouton du joueur 2
            self.jeu.coords[currentPlayer] = [(x, y)]                       # Met à jour les coordonnées du joueur
            self.jeu.possibleMoves[currentPlayer] = []                      # Met à jour les mouvements possibles du joueur
            self.jeu.possibleMoves[currentPlayer] = self.jeu.moveCondition()# Met à jour les mouvements possibles du joueur   
            coupValide = True                                               # Le coup est valide
        else:                                                               # Sinon
            if self.jeu.updateBoard(x, y, self.nbCoups):                    # Si le plateau est mis à jour
                if currentPlayer == 0:                                      # Si le joueur est le joueur 1
                    self.buttons[x][y].config(bg='#3FEE3C')                 # Change la couleur du bouton du joueur 1
                    self.changeColorPlayer1()                               # Change la couleur du bouton du joueur 1
                    self.lastButton1 = self.buttons[x][y]                   # Dernier bouton du joueur 1
                else:                                                       # Sinon
                    self.buttons[x][y].config(bg='#2ddff3')                 # Change la couleur du bouton du joueur 2
                    self.changeColorPlayer2()                               # Change la couleur du bouton du joueur 2
                    self.lastButton2 = self.buttons[x][y]                   # Dernier bouton du joueur 2
                self.jeu.coords[currentPlayer] = [(x, y)]                   # Met à jour les coordonnées du joueur
                self.jeu.possibleMoves[currentPlayer] = []                  # Met à jour les mouvements possibles du joueur
                self.jeu.possibleMoves[currentPlayer] = self.jeu.moveCondition() # Met à jour les mouvements possibles du joueur
                coupValide = True                                           # Le coup est valide
            else:                                                           # Sinon
                self.buttons[x][y].config(bg='red')
                self.buttons[x][y].after(600, lambda: self.restoreColor(x, y)) # Restaure la couleur du bouton
                print("Mouvement invalide, veuillez réessayer.")            # Affiche un message d'erreur

        if coupValide == True:                                              # Si le coup est valide
            self.pion.updatePlayer()                                        # Met à jour le joueur du pion
            nextPlayer = self.pion.getPlayer()                              # Joueur du pion
            self.__nbText.set(f"Player {nextPlayer + 1}")                   # Met à jour le texte du joueur
            self.nbCoups += 1                                               # Incrémente le nombre de coups
            self.finJeu()                                                   # Vérifie si un joueur a gagné 

            
                
tailleJeu = int(input("Taille du plateau (entre 8 et 12) : "))              # Taille du plateau
while tailleJeu < 8 or tailleJeu > 12:                                      # Boucle qui vérifie si la taille du plateau est entre 8 et 12
    print("Erreur : La taille doit être entre 8 et 12.")                    # Affiche une erreur
    tailleJeu = int(input("Taille du plateau (entre 8 et 12) : "))          # Taille du plateau


game = GameInterface(tailleJeu)                                                 # Démarre le jeu