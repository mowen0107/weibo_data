# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180115
    Last modified by: HZT
    Last modified date: 20180119
    Last modified thing: 完成predict函数,增加test函数
'''
import pandas as pd


class Predict():
    def __init__(self):
        self.userFeatureDir = "/Users/hzt/lab/data_miming/weibo_data/temp/userfeature/"
        self.testDataDir = "/Users/hzt/lab/data_miming/weibo_data/temp/traindata/"
        self.resultDir = "/Users/hzt/lab/data_miming/weibo_data/temp/result/"
        self.userFeatureFile = self.userFeatureDir + "washed_userfeature.txt"
        self.testDataFile = self.testDataDir + "washedTrainData.txt"
        self.resultFile = self.resultDir + "traindata_result.txt"
        self.precisionFile = self.resultDir + "precision.txt"
        self.userFeature = pd.read_csv(
            self.userFeatureFile,
            header=0,
            sep=',',
            index_col=0,
            encoding='utf-8')
        self.testData = pd.read_csv(
            self.testDataFile, header=0, sep=',', encoding='utf-8')

    def test(self):
        test_uid = 'c60533fdb5278412b14379f693f77dd5'
        uid_list = list(self.userFeature.index)
        print(uid_list)
        if test_uid in uid_list:
            print("find it")

    def predict(self):
        ''' 在清洗过后的训练集中查找uid，若存在则进行预测
            若不存在则判断为0
            td前缀表示testdata，uf前缀表示userfeature
        '''
        fcs_list = []
        ccs_list = []
        lcs_list = []
        sum_list = []
        rank_list = []
        testdataIndex = self.testData.index
        uf_uid_list = list(self.userFeature.index)
        for index in testdataIndex:
            td_uid = self.testData.loc[index]['uid']
            print("------DEBUG LOG :", index, td_uid)
            pre_fcs = 0
            pre_ccs = 0
            pre_lcs = 0
            pre_sum = 0
            pre_rank = 1
            if td_uid in uf_uid_list:
                print("------DEBUG LOG FIND:", td_uid)
                subData = self.userFeature.loc[td_uid]
                if subData['avg_fcs'] < 1:
                    pre_fcs = 1
                    # pre_fcs = subData['max_fcs'].astype(int)
                else:
                    pre_fcs = subData['avg_fcs'].astype(int)
                if subData['avg_ccs'] < 1:
                    pre_ccs = 1
                    # pre_ccs = subData['max_ccs'].astype(int)
                else:
                    pre_ccs = subData['avg_ccs'].astype(int)
                if subData['avg_lcs'] < 1:
                    pre_lcs = 1
                    # pre_lcs = subData['max_lcs'].astype(int)
                else:
                    pre_lcs = subData['avg_lcs'].astype(int)
                pre_sum = pre_fcs + pre_ccs + pre_lcs
                if pre_sum < 6:
                    pre_rank = 1
                elif pre_sum < 11:
                    pre_rank = 2
                elif pre_sum < 51:
                    pre_rank = 3
                elif pre_sum < 101:
                    pre_rank = 4
                else:
                    pre_rank = 5
            fcs_list.append(pre_fcs)
            ccs_list.append(pre_ccs)
            lcs_list.append(pre_lcs)
            sum_list.append(pre_sum)
            rank_list.append(pre_rank)
        self.testData['pre_fcs'] = fcs_list
        self.testData['pre_ccs'] = ccs_list
        self.testData['pre_lcs'] = lcs_list
        self.testData['pre_sum'] = sum_list
        self.testData['pre_rank'] = rank_list
        newCols = [
            'uid', 'mid', 'fcs', 'pre_fcs', 'ccs', 'pre_ccs', 'lcs', 'pre_lcs',
            'sum', 'pre_sum', 'rank', 'pre_rank'
        ]
        self.testData = self.testData.ix[:, newCols]
        self.testData.to_csv(
            self.resultFile, index=False, sep=",", encoding='utf-8')

    def getPrecision(self):
        ''' 获得最后的精确度
        '''
        resultData = pd.read_csv(
            self.resultFile, header=0, sep=',', encoding='utf-8')
        rightValue = 0
        totalValue = 0
        rightNumList = [0, 0, 0, 0, 0]
        totalNumList = [0, 0, 0, 0, 0]
        for index in resultData.index:
            print("------DEBUG LOG :", index)
            rank = resultData.loc[index]['rank']
            pre_rank = resultData.loc[index]['pre_rank']
            rankIndex = rank - 1
            totalNumList[rankIndex] += 1  # 这个档位的微博数加1
            if rank == pre_rank:
                rightNumList[rankIndex] += 1  # 如果预测对了，这个档位的预测对微博数加1
        rightValue = rightNumList[0] + rightNumList[1] * 10 + rightNumList[2] * 50 + rightNumList[3] * 100 + rightNumList[4] * 200
        totalValue = totalNumList[0] + totalNumList[1] * 10 + totalNumList[2] * 50 + totalNumList[3] * 100 + totalNumList[4] * 200
        precision = rightValue / totalValue
        print("------准确率为：", precision)
