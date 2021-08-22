import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

import math


# op0-all
# op1=15sec
# op2-up and down, all seconds
# op3-up and down, 15 seconds


def distance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt(math.pow(x2 - x1, 2) +
                  math.pow(y2 - y1, 2) +
                  math.pow(z2 - z1, 2) * 1.0)
    return (d)


def show_rates(data_frame,num_rates=0,num_types=[],op=0):
    # for i in range(1,data_frame['class'].max()+1):
    # num_types = [1,6]
    colors=['green','blue','yellow','red','orange','black']
    fig, axs = plt.subplots()
    for index, item in enumerate(num_types):
        # axs[index].set_title('Type {}'.format(item))
        cur_class = data_frame[data_frame['class'] == item]
        # cur_num_rates=num_rates
        # if cur_num_rates==0:
        #     cur_num_rates= cur_class.groupby("class").size()[item]
        r = random.random()
        b = random.random()
        g = random.random()
        print_route(cur_class, num_rates, axs,(r, g, b),op)
    fig.tight_layout()
    plt.show()



def print_route(data,num,axs,color,op):
    if num==0:
        num=data.shape[0]
    for i in range(num):
        x = list(data.iloc[i, 2:212:7])
        z = list(data.iloc[i, 4:212:7])
        new_x = []
        new_z = []
        for item in x:
            if str(item) != 'nan':
                new_x.append(item)
        for item in z:
            if str(item) != 'nan':
                new_z.append(item)
        if op==0:
            axs.plot(new_x, new_z,color=color)
        elif op==1:
            if x==new_x:
                axs.plot(new_x, new_z, color=color)
        elif op==2:
            for i in range(1,len(new_z)-1):
                if new_z[i-1]<new_z[i]<new_z[i+1]:
                    axs.plot(new_x, new_z, color=color)
                    break
        elif op==3:
            if x == new_x:
                for i in range(1, len(new_z) - 1):
                    if new_z[i - 1] <new_z[i] > new_z[i + 1]:
                        axs.plot(new_x, new_z, color=color)
                        break
        elif op == 4:
            axs.plot(new_x, color=color)
        elif op == 5:
            axs.plot(new_z, color=color)



