import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns
from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('LoanReshaped.csv')
Status_col = df.iloc[:, 30]
df = df.drop(df.columns[30], axis=1)
df = pd.concat([Status_col, df], axis=1)

#Splitting the Data
from sklearn.model_selection import train_test_split, cross_val_score

X = df.iloc[:,1:]
y = df.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

from keras.models import Sequential
from keras.layers import Dense
# build the neural network model
nn = Sequential()
nn.add(Dense(10, input_dim=35, activation='relu'))
nn.add(Dense(5, activation='relu'))
nn.add(Dense(1, activation='sigmoid'))

# compile the model
nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model to the training data
nn.fit(X_train, y_train, epochs=50, batch_size=32)

# evaluate the model on the test data
loss, accuracy = nn.evaluate(X_train, y_train)

# print the test accuracy
print('Test accuracy:', accuracy)