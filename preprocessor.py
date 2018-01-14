# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180113
    Last modified by: HZT
    Last modified date: 20180113
    Last modified thing: 
'''
import pandas as pd
import pandas.errors as pderr
import copy
import errno


class Preprocessor:
    ''' 对数据进行预处理，了解大致情况
    '''

    def __init__(self):
        self.originPath = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/pro3_data/"
        self.outputPath = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/temp/"
        self.originData = self.readOriginTrainData()

    def readOriginTrainData(self):
        ''' 读取训练集文件
        '''
        data = []
        try:
            data = pd.read_csv(
                self.originPath + 'weibo_train_data.txt',
                encoding='utf8',
                names=['luid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'cont'])
            print("length of data:", len(data))
        except OSError as e:
            print("ERROR LOG:", e)
            print("找不到weibo_train_data.txt文件")
            return None
        try:
            data['fcs'] = data['fcs'].astype('int')
            data['ccs'] = data['ccs'].astype('int')
            data['lcs'] = data['lcs'].astype('int')
        except Exception as e:
            data['fcs'] = 0
            data['ccs'] = 0
            data['lcs'] = 0
            print("ERROR LOG:", repr(e))
        return data

    def getUserFeature(self, originData):
        ''' 得到用户特征，包括各项数值的极值、平均值
        '''
        userFeatureList = []
        for line in originData:
            userFeature = {}
            luid = line['luid']
            mid = line['mid']
            time = line['time']
            fcs = line['fcs']
            ccs = line['ccs']
            lcs = line['lcs']
            cont = line['cont']
            userFeature['luid'] = luid
            # userFeature['']

    def getUserDistr(self):
        ''' 获得用户出现的次数
        '''
        originData = copy.deepcopy(self.originData)
        userList = []
        userDistr = []
        for luid in originData['luid']:
            if luid in userList:
                index = userList.index(luid)
                userDistr[index] += 1
            else:
                userList.append(luid)
                userDistr.append(1)
                print(userList.index(luid))
        return [userList, userDistr]
