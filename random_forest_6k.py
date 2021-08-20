# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:50:02 2020
random forest on 500k, data 2.5M actors, 365421 000_1, 5759791 000_0 data points with 54 variables where 4 are movie IDs and 1 is actor Id.
Constructing the random forest to obtain same numebr of points from the 5M in order to balance calsses.
# 5-fold cross validation
@author: rabbitindamoon
"""
import pandas as pd
import numpy as np
import re as re
#import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
#import numba
#from numba import cuda
import matplotlib.pyplot as plt
#from sklearn.model_selection import learning_curve
#from sklearn.model_selection import validation_curve
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics


# =============================================================================
# 
# actors_data_000_1_pd = pd.read_csv('actors_data_000_1_pd.csv')
# actors_data_000_0_pd = pd.read_csv('actors_data_000_0_pd.csv')
# 
# sample_data = actors_data_000_0_pd.sample(n = 365421, replace = False, random_state = 2) 
# frames = [actors_data_000_1_pd, sample_data]
# results = pd.concat(frames)
# actors_data = results.sample(frac=1, replace = False, random_state = 3).reset_index(drop=True)
# 
# =============================================================================
#
##############  This is just for the column names... so I dont forget!
# =============================================================================
# column_names = ['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',

#                'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1',
#                'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'feature_binary_1',

#                'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 
#                'star_2_1', 'star_2_2', 'star_2_3','score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'feature_binary_2',
#                'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 
#                'star_3_1', 'star_3_2', 'star_3_3','score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 
#                'feature_binary_3', 

#                 'feature_binary_4'])
# 
# =============================================================================
actors_data_000_0_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_000_0_pd.csv')
actors_data_111_0_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_111_0_pd.csv')
actors_data_001_0_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_001_0_pd.csv')
actors_data_011_0_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_011_0_pd.csv')
actors_data_110_0_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_110_0_pd.csv')
actors_data_010_0_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_010_0_pd.csv')
actors_data_100_0_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_100_0_pd.csv')
actors_data_101_0_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_101_0_pd.csv')

actors_data_000_1_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_000_1_pd.csv')
actors_data_111_1_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_111_1_pd.csv')
actors_data_001_1_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_001_1_pd.csv')
actors_data_011_1_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_011_1_pd.csv')
actors_data_110_1_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_110_1_pd.csv')
actors_data_010_1_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_010_1_pd.csv')
actors_data_100_1_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_100_1_pd.csv')
actors_data_101_1_pd = pd.read_csv(r'D:\Thesis\code\20-02-10\actors_data_101_1_pd.csv')

sample_data = actors_data_000_0_pd.sample(n = 3000, replace = False, random_state = 2).reset_index(drop=True)
frames = [sample_data, actors_data_000_1_pd, actors_data_111_0_pd, actors_data_001_0_pd, actors_data_011_0_pd, 
          actors_data_110_0_pd, actors_data_010_0_pd, actors_data_100_0_pd, actors_data_101_0_pd, 
          actors_data_111_1_pd, actors_data_001_1_pd, actors_data_011_1_pd, actors_data_110_1_pd, 
          actors_data_010_1_pd, actors_data_100_1_pd, actors_data_101_1_pd]

results = pd.concat(frames)
actors_data = results.sample(frac=1, replace = False, random_state = 3).reset_index(drop=True)


#actors_data = pd.read_csv(r'D:\Thesis\code\20-02-04\all_variables\actors_data_rf.csv')



#The following code divides data into attributes and labels:

X = actors_data[['IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1','budget_1', 'box_office_1', 'feature_binary_1',
                 'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2','budget_2', 'box_office_2', 'feature_binary_2',
                 'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3','budget_3', 'box_office_3', 'feature_binary_3']]

# here i am using the dataset that will be 
y= actors_data['feature_binary_4']
# Saving feature names for later use

#The following code divides data into training and testing sets:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)


y_train=  y_train.astype('float')
y_test = y_test.astype('float')
y = y.astype('float')
X_train = X_train.astype('float')
X_test = X_test.astype('float')
X = X.astype('float')

print('Training Features Shape:', X_train.shape)
print('Training Labels Shape:', y_train.shape)
print('Testing Features Shape:', X_test.shape)
print('Testing Labels Shape:', y_test.shape)


#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=1000, n_jobs=-1)


#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)


# predictions
y_pred=clf.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation

#y_test=y_test.astype('int')
#y_pred=y_pred.astype('int')

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# Get numerical feature importances
importances = list(clf.feature_importances_)

# List of tuples with variable and importance
#feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]

# Sort the feature importances by most important first
#feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)

# Print out the feature and importances 
#[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];




print(pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

#cross validation part.  run cross-validation to get a better overview of the results.

rfc_cv_score = cross_val_score(clf, X, y, cv=5, scoring='roc_auc')

print(rfc_cv_score)

#printing results:
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))
print('\n')
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))
print('\n')
print("=== All AUC Scores ===")
print(rfc_cv_score)
print('\n')
print("=== Mean AUC Score ===")
print("Mean AUC Score - Random Forest: ", rfc_cv_score.mean())


#from yellowbrick.model_selection import CVScores
#visualizer = CVScores(model, cv=cv, scoring='f1_weighted')
#visualizer.fit(X, y)        # Fit the data to the visualizer
#visualizer.show()           # Finalize and render the figure

#Confusion matrix plot 
import seaborn as sn
plt.rcParams['figure.figsize'] = 8,6
cm = confusion_matrix(y_test, y_pred)
df_cm = pd.DataFrame(cm, range(2), range(2))
#plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
# Show confusion matrix in a separate window
#plt.matshow(cm)
sn.heatmap(cm, annot=True,annot_kws={"size": 16},cmap=plt.cm.Blues, fmt='g')# font size
plt.title('Confusion matrix')
#plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()

#importance variables graph, super nice.
importances = clf.feature_importances_
indices = np.argsort(importances)
features = X_train.columns
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.ylim([-1, X.shape[1]])
plt.xlabel('Relative Importance')
plt.tight_layout()
plt.show()



feature_importances = pd.DataFrame(clf.feature_importances_,
                                   index = X_train.columns,
                                    columns=['importance']).sort_values('importance', ascending=False)


# =============================================================================
# feature_importances.to_csv(r'D:\Thesis\code\20-02-04\wo_binary_for_3_movies\feature_importances_table.csv')
# X.to_csv(r'D:\Thesis\code\20-02-04\all_variables\X.csv')
# y.to_csv(r'D:\Thesis\code\20-02-04\all_variables\y.csv')
# X_test.to_csv(r'D:\Thesis\code\20-02-04\all_variables\X_test.csv')
# X_train.to_csv(r'D:\Thesis\code\20-02-04\all_variables\X_train.csv')
# 
# y_pred.to_csv(r'D:\Thesis\code\20-02-04\all_variables\y_pred.csv')
# y_test.to_csv(r'D:\Thesis\code\20-02-04\all_variables\y_test.csv')
# y_train.to_csv(r'D:\Thesis\code\20-02-04\all_variables\y_train.csv')
# 
# import csv
# with open('importances.txt', 'w') as filehandle:
#     for listitem in importances:
#         filehandle.write('%s\n' % listitem)
# =============================================================================



# =============================================================================
# 
# The features are always randomly permuted at each split. Therefore, the best found split may vary, 
# even with the same training data and max_features=n_features, if the improvement of the criterion 
# is identical for several splits enumerated during the search of the best split. To obtain a deterministic 
# behaviour during fitting, random_state has to be fixed.
# 
# =============================================================================





