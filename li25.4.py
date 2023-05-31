#查看数据集单元格中的数据
#loc和iloc都能实现这个功能，就是使用iloc函数列要使用索引

import pandas
df=pandas.read_csv('gapminder.tsv',sep='\t')
#获取year和pop列的所有数据
subset=df.loc[:,['year','pop']]
print(subset.head(2))
#获取列索引为2，4，-1（最后一行）的列的所有数据
subset=df.iloc[:,[2,4,-1]]
print(subset.head(2))
#获取列索引为3，4，5的列的所有数据
subset=df.iloc[:,3:6]
print(subset.head(2))
#获取行索引为0.1.2，列索引为3，4，5的数据
subset=df.iloc[0:3,3:6]
print(subset)
#获取行索引为1 ，列名为lifeExp的列的数据
subset=df.loc[1,'lifeExp']
print(subset)

