import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures, StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC, SVC
import warnings
import time

# read data
df = pd.read_pickle("../Datasets/matches_full.pkl")
df.head()

# shape
df.shape

# train test
train = df.loc[:int(df.shape[0]*0.7)]
test = df.loc[int(df.shape[0]*0.7)+1:]

# selected stats from team
selected_stats_from_team = ['gf_average', 'ga_average', 'poss_average', 'sot%_average', 'saves_average', 
                  'stp_average', '#opa_average', 'kp_average', 'crspa_average', 
                  'tkl_average', 'blocks_average', 'int_average', 'att_y_average', 
                            'succ%_average', 'venue_encoded', 'team_encoded']

# select stats
selected_stats_from_opponent = [f"{stat}_opponent" for stat in selected_stats_from_team]
predictors = selected_stats_from_team + selected_stats_from_opponent
predictors.remove('venue_encoded_opponent')
predictors

# LinearSVC doesn't have predict_proba. So we use SVC
# make a pipeline
svm_pipeline = make_pipeline(StandardScaler(), SVC(probability=True))

# parameters grid
param_grid = {
    'svc__kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
    'svc__degree': [2, 3, 4],
    'svc__gamma': [0.1, 0.6, 1, 10],
    'svc__C': [0.1, 1, 5, 10]
}

# carry out a GridSearchCV
grid_search = GridSearchCV(svm_pipeline, param_grid, cv=5)

# Fit the grid search to training data
start_time = time.time()
grid_search.fit(train[predictors], train['result_encoded'])
end_time = time.time()
fit_duration = end_time - start_time

svm_clf.fit(train[predictors], train['result_encoded'])

# test
prob_preds = svm_clf.predict_proba(test[predictors])
preds = svm_clf.predict(test[predictors])

print("a", 1)

print("Accuracy on test set", accuracy_score(test['result_encoded'], preds))

preds_on_training = svm_clf.predict(train[predictors])
print("Accuracy on training set", accuracy_score(train['result_encoded'], preds_on_training))