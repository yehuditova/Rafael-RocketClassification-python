import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.linear_model import PoissonRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from ex4 import *

from sklearn.linear_model import LogisticRegression


def data_to_x_y_z(data, op=0):
    sol = []
    for i in range(data.shape[0]):
        x_pos = list(data.iloc[i, 2:212:7])
        y_pos = list(data.iloc[i, 3:212:7])
        z_pos = list(data.iloc[i, 4:212:7])
        x_vel = list(data.iloc[i, 5:212:7])
        y_vel = list(data.iloc[i, 6:212:7])
        z_vel = list(data.iloc[i, 7:212:7])

        new_x_pos = []
        new_y_pos = []
        new_z_pos = []
        new_x_vel = []
        new_y_vel = []
        new_z_vel = []
        for item in x_pos:
            if str(item) != 'nan':
                new_x_pos.append(item)
            else:
                break
        for item in y_pos:
            if str(item) != 'nan':
                new_y_pos.append(item)
            else:
                break
        for item in z_pos:
            if str(item) != 'nan':
                new_z_pos.append(item)
            else:
                break

        for item in x_vel:
            if str(item) != 'nan':
                new_x_vel.append(item)
            else:
                break
        for item in y_vel:
            if str(item) != 'nan':
                new_y_vel.append(item)
            else:
                break
        for item in z_vel:
            if str(item) != 'nan':
                new_z_vel.append(item)
            else:
                break

        energy = find_energy(new_z_pos[-1], new_x_vel[-1], new_y_vel[-1], new_z_vel[-1])
        energy_pre = find_energy(new_z_pos[0], new_x_vel[0], new_y_vel[0], new_z_vel[0])
        if op == 0:
            sol.append([new_x_pos[-1], new_y_pos[-1], new_z_pos[-1], new_x_vel[-1], new_y_vel[-1], new_z_vel[-1],
                        len(new_x_pos), energy])
        elif op == 1:
            sol.append([new_x_pos[-1], new_y_pos[-1], new_z_pos[0], new_z_pos[-1], len(new_x_pos), energy])
        elif op == 2:
            sol.append([new_x_pos[-1], new_y_pos[-1], new_z_pos[0], new_z_pos[-1], len(new_x_pos), energy, energy_pre])
        elif op == 3:
            length = len(new_x_pos)
            ind1 = int(length / 4)
            ind2 = int((length / 4) * 2)
            ind3 = int((length / 4) * 3)
            cur_item = []
            cur_indexes = [0, ind1, ind2, ind3, -1]
            for i in cur_indexes:
                cur_item.extend((new_x_pos[i], new_y_pos[i], new_z_pos[i],
                                 find_energy(new_z_pos[i], new_x_vel[i], new_y_vel[i], new_z_vel[i])))
            cur_item.append(len(new_x_pos))
            sol.append(cur_item)

    return sol


def m_PoissonRegressor(X_train, y_train, X_test, y_test):
    classifier = LogisticRegression()
    # X_train=np.array(X_train).reshape(-1, 1)
    y_train = np.array(y_train).reshape(-1, 1)

    # X_test = np.array(X_test).reshape(-1, 1)
    y_test = np.array(y_test).reshape(-1, 1)

    # print(X_train.shape)
    # print(y_train.shape)
    # print(X_test.shape)
    # print(y_test.shape)

    classifier.fit(X_train, y_train)
    print(classifier.score(X_train, y_train))
    print(classifier.score(X_test, y_test))


def m_RandomForestClassifier(X_train, y_train, X_test, y_test):
    classifier = RandomForestClassifier(n_estimators=10, max_depth=8)
    classifier.fit(X_train, y_train)
    fig, axs = plt.subplots(2)
    axs[0].plot(classifier.predict_proba(X_train))
    axs[1].plot(classifier.predict_proba(X_test))
    print(classifier.score(X_train, y_train))
    print(classifier.score(X_test, y_test))

    plt.show()


def m_DecisionTreeRegressor(X_train, y_train, X_test, y_test):
    classifier = DecisionTreeRegressor(max_depth=7)
    classifier.fit(X_train, y_train)
    tree.plot_tree(classifier,fontsize=10)
    print(classifier.score(X_train, y_train))
    print(classifier.score(X_test, y_test))

    plt.show()

