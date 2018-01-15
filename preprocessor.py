# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180113
    Last modified by: HZT
    Last modified date: 20180115
    Last modified thing: 添加用户分布分析
'''
import numpy as np
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
            data = pd.read_csv(filePath, encoding='utf8', header=0)
            print("------Length of data:", len(data))
        except OSError as e:
            print("------ERROR LOG 打开训练集数据出错:", e)
            print("------找不到" + filePath + "文件")
            return None
        return data

    def getUserFeature(self):
        ''' 得到用户特征，包括各项数值的极值、平均值
                luid 用户id
                count 出现的频次
                max_fcs 最大转发量
                min_fcs 最小转发量
                avg_fcs 平均转发量
                max_ccs 最大评论数
                min_ccs 最小评论数
                avg_ccs 平均评论数
                max_lcs 最大赞数
                min_lcs 最小赞数
                avg_lcs 平均赞数
                max_sum 最大互动数
                min_sum 最小互动数
                avg_sum 平均互动数
                above_avg_rate 高于平均值的概率
            并写入userfeature.txt
        '''
        fileName = "userfeature.txt"
        filePath = self.trainDataDir + fileName
        trainData = copy.deepcopy(self.trainData)
        userFeature = trainData['luid'].value_counts()
        userList = userFeature.index
        for user in userList:
            # 筛选出luid相同的行
            subData = trainData.loc[(trainData['luid']==user)]
            max_fcs = subData['fcs'].max()
            min_fcs = subData['fcs'].min()
            avg_fcs = subData['fcs'].mean()
            max_ccs = subData['ccs'].max()
            min_ccs = subData['ccs'].min()
            avg_ccs = subData['ccs'].mean()
            max_lcs = subData['lcs'].max()
            min_lcs = subData['lcs'].min()
            avg_lcs = subData['lcs'].mean()
            break
        # userFeature.to_csv(filePath, header=0, index=True, sep=',')
        return userFeature
