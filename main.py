# 23/10

#  tic tac toe , version 0.1, lucas & fred

import os
 
os.system('cls') # cls= clear screen , sur systeme linux c une autre commande : clear

""""

l'idee de base etant que a chaque exectution la fenetre terminal soit remise a zero
pour une meilleur lisibilité

"""


# noius definisson et creeons le plateau de jeu , separation par 9 x 'i'


def afficher_plateau(plateau_de_jeu):
    for ligne in plateau_de_jeu:
        print(" | ".join(ligne))
        print("-" * 9) 
        
""""
je definie le plateau de jeu colonnes representer par |
et lignes se materialisant par '-' , 9 x "-" , car 3 cases de 3 carachteres par lignes 


"""





def verifier_victoire(plateau_de_jeu, joueur):
    # Vérifie les lignes, les colonnes et les diagonales
    for ligne in plateau_de_jeu:
        if all(s == joueur for s in ligne):
            return True
    for col in range(3):
        if all(plateau_de_jeu[row][col] == joueur for row in range(3)):
            return True
    if all(plateau_de_jeu[i][i] == joueur for i in range(3)) or all(plateau_de_jeu[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def partie_tic_tac_toe():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueurs = ["Lucas", "Fred"]
    tour = 0

    """ 
    ici nous definisson le nom des joueurs , a savoir nos prenoms
    """



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
                print("Entrée non valide. Veuillez entrer des valeurs entre 0 et 2.")

        if verifier_victoire(plateau, joueur):
            afficher_plateau(plateau)
            print(f"Félicitations ! Le joueur {joueur} a gagné !")
            return

        tour += 1

    afficher_plateau(plateau)
    print("C'est un match nul !")

if __name__ == "__main__":
    partie_tic_tac_toe()
