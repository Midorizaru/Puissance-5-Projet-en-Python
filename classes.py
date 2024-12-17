from tkinter import *                                                       # Importation de la bibliothèque tkinter

class Pion:                                                                 # Classe Pion                                        
    def __init__(self, abscisse = -1, ordonnee = -1, player = 0):           # Constructeur de la classe Pion
        self.__x = abscisse                                                 # Abscisse du pion
        self.__y = ordonnee                                                 # Ordonnée du pion
        self.__player = player                                              # Joueur du pion                          

    def getX(self):                                                         # Getter de l'abscisse du pion                               
        return self.__x                                                     # Retourne l'abscisse du pion
    def getY(self):                                                         # Getter de l'ordonnée du pion
        return self.__y                                                     # Retourne l'ordonnée du pion                 

    def setX(self, newX):                                                   # Setter de l'abscisse du pion                                  
        self.__x = newX                                                     # Modifie l'abscisse du pion
    def setY(self, newY):                                                   # Setter de l'ordonnée du pion                     
        self.__y = newY                                                     # Modifie l'ordonnée du pion

    def getPlayer(self):                                                    # Getter du joueur du pion
        return self.__player                                                # Retourne le joueur du pion

    def setPlayer(self, newPlayer):                                         # Setter du joueur du pion
        self.__player = newPlayer                                           # Modifie le joueur du pion

    def updatePlayer(self):                                                 # Méthode qui change le joueur du pion
        self.__player = (self.__player + 1) % 2                             # Modifie le joueur du pion


