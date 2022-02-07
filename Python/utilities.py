#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    
    
############################### STORAGE ############################
## Some useful functions to store and load data

import pickle
def dump(obj,name):
	pickle.dump(obj, open(f'{name}.p', "wb")) 
def load(name):
	return pickle.load(open(f'{name}.p', "rb"))