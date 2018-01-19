# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180114
    Last modified by: HZT
    Last modified date: 20180115
    Last modified thing: 
'''
import sys
sys.path.append('..')
from userfeature import UserFeature

def main():
    userFeature = UserFeature()
    userFeature.getUserFeature()
    print("------DONE------")

if __name__ == '__main__':
    main()