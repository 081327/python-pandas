#创建dataframe,用字典的形式，还可以使用columns关键字参数指定列的顺序，通过index关键字参数改变默认的索引值！

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