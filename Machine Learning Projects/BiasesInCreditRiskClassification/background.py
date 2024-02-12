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

#Random Forest Classifier
from sklearn.ensemble import AdaBoostClassifier

clf = AdaBoostClassifier(n_estimators=200, random_state=42)
# scores = cross_val_score(model, X_train, y_train, cv=10, scoring='f1_macro', error_score="raise")
# print('CV score:', scores.mean(), "+/-", scores.std())

param_grid = {
    'n_estimators': [100, 200, 400, 600, 800], 
}

# create a GridSearchCV object with the specified hyperparameter grid
grids = GridSearchCV(clf, param_grid, cv=5, scoring = ['f1_macro', 'precision', 'recall'], refit='f1_macro', verbose = 1)

# fit the grid search object to the data
grids.fit(X_train , y_train)

# print the best hyperparameters and the corresponding score
print("Best hyperparameters: ", grids.best_params_)
print("Best score: ", grids.best_score_)