#!/usr/bin/python
from __future__ import division
import pprint
import matplotlib.pyplot as plt

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
#from tester import dump_classifier_and_data

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

# Remove outliers that were identified in previous iterations
identified_outliers = ["TOTAL", "LAVORATO JOHN J", "MARTIN AMANDA K", "URQUHART JOHN A", "MCCLELLAN GEORGE", "SHANKMAN JEFFREY A", "WHITE JR THOMAS E", "PAI LOU L", "HIRKO JOSEPH"]

for outlier in identified_outliers:
    data_dict.pop(outlier)

# Explore dataset
financial_features = ['poi', 'salary', 'total_payments', 'bonus', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock']
#'email_address',
email_features = ['poi', 'to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']
data_points = len(data_dict)
poi_count = 0
non_poi_count = 0
print "Data points:\t", data_points
print "no of POIs:\t\t", poi_count
print "no of non POIs:\t", non_poi_count
print "POI ratio:\t\t", poi_count/data_points
print "Total features:\t", len(data_dict[data_dict.keys()[0]])
print "Financial features:\t", len(financial_features)
print "Email features:\t", len(email_features)
print ""

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

#Find features with more than 50% of missing values
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
print ""
print "Features with pois with >50% missing values:", significant_poi_values
print ""


### Task 2: Remove outliers
financial_outliers = featureFormat(data_dict, financial_features)
email_outliers = featureFormat(data_dict, email_features)

def outlier_visualization(data, a, b, a_name, b_name, pos):
    plt.subplot(3,3,pos)
    f1 = []
    f2 = []
    y = []
    for point in data:
        f1.append(point[a])
        f2.append(point[b])
        c = 'red' if point[0]==True else 'blue'
        y.append(c)
    plt.scatter(f1, f2, c=y)
    '''    
    for X,Y in zip(f1, f2):
        plt.annotate('{},{}'.format(X,Y), xy=(X,Y), xytext=(-5, 5), ha='right',
                    textcoords='offset points')
    '''
    frame = plt.gca()
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])
    plt.xlabel(a_name)
    plt.ylabel(b_name)
    plt.show()


def visualize_outliers():
    start = 1
    for i in range(2, len(financial_features)):
        outlier_visualization(financial_outliers, 1, i, 'salary', financial_features[i], start)
        start += 1
    start = 10
    '''
    for i in range(2, len(email_features)):
        outlier_visualization(email_outliers, 1, i, 'to_messages', email_features[i], start)
        start += 1
        '''

# Gets the outlier's name
# pp.pprint(get_outlier('to_messages', 15149))
def get_outlier(feature, value):
    for person, features in data_dict.iteritems():
        if features[feature] == value:
            print "Outlier is:", person, features['poi']

visualize_outliers()

pp = pprint.PrettyPrinter(indent=4)

### Extract features and labels from dataset for local testing
#data = featureFormat(my_dataset, features_list, sort_keys = True)
#labels, features = targetFeatureSplit(data)



### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".



features_list = ['poi', 'salary'] # You will need to use more features






