# importing libraries
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

# import custom modules

import EDA
import spliting
# paths
data_path = str(os.getcwd())+'/data'+'/diabetes.csv'
output_path =  str(os.getcwd())+'/output/'

data = EDA.eda(data_path,output_path)

x_train,x_test,y_train, y_test = spliting.split(data,output_path)

"""MODEL"""

"""Logistic Regression"""
print("\n\n[INFO] For LogisticRegression")
# Create object for LogisticRegression.set max_iter>100 as the dataset is big
logisticRegr = LogisticRegression(solver='lbfgs', max_iter=300)
# training
logisticRegr.fit(x_train, y_train)
# Predicting on test data
logr_predict = logisticRegr.predict(x_test)

# Accuracy on test data
print("Accuracy On Test Data:", metrics.accuracy_score(y_test, logr_predict))

# visualize confusion matrix for logistic regression
cm = metrics.confusion_matrix(y_test, logr_predict)

print("Confusion matrix:")
print(cm)
labels = ['No-Diabates','Diabetes']
ax = plt.subplot()
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r');

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
ax.figure.savefig(output_path+'/confusion matrix for logistic regression.png')
plt.close()


# saving/serializing the model on the disk as pkl
filename = output_path+'/model_logreg.pkl'
pickle.dump(logisticRegr, open(filename, 'wb'))



"""Random Forest"""
print("\n\n[INFO] For Random Forest")
randomforest = RandomForestClassifier(n_estimators=20, random_state=0)
# training
randomforest.fit(x_train, y_train)
# Predicting on test data
y_pred = randomforest.predict(x_test)
print("Accuracy on Test Data:", metrics.accuracy_score(y_test, y_pred))

# visualize confusion matrix for Random Forest
cm = metrics.confusion_matrix(y_test, y_pred)
print("Confusion matrix:")
print(cm)
labels = ['No-Diabates','Diabetes']
ax = plt.subplot()
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r');

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
ax.figure.savefig(output_path+'/confusion matrix for Random Forest.png')
plt.close()

# saving/serializing the model on the disk as pkl
filename = output_path+'/model_random_forest.pkl'
pickle.dump(randomforest, open(filename, 'wb'))



"""KNN"""
print("\n\n[INFO] For KNN")
knn = KNeighborsClassifier(n_neighbors=25) # we can do grid search for optimal number of neighbors 
# training
knn.fit(x_train, y_train)
# Predicting on test data
knn_pred = knn.predict(x_test)

print("Accuracy on test data for KNN:", metrics.accuracy_score(y_test, knn_pred))

# visualize confusion matrix for KNN
cm = metrics.confusion_matrix(y_test, knn_pred)

print("Confusion matrix")
print(cm)

labels = ['No-Diabates','Diabetes']
ax = plt.subplot()
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r');

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
ax.figure.savefig(output_path+'/confusion matrix for KNN.png')
plt.close()

# saving/serializing the model on the disk as pkl
filename = output_path+'/model_KNN.pkl'
pickle.dump(randomforest, open(filename, 'wb'))
