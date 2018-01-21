# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180119
    Last modified by: HZT
    Last modified date: 20180120
    Last modified thing: 创建文件
'''
import pandas as pd
import numpy as np
import re
import jieba


class ContentFeature():
    def __init__(self):
        self.trainDateDir = "/Users/hzt/lab/data_miming/weibo_data/temp/traindata/"
        self.contentFeatureDir = "/Users/hzt/lab/data_miming/weibo_data/temp/contentfeature/"
        self.washedTrainDataFile = self.trainDateDir + "washedTrainData.txt"
        self.contentFeature = self.contentFeatureDir + "contentfeature.txt"
        self.trainData = pd.read_csv(
            self.washedTrainDataFile, header=0, sep=',', encoding='utf-8')

    def testJieBa(self):
        ''' 测试jieba的用法
        '''
        r = '[’!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~，。？”“‘；：《》【】「」！¥…（）—]+'
        originStr = "我叫#黄子《韩国》廷#，@hzt"
        reStr = re.sub(r, '', originStr)
        outputList = jieba.lcut(reStr, cut_all=False)
        print("------TEST LOG :", outputList)

    def testDataFrame(self):
        df = pd.DataFrame(columns=('uid', 'mid', 'word'))  # 生成空的pandas表
        df.loc[0] = [1234, 5678, 'hello']
        df.to_csv(
            self.contentFeatureDir + "test.txt",
            sep=',',
            encoding='utf-8',
            index=False)

    def getWordSplit(self):
        ''' 把每条微博里的每个词抽出来，每行是[uid,mid,word]，然后删除重复行
        '''
        df = pd.DataFrame(columns=('uid', 'mid', 'word'))  # 生成空的pandas表
        r = '[’!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~，。？”“‘；：《》【】「」！¥…（）—]+'
        dfIndex = 0
        for index in self.trainData.index:
            if index > 300:
                break
            print("------DEBUG LOG :", index)
            uid = self.trainData.loc[index]['uid']
            mid = self.trainData.loc[index]['mid']
            cont = self.trainData.loc[index]['cont']
            if pd.isnull(cont):
                continue
            reCont = re.sub(r, "", cont)
            cutWordList = jieba.lcut(reCont, cut_all=False)
            for word in cutWordList:
                df.loc[dfIndex] = [uid, mid, word]
                dfIndex += 1
        dfDroped = df.drop_duplicates()  # 删除同一条微博中的重复的词
        dfDroped.to_csv(
            self.contentFeatureDir + "splitedword.txt",
            sep=',',
            index=False,
            encoding='utf-8')
