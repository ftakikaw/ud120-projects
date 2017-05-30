#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC

#clf = SVC(kernel="linear")
clf = SVC(C=10000, kernel="rbf")

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

print "Inicio treinamento: ", time.asctime( time.localtime(time.time()) )
clf.fit(features_train, labels_train)
print "Termino treinamento: ", time.asctime( time.localtime(time.time()) )

print "Inicio Teste: ", time.asctime( time.localtime(time.time()) )
pred = clf.predict(features_test)
print "Termino Teste: ", time.asctime( time.localtime(time.time()) )

print "no. of Chris predicted emails:", sum(pred)
print "no. of Sara predicted emails:", len(pred)-sum(pred)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc
#########################################################


