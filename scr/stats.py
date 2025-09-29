import numpy as np
import data

products = data.products

def val_total_stock(products):
    quantite = products[:,1]
    prix = products[:,2]
    valeur_total = np.add.reduce(quantite * prix)
    # print(quantite * prix)
    return valeur_total
    
print(val_total_stock(products))