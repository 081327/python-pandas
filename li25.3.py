#查看数据集的行
#loc和iloc函数，loc索引只能是正索引，不能为负数，iloc可以用正索引，也可以用负索引

import pandas
df=pandas.read_csv('gapminder.tsv',sep='\t')
#输出第5行的数据
print(df.loc[4])
#这里loc后面两个[]，主要是为了输出二维表形式，如果loc[2]形式，输出的就是一个series形式
print(df.loc[[2,4,5]])
print(df.iloc[-1])