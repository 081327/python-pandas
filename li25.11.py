#series条件过滤
import pandas
scientists=pandas.read_csv('scientists.csv')
ages=scientists['Ages']
#筛选出age大于平均值的数据
print(ages[ages>ages.mean()].head(3))

#筛选出age大于平均值的数据，与前面的筛选方式显示的输出格式不同，注意这点！！！
print((ages>ages.mean()).head(3))


print(type(ages>ages.mean()))

#重要！！直接指定哪行记录不显示，哪行记录显示，True表示显示，False表示不显示
print(ages[[True,True,False,True,False,True,True,False]])