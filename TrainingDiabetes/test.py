import pickle
import pandas as pd
import numpy as np
import os

#load scaler
scl = str(os.getcwd())+'/output'+'/sc.pkl'
scaler = pickle.load(open(scl, 'rb'))

#load model
mod = str(os.getcwd())+'/output'+'/model_logreg.pkl'
model = pickle.load(open(mod, 'rb'))

mod1 = str(os.getcwd())+'/output'+'/sc.pkl'+'/model_random_forest.pkl'
randomforest = pickle.load(open(mod, 'rb'))


test_df=pd.DataFrame({'Pregnancies':[7],
                     'Glucose':[48],
                     'BloodPressure':[80],
                     'SkinThickness':[35],
                     'Insulin':[0],
                     'BMI':[33.5],
                      'DiabetesPedigreeFunction':[0.201],
                      'Age':[50],
                      })


print(type(test_df))
a=np.array(test_df)
print(a)
data = scaler.transform(a)
print(data)

prediction = model.predict(data)
print(prediction)