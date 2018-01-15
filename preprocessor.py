# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180113
    Last modified by: HZT
    Last modified date: 20180114
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
        self.trainDataDir = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/temp/"
        # self.outputPath = "/Users/hzt/lab/data_miming/weibo_data/temp/"
        self.trainDataFile = "washedTrainData.txt"
        self.trainData = self.readTrainData()

    def readTrainData(self):
        ''' 读取训练集文件,返回pandas格式的Dataframe
        '''
        data = None
        filePath = self.trainDataDir + self.trainDataFile
        try:
            data = pd.read_csv(
                filePath,
                encoding='utf8',
                header=0)
            print("------Length of data:", len(data))
        except OSError as e:
            print("------ERROR LOG 打开训练集数据出错:", e)
            print("------找不到" + filePath + "文件")
            return None
        try:
            data['fcs'] = data['fcs'].astype('int')
            data['ccs'] = data['ccs'].astype('int')
            data['lcs'] = data['lcs'].astype('int')
        except Exception as e:
            data['fcs'] = 0
            data['ccs'] = 0
            data['lcs'] = 0
            print("------ERROR LOG 数据类型转换时出错:", e)
        return data

    def getUserFeature(self, trainData):
        ''' 得到用户特征，包括各项数值的极值、平均值
        '''
        userFeatureList = []
        for line in trainData:
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
        originData = copy.deepcopy(self.trainData)
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
