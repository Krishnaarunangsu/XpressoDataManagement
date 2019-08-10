import pandas as pd


df1 = pd.read_excel('./data/Excel1.xlsx')
df2 = pd.read_excel('Excel2.xlsx')

mergedStuff = pd.merge(df1, df2, on=['Name'], how='inner')
mergedStuff.head()

df_1 = pd.DataFrame({
'A' : [1.0, 2.0, 3.0, 4.0],
'B' : [100, 200, 300, 400],
'C' : [2, 3, 4, 5]
                   })

df_2 = pd.DataFrame({
'B' : [1.0, 2.0, 3.0, 4.0],
'C' : [100, 200, 300, 400],
'D' : [2, 3, 4, 5]
                  })
