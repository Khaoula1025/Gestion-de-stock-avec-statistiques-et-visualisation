def mettreAjourQ(n):
    products=n
    choix=input('enter product name : ')
    for i in n:
        if choix not in products[i[0]] :
            print('product not found ')
        else:
            q=int(print('enter the new quantity : '))
            products[i[1]]=q
    return products