#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""
from __future__ import division
import pickle
import sys
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.cross_validation import train_test_split

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### Training and testing sets
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)

### Decision tree 
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "accuracy:", accuracy_score(labels_test, pred)

### evaluation
values, counts = np.unique(pred, return_counts=True)
test_size = len(features_test)
print "predicted POIs:", zip(values, counts)
print "total no in test set:", test_size
print "accuracy if all poi=0:", counts[0]/test_size

true_positives = 0
for actual, predicted in zip(labels_test, pred):
    if actual==1 and predicted==1:       
        true_positives += 1

print "true positives:", true_positives
print "precision score:", precision_score(labels_test, pred)
print "recall score:", recall_score(labels_test, pred)  


prediction_labels = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]



def calc_precision_and_recall(actual, predicted):
    print "Calculating precision and recall..."    
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    true_negatives = 0
    for a, p in zip(actual, predicted):
        if a==1 and p==1:
            true_positives += 1
        elif a==1 and p==0:
            false_negatives += 1
        elif a==0 and p==1:
            false_positives += 1
        else:
            true_negatives += 1
    print "precision:", true_positives/(true_positives+false_positives)
    print "recall:", true_positives/(true_positives+false_negatives)
    
    
calc_precision_and_recall(true_labels, prediction_labels)