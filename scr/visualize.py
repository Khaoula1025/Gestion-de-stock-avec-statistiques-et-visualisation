import matplotlib.pyplot as plt
import stock as stock
def pie_chart(products):
     pr_name= []
     val_pr= []
     for p in products:
        pr_name.append(p[0])
        val_pr.append(p[1]*p[2])
    
     plt.pie(val_pr, labels= pr_name)
     plt.show()
     plt.savefig('documents/pie_chart.png')


def bar_chart(products):
    x=products[:,1]
    y=products[:,2]
    plt.bar(x,y)
    plt.show()
    plt.savefig('documents/bar_chart.png')

