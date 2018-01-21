# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180114
    Last modified by: HZT
    Last modified date: 20180120
    Last modified thing: 增加rank字段
'''
import sys
sys.path.append('..')
from washing import Washing


def main():
    washing = Washing()
    # washing.washTrainData()
    # washing.washTestData()
    # washing.addSumRank()
    washing.washCont()
    print("------DONE------")


if __name__ == '__main__':
    main()