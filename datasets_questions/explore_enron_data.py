#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

number_total = len(enron_data.items())
number_poi = 0
number_salario_nan = 0
number_email_nan = 0
number_total_payment_nan = 0

for key, value in enron_data.items():
    
    if(value['poi']):
        number_poi = number_poi + 1

    if(str(value['salary']) == 'NaN'):
        number_salario_nan = number_salario_nan + 1
        
    if(str(value['email_address']) == 'NaN'):
        number_email_nan = number_email_nan + 1
    
    if(str(value['total_payments']) == 'NaN'):
        number_total_payment_nan = number_total_payment_nan + 1


print "qde total: ", number_total 
print "qde poi: ", number_poi
print "qde salario informado: ", number_total - number_salario_nan
print "qde email informado: ", number_total - number_email_nan
print "qde total payment NaN", number_total_payment_nan
print "% total payment NaN: ", (number_total_payment_nan / (number_total + 0.0))