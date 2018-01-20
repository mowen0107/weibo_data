# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180119
    Last modified by: HZT
    Last modified date: 20180120
    Last modified thing: 创建文件
'''
import pandas as pd
import re
import jieba


class ContentFeature():
    def __init__(self):
        self.trainDateDir = "/Users/hzt/lab/data_miming/weibo_data/temp/traindata/"
        self.contentFeatureDir = "/Users/hzt/lab/data_miming/weibo_data/temp/contentfeature/"
        self.washedTrainDataFile = self.trainDateDir + "washedTrainData.txt"
        self.contentFeature_1day = self.contentFeatureDir + "contentfeature_1day.txt"
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

    def getContentFeature(self):
        r = '[’!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~，。？”“‘；：《》【】「」！¥…（）—]+'
        wordDict = {}
        for index in self.trainData.index:
            print("------DEBUG LOG :", index)
            cont = self.trainData.loc[index]['cont']
            reCont = re.sub(r, "", cont)
            cutWordList = jieba.lcut(reCont, cut_all=False)
            for word in cutWordList:
                if wordDict.has_key(word):
                    pass
