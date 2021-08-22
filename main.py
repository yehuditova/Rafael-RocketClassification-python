import pandas as pd
from ex1 import *
from ex2 import *
from ex3 import *
from ex4 import *
from ex5 import *

if __name__ == '__main__':
    data_frame = pd.read_csv('train.csv')
    data_frame.drop('targetName', inplace=True, axis=1)
    data_frame = data_frame.head(2000)
    types=[1,4,7,10]
    # types = [5,6]
    # types = [12, 15]
    # types=[1,16]
    training_set, test_set, test_vector = disassembly_data(data_frame, types)

    # print_histograma(training_set)

    # show_rates(data_frame=training_set, num_rates=0, num_types=types, op=0)

    # decision=make_decision(test_set)
    # score=f1_score(decision,test_vector,1, 16)
    # print(score)

    train_x = data_to_x_y_z(training_set,3)
    out_train = list(training_set['class'])
    test_x = data_to_x_y_z(test_set,3)
    out_test = list(test_vector)

    # m_RandomForestClassifier(train_x, out_train, test_x, out_test)
    m_PoissonRegressor(train_x,out_train,test_x,out_test)
    # m_DecisionTreeRegressor(train_x,out_train,test_x,out_test)
