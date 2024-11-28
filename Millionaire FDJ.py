import random

def jeu_millionnaire():
    print("\nBienvenue au jeu de la roue du millionnaire de la FDJ!")
    print("\nVoici les montants possibles sur la roue:")

    # Montants sur la roue
    montants = [
        0, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 50000, 100000, 1000000
    ]

    # Afficher les montants pour information
    for montant in montants:
        print(f"- {montant} euros")

    print("\nTournez la roue et découvrez votre gain unique!")

    # Simuler la roue
    gain = random.choice(montants)

    print("\nLa roue tourne...")
    print("\nFélicitations! Vous avez gagné:")
    print(f"{gain} euros!")

    print("\nMerci d'avoir joué au jeu du millionnaire de la FDJ!")

# Lancer le jeu
jeu_millionnaire()
