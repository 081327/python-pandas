#使用read_csv函数装载gapminder.tsv文件，成功装载数据，read_csv函数会返回一个DataFrame对象。
#并输出样本数据的前5行，用head方法，通过columns属性可以获得样本数据的列

import pandas
df=pandas.read_csv('gapminder.tsv',sep='\t')
print(type(df))

print(df.head())
print(df.shape)
print(df.columns)

#对数据集的列进行迭代
for column in df.columns:
    print(column,end=' ')
    