# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:07:55 2021

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
parser.add_argument("cmd",help="The command to run, typically 'run','plot','test'")

params = yaml.safe_load(open('C:/Users/Gilles/Documents/GitHub/my_own_dvc_test/params.yaml'))['modify_data']

def add_slope(file_name):
    print('Loading data...')
    data = np.loadtxt(file_name,delimiter=',')
    x = data[0,:]
    y = data[0,:]
    print('Data loaded.')
    slope = params['slope']
    print('Adding slope')
    y_mod = y + x*slope
    print('data_slope.txt written')
    np.savetxt("data/data_slope.txt",np.transpose(np.array([x,y])),delimiter=',');
    return y_mod

if __name__ == '__main__':
    print('Prog is used as a main')
    myargs = parser.parse_args()
    file_name = myargs.cmd
    add_slope(file_name)
    print('End of main')