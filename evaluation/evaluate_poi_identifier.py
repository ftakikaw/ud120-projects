#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

### it's all yours from here forward!  
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features, labels)

pred = clf.predict(features)

acc = accuracy_score(pred, labels)

print "acuracia antes train_test_split :", acc

from sklearn import cross_validation

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

acc = accuracy_score(pred, labels_test)

print "acuracia depois train_test_split :", acc

i = 0
pred_zero = []

while i < len(pred):
    
    pred_zero.append(0)
    i+=1
    
acc = accuracy_score(pred_zero, labels_test)    
    
print "acuracia todos zero (nao poi) :", acc

from sklearn import metrics

precision = metrics.precision_score(labels_test, pred_zero)

print "precisao :", precision

recall = metrics.recall_score(labels_test, pred_zero)

print "revocacao :", precision

previsoes = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
previsoes_verdadeiras = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print "precisao 2:", metrics.precision_score(previsoes_verdadeiras, previsoes)

print "revocacao 2", metrics.recall_score(previsoes_verdadeiras, previsoes)