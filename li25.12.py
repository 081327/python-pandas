#DataFrame的条件过滤

import pandas as pd
scientists=pd.read_csa('scientist.csv')
#输出数据集中Age大于平均值的记录
print(scientists[scientists['Age']>scientists['Age'].mean()])
#只显示行索引为0，1，3的记录
print(scientists.loc[[True,True,False,True]])
#只显示记录索引为1，3，4的记录
print(scientists.iloc[[1,3,4]])
#获取Age大于平均值的所有记录，只显示Name、Age和Occupation三列
print(scientists[['Name','Age','Occupation']][scientists['Age']>scientists['Age'].mean()].head(2))