class Jeu:                                                                  # Classe Jeu
    def __init__(self, boardSize, pion):                                    # Constructeur de la classe Jeu
        self.__boardSize = boardSize                                        # Taille du plateau             
        self.pion = pion                                                    # Pion du jeu                       
        self.__Board = self.plateau(boardSize)                              # Plateau du jeu       
        self.coords = {0: [], 1: []}                                        # Coordonnées des pions des joueurs                      
        self.possibleMoves = {0: [], 1: []}                                 # Mouvements possibles des joueurs                      


    def plateau(self, boardSize):                                           # Méthode qui crée le plateau du jeu
        board = []                                                          # Liste qui contiendra le plateau                         
        for i in range(boardSize):                                          # Boucle qui parcourt les lignes du plateau               
            line = []                                                       # Liste qui contiendra les lignes du plateau
            for j in range(boardSize):                                      # Boucle qui parcourt les colonnes du plateau                 
                line.append(0)                                              # Ajoute un 0 à la ligne  
            board.append(line)                                              # Ajoute la ligne au plateau
        return board                                                        # Retourne le plateau


    def moveCondition(self):                                                # Méthode qui vérifie les mouvements possibles
        currentPlayer = self.pion.getPlayer()                               # Joueur du pion
        if currentPlayer in self.coords:                                    # Si le joueur a déjà placé un pion
            coords_player = self.coords[currentPlayer]                      # coord = coordonnées du pion du joueur
            x = coords_player[0][0]                                         # Abscisse du pion du joueur    
            y = coords_player[0][1]                                         # Ordonnée du pion du joueur
        else:                                                               # Sinon                                
            x, y = -1, -1                                                   # Abscisse et ordonnée du pion du joueur = -1 = Erreur

        possibleCoords = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]               # Liste des mouvements possibles
        for possibleCoordsX, possibleCoordsY in possibleCoords:                                                 # Boucle qui parcourt les mouvements possibles   
            newX, newY = x + possibleCoordsX, y + possibleCoordsY                                               # Nouvelles coordonnées du pion du joueur
            if 0 <= newX < self.__boardSize and 0 <= newY < self.__boardSize and self.__Board[newX][newY] == 0: # Si les coordonnées sont dans le plateau et que la case est vide
                self.possibleMoves[currentPlayer].append((newX, newY))                                          # Ajoute les coordonnées à la liste des mouvements possibles
        return self.possibleMoves[currentPlayer]                                                                # Retourne la liste des mouvements possibles


    def winCondition(self):                                                 # Méthode qui vérifie si un joueur a gagné
        boardSize = self.__boardSize                                        # Taille du plateau 
        rows, cols = boardSize, boardSize                                   # Nombre de lignes et de colonnes du plateau               
        currentPlayer = self.pion.getPlayer()                               # Joueur du pion

        # Vérification de la victoire horizontale
        for row in range(rows):                                             # Boucle qui parcourt les lignes du plateau
            for col in range(cols - alignement + 1):                        # Boucle qui parcourt les colonnes du plateau
                victoire = True                                             # assignation de la variable victoire à True pour chaque case
                for i in range(alignement):                                 # Boucle qui parcourt les cases alignées                    
                    if self.__Board[row][col + i] != currentPlayer + 1:     # Si la case d'apès n'est pas égale au joueur + 1 car pour la machine joueur = 0 ou 1 et pour l'humain joueur = 1 ou 2
                        victoire = False                                    # assignation de la variable victoire à False car il n'y a pas de victoire
                        break                                               # Sort de la boucle
                if victoire:                                                # Si victoire = True
                    print(f"Victoire horizontale détectée en ligne {row}, colonne {col} à {col + alignement - 1}") # Affiche la victoire horizontale
                    return True                                             # Retourne True pour la suite du programme

        # Vérification de la victoire verticale
        for row in range(rows - alignement + 1):                            # Boucle qui parcourt les lignes du plateau
            for col in range(cols):                                         # Boucle qui parcourt les colonnes du plateau    
                victoire = True                                             # assignation de la variable victoire à True pour chaque case    
                for i in range(alignement):                                 # Boucle qui parcourt les cases alignées
                    if self.__Board[row + i][col] != currentPlayer + 1:     # Si la case d'en dessous n'est pas égale au joueur + 1 car pour la machine joueur = 0 ou 1 et pour l'humain joueur = 1 ou 2
                        victoire = False                                    # assignation de la variable victoire à False car il n'y a pas de victoire
                        break                                               # Sort de la boucle
                if victoire:                                                # Si victoire = True
                    print(f"Victoire verticale détectée en ligne {row}, à {row + alignement - 1}, colonne {col}") # Affiche la victoire verticale
                    return True                                             # Retourne True pour la suite du programme

        # Vérification de la victoire diagonale (\\)
        for row in range(rows - alignement + 1):                            # Boucle qui parcourt les lignes du plateau
            for col in range(cols - alignement + 1):                        # Boucle qui parcourt les colonnes du plateau   
                victoire = True                                             # assignation de la variable victoire à True pour chaque case
                for i in range(alignement):                                 # Boucle qui parcourt les cases alignées
                    if self.__Board[row + i][col + i] != currentPlayer + 1: # Si la case d'apres, en dessous est pas égale au joueur + 1 car pour la machine joueur = 0 ou 1 et pour l'humain joueur = 1 ou 2
                        victoire = False                                    # assignation de la variable victoire à False car il n'y a pas de victoire  
                        break                                               # Sort de la boucle
                if victoire:                                                # Si victoire = True
                    print(f"Victoire diagonale (\\) détectée de ({row}, {col}) à ({row + alignement - 1}, {col + alignement - 1})") # Affiche la victoire diagonale (\\)
                    return True                                             # Retourne True pour la suite du programme

        # Vérification de la victoire diagonale (//)
        for row in range(alignement - 1, rows):                             # Boucle qui parcourt les lignes du plateau
            for col in range(cols - alignement + 1):                        # Boucle qui parcourt les colonnes du plateau
                victoire = True                                             # assignation de la variable victoire à True pour chaque case
                for i in range(alignement):                                 # Boucle qui parcourt les cases alignées
                    if self.__Board[row - i][col + i] != currentPlayer + 1: # Si la case d'après, au dessus est pas égale au joueur + 1 car pour la machine joueur = 0 ou 1 et pour l'humain joueur = 1 ou 2
                        victoire = False                                    # assignation de la variable victoire à False car il n'y a pas de victoire
                        break                                               # Sort de la boucle
                if victoire:                                                # Si victoire = True
                    print(f"Victoire diagonale (//) détectée de ({row}, {col}) à ({row - alignement + 1}, {col + alignement - 1})") # Affiche la victoire diagonale (//)
                    return True                                             # Retourne True pour la suite du programme

        return False                                                        # Retourne False si il n'y a pas de victoire
    
    
    def updateBoard(self, x, y, nbCoups):                                   # Méthode qui met à jour le plateau
        currentPlayer = self.pion.getPlayer()                               # Joueur du pion
        if nbCoups > 1 and (x, y) not in self.possibleMoves[currentPlayer]: # Si le nombre de coups est supérieur à 1 et que les coordonnées ne sont pas dans les mouvements possibles
            return False                                                    # Retourne False

        if (x, y) in self.moveCondition() or nbCoups <= 1:                  # Si les coordonnées sont dans les mouvements possibles ou si le nombre de coups est inférieur ou égal à 1
            self.__Board[x][y] = currentPlayer + 1                          # Met à jour le plateau
            self.pion.setX(x)                                               # Met à jour l'abscisse du pion
            self.pion.setY(y)                                               # Met à jour l'ordonnée du pion    
            nbCoups += 1                                                    # Incrémente le nombre de coups                     
            return True                                                     # Retourne True      
        return False                                                        # Retourne False si il n'y a pas de victoire
    

alignement = int(input("Nombre d'alignement pour gagner (entre 4 et 6) : "))     # Nombre d'alignement pour gagner
while alignement < 4 or alignement > 6:                                          # Boucle qui vérifie si le nombre d'alignement est entre 4 et 6
    print("Erreur : Le nombre d'alignement doit être entre 4 et 6.")             # Affiche une erreur
    alignement = int(input("Nombre d'alignement pour gagner (entre 4 et 6) : ")) # Nombre d'alignement pour gagner
