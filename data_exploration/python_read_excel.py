import pandas as pd


df = pd.read_excel('File.xlsx', sheetname='Sheet1')

print("Column headings:")
print(df.columns)
print(df['Name'])
