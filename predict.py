# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180115
    Last modified by: HZT
    Last modified date: 20180115
    Last modified thing: 
'''
import numpy as np
import pandas as pd
import pandas.errors as pderr
import copy
import errno

class Predict():
    def __init__(self):
        self.trainDataFile = "washed_userfeature.txt"
        self.testDataFile = "washed_test_data.txt"