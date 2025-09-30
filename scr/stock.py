import numpy as np
import data as produit
import matplotlib.pyplot as plt
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

def produit_disponible():
    return products
def prix_min_max():
     global products
     count=0   
     for p in products:
          if count == 0:
             prix_min= float(p[2])
             prix_max= float(p[2])
             count= count+1
          elif float(p[2])<prix_min:
               prix_min = float(p[2])
               count= count+1
          elif float(p[2])>= prix_max:
               prix_max=float(p[2])
               count= count+1
     return f"Prix maximum {prix_max} , Prix minimum {prix_min}"

def pie_chart():
     pr_name= []
     val_pr= []
     for p in products:
        pr_name.append(p[0])
        val_pr.append(p[1]*p[2])
    
     plt.pie(val_pr, labels= pr_name)
     plt.show()

