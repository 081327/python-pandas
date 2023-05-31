#series基本操作
import pandas as pd
scientists=pd.DataFrame({
  'Name':['Rosaline Franklin','William Gosset'],
  'Occupation':['Chemist','Statisttician'],
  'Born':['1920-07-25','1876-06-13'],
  'Died':['1958-04-16','1937-10-16'],
  'Age':[37,61]},columns=['Occupation','Born','Died','Age'],
  index=['Rosaline Franklin','William Gosset']
)
print(scientists)

#获取行索引为“Rosaline Franklin”的整行数据
first_row=scientists.loc['Rosaline Franklin']
print(first_row)

print(type(first_row))


#获取列名（Index）!!!
print(first_row.index)
#也是获取列名
print(first_row.keys())

#获取所有值
print(first_row.values)

#获取第一个值，运行结果：Occupation
print(first_row.index[0])