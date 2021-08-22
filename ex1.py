import math
import pandas as pd
import matplotlib.pyplot as plt

def print_histograma(data):
    d1=data.isnull().sum(axis=1).tolist()
    d2=[]
    for i in range(len(data)):
        dist=29-int(d1[i]/7)
        d2.append(math.sqrt(data.loc[i,"posX_{}".format(dist)]**2+data.loc[i,"posY_{}".format(dist)]**2))
    data["dist"]=d2
    for i in range(25):
        types=data[data["class"]==i+1]
        plt.hist(types["dist"],bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
        plt.grid(axis='y', alpha=0.75)
        plt.show()