# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:08:10 2021

@author: Gilles
"""

import io
import sys
import argparse
import xml.etree.ElementTree
import random
import re
import os
import yaml
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file1",help="The command to run, typically 'run','plot','test'")
parser.add_argument("file2",help="The command to run, typically 'run','plot','test'")

params = yaml.safe_load(open('C:/Users/Gilles/Documents/GitHub/my_own_dvc_test/params.yaml'))['modify_data']

def compare_data(file_name_init,file_name_mod,params):
    print('Loading data...')
    gain = params['gain']
    data_init = np.loadtxt(file_name_init,delimiter=',')
    data_mod = np.loadtxt(file_name_init,delimiter=',')
    x_init = data_init[0,:]
    y_init = data_init[0,:]
    x_mod = data_mod[0,:]
    y_mod = data_mod[0,:]
    print('Data loaded.')
    print('Adding slope')
    diff = (y_init - y_mod)*gain
    print('data_diff.txt written')
    np.savetxt("data/data_diff.txt",np.transpose(np.array([x_init,diff])),delimiter=',');
    return y_mod

if __name__ == '__main__':
    print('Prog is used as a main')
    myargs = parser.parse_args()
    file_name_init = myargs.file1
    file_name_mod = myargs.file1
    compare_data(file_name_init,file_name_mod)
    print('End of main')