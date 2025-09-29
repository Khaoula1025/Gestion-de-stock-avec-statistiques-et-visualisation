import numpy as np
import data as produit

products =produit.products
def ajouter_produit():
    nom_produit= input("inserer nom produit: ")
    prix= input("inserer le prix du produit: ")
    quantite= int(input("inserer la quantite du produit"))
    new_produit= [nom_produit, prix, quantite]
    products = np.vstack([produit.products , new_produit])
    print(products)
# ajouter_produit()


def delete_product(products):
    product_name = input("donner le nom du produit : ")
    product_index = None
    for i,product in enumerate(products):
        if product[0].lower() == product_name.lower():
            product_index =i
            break 
        
    if product_index is not None:
        new_list = np.delete(products, product_index,axis=0)
        return new_list
    else:
        return 'produit introuvable'
print(delete_product(products))


