import matplotlib.pyplot as plt
import stock as stock
products = stock.products
def pie_chart():
     pr_name= []
     val_pr= []
     for p in products:
        pr_name.append(p[0])
        val_pr.append(p[1]*p[2])
    
     plt.pie(val_pr, labels= pr_name)
     plt.show()
pie_chart()