import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

""" Spliting and scaling"""
def split(encoded_data,output_path):
        
    # Splitting the dataset into independent(x) and dependent/target(y) variable/features
    x = encoded_data.iloc[:, :-1].values
    y = encoded_data.iloc[:, -1].values


    # Splitting the variables/features into train and test set by 80/20 (80% for training and 20% for testing)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # Normalizing or scalling the dataset into norml/binomial/gaussian distribution
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    # saving the scalling object for using while inference
    filename = output_path+'/sc.pkl'
    pickle.dump(sc, open(filename, 'wb'))

    return x_train,x_test,y_train, y_test