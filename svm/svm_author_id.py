#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
    
    RESULTS
    training time: 366.834 s
    prediction time: 39.315 s
    Accuracy: 0.984072810011
    
    Reduced dataset
    training time: 0.208 s
    prediction time: 2.223 s
    Accuracy: 0.884527872582
   
    Reduced dataset, complex rbf kernel
    training time: 0.234 s
    prediction time: 2.544 s
    Accuracy: 0.616040955631

    Reduced dataset & complex rbf kernel, accuracy for different values of C
    C=10    0.616040955631
    C=100   0.616040955631
    C=1000  0.821387940842
    C=10000 0.892491467577
    
    Complete dataset, rbf kernel, C=10000 accuracy
    0.990898748578
    
    Reduced dataset predictions:
    10: 1
    26: 0
    50: 1
    
    No of predictions for Sara(0) and Chris(1): Counter({0: 881, 1: 877})
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from collections import Counter

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#reduce size-at the cost of accuracy
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

#clf = SVC(kernel='linear')
clf = SVC(kernel='rbf', C=10000)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

print "accuracy:", accuracy_score(labels_test, pred)

print "Predictions:"
print "10:", pred[10]
print "26:", pred[26]
print "50:", pred[50]

c = Counter(pred)
print "No of predictions for Chris(1):", c[1]


