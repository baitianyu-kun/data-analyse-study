import pandas as pd

df2022=pd.read_csv('2022zhiwei.csv')
df2023=pd.read_csv('2023zhiwei.csv')
df2022=df2022.drop(columns=['详情介绍','部门名称_链接'])
df2023=df2023.drop(columns=['详情介绍','部门名称_链接'])
df2022=df2022[0:10000]
df2023=df2023[0:10000]
df2022.to_csv('./2022repack.csv', index=False, sep=',', encoding='utf_8_sig')
df2023.to_csv('./2023repack.csv', index=False, sep=',', encoding='utf_8_sig')
