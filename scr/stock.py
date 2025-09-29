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