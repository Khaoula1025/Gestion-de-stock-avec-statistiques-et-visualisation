import numpy as np
import data as produit
def ajouter_produit():
    nom_produit= input("inserer nom produit: ")
    prix= input("inserer le prix du produit: ")
    quantite= int(input("inserer la quantite du produit"))
    new_produit= [nom_produit, prix, quantite]
    