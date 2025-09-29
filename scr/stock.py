import data
import numpy as np

products = data.stock


def delete_product(product_name, products):
    for product in products:
        product_index = np.where(product[0] == product_name)
        if product[0] == product_name:
            return np.delete(products, product_index)
