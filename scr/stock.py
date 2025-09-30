import numpy as np
import data as produit
def mettreAjourQ(n):
    choix=input('enter product name : ')
    found=False
    for i in n:
        if i[0].lower()==choix.lower() :
             q=int(input('enter the new quantity : '))
             i[1]=q
             found=True
             break
    if not found :
            print('product not found ')
           
    return n

products =produit.products
def ajouter_produit():
    global products
    nom_produit= input("inserer nom produit: ")
    prix= float(input("inserer le prix du produit: "))
    quantite= int(input("inserer la quantite du produit"))
    new_produit= [nom_produit, prix, quantite]
    products = np.vstack([produit.products , new_produit])
    print(products)


def delete_product():
    
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
# print(delete_product(products))




