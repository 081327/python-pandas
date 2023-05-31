#对数据集进行分组统计
#使用groupby函数
#mean是计算平均值，nunique函数计算个数
#重置索引reset_index()函数
import pandas
df=pandas.read_csv('gapminder.tsv',sep='\t')

#对预期寿命分组进行统计
print(df.groupby('year')['lifeExp'].mean().head(3))


#多列分组统计
multi_group_var=df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean().head(3)
print(multi_group_var)

#重置索引，让每一行都显示行索引（从0开始）
print(multi_group_var.reset_index())

print(df.groupby('continent')['country'].nunique())