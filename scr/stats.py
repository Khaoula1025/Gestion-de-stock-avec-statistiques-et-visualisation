import numpy as np
import data
import stock as stock
products = stock.products

def val_total_stock(products):
    quantite = products[:,1]
    prix = products[:,2]
    valeur_total = np.add.reduce(quantite * prix)
    # print(quantite * prix)
    return valeur_total


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

def averagePrice(n):
    prix_unitaire=n[:,2]
    return np.mean(prix_unitaire)

print('moyen :',averagePrice(products))
 
print(val_total_stock(products))
print(prix_min_max())