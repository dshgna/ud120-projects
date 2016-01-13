#!/usr/bin/python
from __future__ import division
import pprint
import matplotlib

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
financial_features = ['salary', 'total_payments', 'bonus', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock']
email_features = ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'poi', 'shared_receipt_with_poi']
features_list = ['poi', 'salary'] # You will need to use more features
pp = pprint.PrettyPrinter(indent=4)

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

# Explore dataset
data_points = len(data_dict)
poi_count = 0
non_poi_count = 0
# check for missing values
missing_value_map = { 'bonus': {'count':0, 'poi':0}, 'deferral_payments': {'count':0, 'poi':0},
    'deferred_income': {'count':0, 'poi':0},'director_fees': {'count':0, 'poi':0}, 
    'exercised_stock_options': {'count':0, 'poi':0}, 'total_payments': {'count':0, 'poi':0},
    'expenses': {'count':0, 'poi':0}, 'loan_advances': {'count':0, 'poi':0},
    'long_term_incentive': {'count':0, 'poi':0}, 'restricted_stock_deferred': {'count':0, 'poi':0},
    'other': {'count':0, 'poi':0}, 'restricted_stock': {'count':0, 'poi':0}, 
    'total_stock_value': {'count':0, 'poi':0}, 'salary': {'count':0, 'poi':0}, 
    'email_address': {'count':0, 'poi':0}, 'from_messages': {'count':0, 'poi':0}, 
    'from_poi_to_this_person': {'count':0, 'poi':0}, 'shared_receipt_with_poi': {'count':0, 'poi':0},
    'from_this_person_to_poi': {'count':0, 'poi':0}, 'to_messages': {'count':0, 'poi':0} }


for person, features in data_dict.iteritems():    
    isPoi = False    
    if features['poi'] == True:
        poi_count += 1
        isPoi = True
    else:
        non_poi_count += 1
    for name, value in features.iteritems():         
        if value == 'NaN':
            missing_value_map[name]['count'] += 1
            if isPoi:
                missing_value_map[name]['poi'] += 1


print "Data points:\t", data_points 
print "no of POIs:\t\t", poi_count
print "no of non POIs:\t", non_poi_count
print "POI ratio:\t\t", poi_count/data_points
print "Total features:\t", len(data_dict[data_dict.keys()[0]])
print "Financial features:\t", len(financial_features)
print "Email features:\t", len(email_features)

significant_missing_values = []
significant_poi_values = []

#print "{:<25} {:<20} {:<10}".format('Feature','missing','poi')
for feature, values in missing_value_map.iteritems():
    missing_ratio = values['count']/data_points
    if missing_ratio > 0.5:
        significant_missing_values.append(feature)
    poi_ratio = values['poi']/poi_count
    if poi_ratio > 0.5:
        significant_poi_values.append(feature)
    #print "{:<25} {:<20} {:<10}".format(feature, values['count'], values['poi'])

print "Features with >50% missing values:", significant_missing_values
print "Features with pois with >50% missing values:", significant_poi_values

my_dataset = data_dict

### Task 2: Remove outliers
data_outliers = featureFormat(my_dataset, financial_features)
labels_outliers, features_outliers = targetFeatureSplit(data_outliers)


def outlier_visualization(data):
    for point in data:
        f1 = point[0]
        f2 = point[1]
        matplotlib.pyplot.scatter(f1, f2 )
    
    matplotlib.pyplot.xlabel("Feature 1")
    matplotlib.pyplot.ylabel("Feature 2")
    matplotlib.pyplot.show()



### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)










