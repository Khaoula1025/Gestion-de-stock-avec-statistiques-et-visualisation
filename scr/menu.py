import stats
import visualize
import stock
products = stock.products
def menu(products):
    choix = 0
    while True:
        print('1. Ajouter un produit. ')
        print('2. Supprimer un produit. ')
        print('3. Modifier la quantité d’un produit. ')
        print('4. Afficher le stock. ')
        print('5. Afficher les statistiques. ')
        print('6. Afficher un graphique (choix : bar chart ou pie chart). ')
        print('7. Quitter.')
        choix = int(input('donner votre choix : '))
        match choix :
            case 1  :
                print('-------- Ajouter Produit -----------\n')
                stock.ajouter_produit(products)
            case 2  :
                print('-------- Supprimer Produit -----------\n')
                stock.delete_product(products)
            case 3  :
                print('-------- Modifier Produit -----------\n')
                stock.mettreAjourQ(products)
            case 4  :
                pass
            case 5  :
                print('-------- les statistiques du stock -----------\n')
                stats.val_total_stock(products)
                stats.averagePrice(products)
                stats.prix_min_max(products)
                stats.product_expensive_cheaper(products)
            case 6  :
                print('-------- Visualisations -----------\n')
                visualize.pie_chart(products)
                visualize.bar_chart(products)
            case 7  :
                break
menu(products)
    
    