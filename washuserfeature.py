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

class WashUserFeature:
    def __init__(self):
        self.trainDataDir = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/temp/"
        # self.trainDataDir = "/Users/hzt/lab/data_miming/weibo_data/temp/"
        self.inputFilePath = self.trainDataDir + "userfeature.txt"
        self.outputFilePath = self.trainDataDir + "washeduserfeature.txt"
    
    def washUserFeature(self):
        ''' 对得到的用户特征进行清洗
            可以认为互动数为0的用户对结果没有太大影响，直接从中删除
        '''
        pass
