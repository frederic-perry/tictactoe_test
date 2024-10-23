# 23/10

import os
 
os.system('cls') #pour Windows
os.system('clear') #pour linux


# je creer le plateau de jeu


def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9) # 9 x -

def verifier_victoire(plateau, joueur):
    # Vérifie les lignes, les colonnes et les diagonales
    for ligne in plateau:
        if all(s == joueur for s in ligne):
            return True
    for col in range(3):
        if all(plateau[row][col] == joueur for row in range(3)):
            return True
    if all(plateau[i][i] == joueur for i in range(3)) or all(plateau[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def partie_tic_tac_toe():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueurs = ["X", "O"]
    tour = 0

    while tour < 9:
        joueur = joueurs[tour % 2]
        afficher_plateau(plateau)
       
        while True:
            try:
                ligne = int(input(f"Joueur {joueur}, entrez la ligne (0, 1, 2) : "))
                col = int(input(f"Joueur {joueur}, entrez la colonne (0, 1, 2) : "))
                if plateau[ligne][col] == " ":
                    plateau[ligne][col] = joueur
                    break
                else:
                    print("Cette case est déjà prise. Essayez à nouveau.")
            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez entrer des valeurs entre 0 et 2.")

        if verifier_victoire(plateau, joueur):
            afficher_plateau(plateau)
            print(f"Félicitations ! Le joueur {joueur} a gagné !")
            return

        tour += 1

    afficher_plateau(plateau)
    print("C'est un match nul !")

if __name__ == "__main__":
    partie_tic_tac_toe()