#查看数据集中的列
#如果只是返回一列数据，可以是列表形式（series），也可以是数据集形式（dataframe），如果是返回多列的数据，必须使用df[['abc']]形式
#series相当于python语言中的列表，dataframe相当于一个二维的记录集

import pandas
df=pandas.read_csv('gapminder.tsv',sep='\t')
#获取country列的数据，返回series对象
country_df=df['country']
print(country_df.head(2))
print(country_df.tail(2))

#获取country、continent和year列的数据，返回dataframe对象
subset=df[['country','continent','year']]  #注意：这块有两个[]
print(subset.head(2))
print(subset.tail(2))