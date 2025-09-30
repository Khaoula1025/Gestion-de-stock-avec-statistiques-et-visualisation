import numpy as np
import stock as stock

def val_total_stock(products):
    quantite = products[:,1]
    prix = products[:,2]
    valeur_total = np.add.reduce(quantite * prix)
    # print(quantite * prix)
    return valeur_total


def prix_min_max(products):
     # global products
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
     # print(f'Prix maximum {prix_max} , Prix minimum {prix_min}')
     return [prix_max,prix_min]

def averagePrice(products):
    prix_unitaire=products[:,2]
    return np.mean(prix_unitaire)

#print('moyen :',averagePrice(products))

def product_expensive_cheaper(products):
     min_max = prix_min_max(products)
     for product in products:
          if product[2] == min_max[0]:
               print(f'le produit le plus cher : {product[0]}')
          if product[2] == min_max[1]:
               print(f'le produit le moins cher : {product[0]}')
               
# print(val_total_stock(products))
# print(prix_min_max())