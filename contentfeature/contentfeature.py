# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180119
    Last modified by: HZT
    Last modified date: 20180119
    Last modified thing: 创建文件
'''
import pandas as pd
import jieba


class ContentFeature():
    def __init__(self):
        pass

    def testJieBa(self):
        ''' 测试jieba的用法
        '''
        outputList = jieba.lcut("我叫黄子廷hzt", cut_all=False)
        print("------TEST LOG :", outputList)
