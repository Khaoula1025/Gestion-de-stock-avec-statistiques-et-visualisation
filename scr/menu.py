import stats
import visualize
import stock

def menu(products):
    newData=products
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
                newData=stock.ajouter_produit(newData)
            case 2  :
                print('-------- Supprimer Produit -----------\n')
                newData=stock.delete_product(newData)
            case 3  :
                print('-------- Modifier Produit -----------\n')
                stock.mettreAjourQ(newData)
            case 4  :
                stock.afficherStock(newData)
            case 5  :
                print('-------- les statistiques du stock -----------\n')
                stats.val_total_stock(newData)
                stats.averagePrice(newData)
                stats.prix_min_max(newData)
                stats.product_expensive_cheaper(newData)
            case 6  :
                print('-------- Visualisations -----------\n')
                visualize.pie_chart(newData)
                visualize.bar_chart(newData)
            case 7  :
                break

    
    