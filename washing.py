# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180113
    Last modified by: HZT
    Last modified date: 20180113
    Last modified thing: 
'''


class Washing():
    ''' 对训练集进行清洗和校正
    '''

    def __init__(self):
        self.originPath = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/pro3_data/"
        self.outputPath = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/temp/"
        self.fileName = "weibo_train_data2.txt"

    def run(self):
        ''' 进行清洗的执行函数
        '''
        originTrainData = self.readFile()
        washedData = []
        for line in originTrainData:
            washedLine = self.replaceTable(line)
            washedData.append(washedLine)
        self.writeFile(washedData)
        print("------DONE------")

    def readFile(self):
        ''' 读文件操作，返回一个很大的string
        '''
        originTrainData = None
        try:
            originFile = open(
                self.originPath + self.fileName, 'r', encoding='utf-8')
            originTrainData = originFile.readlines()
        except Exception as e:
            print("------ERROR LOG:", e)
            return None
        finally:
            originFile.close()
        return originTrainData

    def writeFile(self, washedData):
        ''' 写文件操作
        '''
        try:
            # w+,进行读写操作，文件不存在就创建，先清空再写
            washedFile = open(
                self.outputPath + self.fileName, 'w+', encoding='utf-8')
            washedFile.writelines(washedData)
        except Exception as e:
            print("------ERROR LOG:", e)

    def replaceTable(self, string):
        ''' 替换掉'\t',很多行都有这个问题，导致不能正确把各个特征值分开
        '''
        resultStr = string.replace('\t', ',')
        # print("------After replace:\n",resultStr)

        return resultStr