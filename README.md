# weibo_data
Weibo data prediction

Create date: 20180113

Author: HZT

# 数据清洗
washing.py

训练集中有的行不是用逗号分开的，是用\t分开的，所以要把\t替换成逗号

有的行不是有效行，是混乱的信息，这些行的fcs，ccs，lcs都是NaN，要剔除掉

# 预处理
preprocessor.py

要先对数据集有个大概的认识

有多少条数据

用户有多少人

各项数据的极值是多少，分布大概如何

训练集的sum分布如何

content要怎么从中选取关键词

# 参考资料

http://blog.csdn.net/xieyan0811/article/details/78750611

http://blog.csdn.net/jingyi130705008/article/details/78257350

http://blog.csdn.net/bryan__/article/details/50220229

http://blog.csdn.net/fjssharpsword/article/details/78412803?locationNum=7&fps=1

http://lemondy.github.io/2015/12/01/sina_weibo_big_data_competition/