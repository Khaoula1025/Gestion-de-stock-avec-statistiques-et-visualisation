import numpy as np
import data as produit

products =produit.products
def ajouter_produit():
    global products
    nom_produit= input("inserer nom produit: ")
    prix= input("inserer le prix du produit: ")
    quantite= int(input("inserer la quantite du produit"))
    new_produit= [nom_produit, prix, quantite]
    products = np.vstack([produit.products , new_produit])
    print(products)

print('product added')
def produit_disponible():
    return products
