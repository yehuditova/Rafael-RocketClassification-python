# def test(sol,real,types=(1,16)):
#     for item in sol:
#
#
import math


def make_decision(data):
    dict={}
    for i in range(len(data.index)):
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
        if new_x[-1]/len(new_x)<4000/30:
            dict[data.iloc[i, 0]]=1
        else:
            dict[data.iloc[i, 0]] = 16
    return dict


def f1_score(train_classification, real_classification, class_1, class_2):
    confusion_matrix=[[0,0],[0,0]]
    for id in train_classification:
        t_classification = train_classification[id]
        r_classification=real_classification[id]
        if t_classification==class_1 and r_classification==class_1:
            confusion_matrix[0][0]+=1
        if t_classification==class_2 and r_classification==class_1:
            confusion_matrix[0][1]+=1
        if t_classification==class_1 and r_classification==class_2:
            confusion_matrix[1][0]+=1
        if t_classification==class_2 and r_classification==class_2:
            confusion_matrix[1][1]+=1
    # print(confusion_matrix)
    recall=confusion_matrix[1][1]/(confusion_matrix[1][1]+confusion_matrix[1][0])
    precision=confusion_matrix[1][1]/(confusion_matrix[1][1]+confusion_matrix[0][1])
    f1_score=(2*recall*precision)/(recall+precision)
    # print(f1_score)
    return f1_score





def kineticEnergy(M, V):
    # Stores the Kinetic Energy
    KineticEnergy = 0.5 * M * V * V
    return KineticEnergy


# Function to calculate Potential Energy
def potentialEnergy(M, H):
    # Stores the Potential Energy
    PotentialEnergy = M * 10 * H
    return PotentialEnergy

def find_energy(h,x,y,z):
    energy = potentialEnergy(1, h) + kineticEnergy(1, math.sqrt(x * x + y * y + z * z))
    return energy

