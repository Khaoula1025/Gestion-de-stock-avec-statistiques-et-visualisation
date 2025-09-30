import numpy as np
import data as produit
def mettreAjourQ(products):
    choix=input('enter product name : ')
    found=False
    for i in products:
        if i[0].lower()==choix.lower() :
             q=int(input('enter the new quantity : '))
             i[1]=q
             found=True
             break
    if not found :
            print('product not found ')
def ajouter_produit(products):
    # global products
    nom_produit= input("inserer nom produit: ")
    prix= float(input("inserer le prix du produit: "))
    quantite= int(input("inserer la quantite du produit"))
    new_produit= [nom_produit, prix, quantite]
    return np.vstack([products , new_produit])


def delete_product(products):
    product_name = input("donner le nom du produit : ")
    product_index = None
    for i,product in enumerate(products):
        if product[0].lower() == product_name.lower():
            product_index =i
            break 
        
    if product_index is not None:
        return np.delete(products, product_index,axis=0)
    else:
        return 'produit introuvable'

def afficherStock(products):
     print(products)
     
#print(delete_product(products))


