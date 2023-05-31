#pandas两个数据类型：series和dataframe
#创建series

import pandas as pd
s1=pd.Series([43,56,65,32])
print(s1)    #注意：输出的形式！！！
s2=pd.Series([43,12.4])
print(s2)
s4=pd.Series([44,23.1,True,'Hello World'])
print(s4)

#改变第一列的索引（默认是数字）   ，主要注意输出形式，这块要注意！！！！
ss=pd.Series(['Bill Gates','微软创始人'],index=['Person','Who'])
print(ss)
