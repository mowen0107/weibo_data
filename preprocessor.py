# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180113
    Last modified by: HZT
    Last modified date: 20180113
    Last modified thing: 
'''
import pandas as pd


class Preprocessor:
    ''' 对数据进行预处理，了解大致情况
    '''
    def __init__(self):
        self.originPath = "./pro3_data/"
        self.outputPath = "./temp/"

    def readOriginTrainData(self):
        ''' 读取训练集文件
        '''
        data = pd.read_csv(
            self.originPath + 'weibo_train_data.txt',
            encoding='utf8',
            sep='\t',
            names=['luid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'cont'])
        print("length of data:", len(data))
        data['fcs'] = data['fcs'].astype('int')
        data['ccs'] = data['ccs'].astype('int')
        data['lcs'] = data['lcs'].astype('int')
        return data

    def getUserFeature(self, originData):
        for line in originData:
            luid = line['luid']
            mid = line['mid']
        pass 