# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180114
    Last modified by: HZT
    Last modified date: 20180120
    Last modified thing: 增加rank字段
'''
import pandas as pd


class Washing():
    ''' 对训练集和测试集进行清洗
        校正或者删除错误的行
    '''

    def __init__(self):
        # self.originPath = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/pro3_data/"
        # self.outputPath = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/temp/"
        self.originDir = "/Users/hzt/lab/data_miming/weibo_data/pro3_data/"
        self.trainDataDir = "/Users/hzt/lab/data_miming/weibo_data/temp/traindata/"
        self.testDataDir = "/Users/hzt/lab/data_miming/weibo_data/temp/testdata/"
        self.originTrainDataFile = self.originDir + "weibo_train_data2.txt"
        self.trianDataFile = self.trainDataDir + "weibo_train_data2.txt"
        self.testDataFile = self.testDataDir + "weibo_predict_data.txt"
        self.nosumTrainDataFile = self.trainDataDir + "nosumTrainData.txt"
        self.washedTrainDataFile = self.trainDataDir + "washedTrainData.txt"

    def washTrainData(self):
        ''' 进行训练集的清洗
        '''
        originTrainData = self.readFile(self.originTrainDataFile)
        washedData = []
        for line in originTrainData:
            washedLine = self.replaceTable(line)
            washedData.append(washedLine)
        self.writeFile(self.trianDataFile, washedData)
        self.deleteWrongLines()
        print("------DONE------")

    def washTestData(self):
        ''' 进行测试集的清洗
        '''
        readFilePath = self.originPath + self.testDataFile
        writeFilePath = self.outputPath + self.testDataFile
        originTestData = self.readFile(readFilePath)
        washedData = []
        for line in originTestData:
            washedLine = self.replaceTable(line)
            washedData.append(washedLine)
        self.writeFile(writeFilePath, washedData)
        print("------DONE------")
        pass

    def deleteWrongLines(self):
        ''' 删除无效的行
        '''
        nameList = ['uid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'cont']
        data = pd.read_csv(self.trianDataFile, sep=',', names=nameList)
        for index in data.index:
            # print("------Index:",index,data.loc[index]['fcs'])
            fcs = data.loc[index]['fcs']
            ccs = data.loc[index]['ccs']
            lcs = data.loc[index]['lcs']
            if pd.isnull(fcs) and pd.isnull(ccs) and pd.isnull(lcs):
                print("------NA:", index)
                data.drop(index, axis=0, inplace=True)
        data.to_csv(self.nosumTrainDataFile, index=False, sep=",")

    def addSumRank(self):
        ''' 求出sum并写入文件中
        '''
        filePath = self.nosumTrainDataFile
        newCols = [
            'uid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'sum', 'rank', 'cont'
        ]
        trainData = pd.read_csv(filePath, sep=',', header=0)
        trainData['sum'] = trainData.apply(
            lambda x: x['fcs'] + x['ccs'] + x['lcs'], axis=1)
        trainData['rank'] = trainData.apply(
            lambda x: 1 if x['sum'] < 6 else 2 if x['sum'] < 11 else 3 if x['sum'] < 51 else 4 if x['sum'] < 101 else 5,
            axis=1)
        trainData['fcs'] = trainData['fcs'].astype('int')
        trainData['ccs'] = trainData['ccs'].astype('int')
        trainData['lcs'] = trainData['lcs'].astype('int')
        trainData['sum'] = trainData['sum'].astype('int')
        trainData = trainData.ix[:, newCols]
        trainData.to_csv(self.washedTrainDataFile, index=False, sep=",")

    def readFile(self, filePath):
        ''' 读文件操作，返回一个很大的string
        '''
        originTrainData = None
        originFile = None
        try:
            originFile = open(filePath, 'r', encoding='utf-8')
            originTrainData = originFile.readlines()
        except IOError as e:
            print("------ERROR LOG:", e)
            return None
        finally:
            if originFile is not None:
                originFile.close()
        return originTrainData

    def writeFile(self, filePath, washedData):
        ''' 写文件操作
        '''
        try:
            # w+,进行读写操作，文件不存在就创建，先清空再写
            washedFile = open(filePath, 'w+', encoding='utf-8')
            washedFile.writelines(washedData)
        except IOError as e:
            print("------ERROR LOG:", e)

    def replaceTable(self, string):
        ''' 替换掉'\t',很多行都有这个问题，导致不能正确把各个特征值分开
        '''
        resultStr = string.replace('\t', ',')
        # print("------After replace:\n",resultStr)
        return resultStr

    def washCont(self):
        ''' cont字段可能出现nan
        '''
        inputData = pd.read_csv(
            self.washedTrainDataFile, sep=',', header=0, encoding='utf-8')
        for index in inputData.index:
            cont = inputData.loc[index]['cont']
            if pd.isnull(cont):
                print("------DEBUG LOG FIND NAN :", index)
                inputData.loc[index]['cont'] = ""
        inputData.to_csv(
            self.washedTrainDataFile, sep=",", encoding='utf-8', index=False)
