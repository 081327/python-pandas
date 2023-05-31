#series的方法
#max取最大值，min最小值，mean取平均值，std取标准差
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


ages=scientists['Age']
print(ages)

print('mean',':',ages.mean())
print('max',':',ages.max())
print('min',':',ages.min())
print('std',':',ages.std())

#对ages降序排列
print(ages.sort_values(ascending=False))

#将ages追加到自身上
print(ages.append(ages))