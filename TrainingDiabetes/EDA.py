import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns
import os

"""EDA"""
def eda(data_path,output_path):        
    # importing dataset
    data = pd.read_csv(data_path)

    # Having a look into our data
    print(data.info)
    print(data.columns)
    print(data.head(10))

    print(data.describe().T)

    # Check Missing values
    print(data.isnull().sum())

    # getting the number of labels
    for col in data.columns:
        print(col, ':', len(data[col].unique()), 'lebels')


    # for better view of correlation
    corr = data.corr()
    ax = plt.subplot()
    sns_plot = sns.heatmap(corr,
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values)
    ax.figure.savefig(output_path+'/correlation_hetmap.png')
    plt.close()

    return data
    

