# -*- coding: utf-8 -*-
"""Iris_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_xXgiyFa-WbNdzZr9I1vEH6dg-bGr37K

** Importing Libraries **
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

"""**Importing Dataset**"""

df = pd.read_csv("drive/My Drive/Projects/Iris/Iris.csv")

df.head()

df.tail()

print('Rows :',df.shape[0])
print('Columns :',df.shape[1])

df.describe()

df.info()

df.isnull().sum()

df['Species'].value_counts()

sns.pairplot(df,hue='Species',size=2)

df['Species'].value_counts().plot.bar(color = 'cyan', figsize = (5, 5))

plt.subplot(1, 2, 1)
plt.scatter(x = df['SepalLengthCm'], y = df['SepalWidthCm'], color = 'red', marker = 'o',)
plt.title('Length vs Width')
plt.xlabel('Sepal Length in cm')
plt.ylabel('Sepal Width in cm')

plt.subplot(1, 2, 2)
plt.scatter(x = df['SepalLengthCm'], y = df['PetalLengthCm'], color = 'blue', marker = 'x',)
plt.title('Sepal vs Petal')
plt.xlabel('Sepal Length in cm')
plt.ylabel('petal Length in cm')
plt.show()

features = list(df.columns)

print(features)

features.remove('Id')
features.remove('Species')

print(features)

Y = df.Species
X = df[features].values.astype(np.float32)

print(X.shape)
print(Y.shape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# standardization

#from sklearn.preprocessing import MinMaxScaler

#mm = MinMaxScaler()

# feeding the data to the scaler
#x_train = mm.fit_transform(x_train)
#x_test = mm.transform(x_test)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

# feeding the into the scaler

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

"""**Using Machine Learning to solve the Iris Dataset**

**Support Vector Classifier**
"""

model = SVC()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("training accuracy :", model.score(x_train, y_train))
print("testing accuracy :", model.score(x_test, y_test))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)

"""**Decision Tree**"""

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("training accuracy :", model.score(x_train, y_train))
print("testing accuracy :", model.score(x_test ,y_test))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)

"""**Random Forest**"""

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("training accuracy :", model.score(x_train, y_train))
print("testing accuracy :", model.score(x_test, y_test))

cm = confusion_matrix(y_test, y_pred)
print(cm)

"""**Logistic Regression**"""

model = LogisticRegression(C = 1000, random_state = 0)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("training accuracy :", model.score(x_train, y_train))
print("testing accuracy :", model.score(x_test, y_test))

cm = confusion_matrix(y_test,y_pred)
print(cm)

"""**Using Neural Networks to solve Iris Dataset**

**Importing the libraries**
"""

from sklearn.neural_network import MLPClassifier
import tensorflow as tf
import seaborn as sns

"""**Multi Layer Perceptron**"""

model = MLPClassifier(hidden_layer_sizes = (100, 100), max_iter = 150)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("training accuracy :", model.score(x_train, y_train))
print("testing accuracy :", model.score(x_test, y_test))

cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.linear_model import Perceptron

model = Perceptron()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Misclassified Samples : %d" %(y_test != y_pred).sum())

print("Training Accuracy :", model.score(x_train, y_train))
print("Testing Accuracy :", model.score(x_test, y_test))

cm = confusion_matrix(y_pred, y_test)
print("Confusion Matrix :",cm)

