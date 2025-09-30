import matplotlib.pyplot as plt
import stock as stock
products = stock.products
def pie_chart(products):
     pr_name= []
     val_pr= []
     for p in products:
        pr_name.append(p[0])
        val_pr.append(p[1]*p[2])
    
     plt.pie(val_pr, labels= pr_name)
     plt.show()

#pie_chart()

def bar_chart(products):
    x=products[:,1]
    y=products[:,2]
    plt.bar(x,y)
    plt.show()
# bar_chart()