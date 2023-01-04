import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

filepath23=r'.\2023repack.csv'
filepath22=r'.\2022repack.csv'

df=pd.read_csv(filepath23)
df2=pd.read_csv(filepath22)
# df11=pd.read_csv(filepath22)
# df22=pd.read_csv(filepath23)
# print(df11.dtypes)
# df11.loc[:,"竞争比"]=df["竞争比"].str.replace(":","")
# df11["竞争比"]
#
# print(df11.head(20))
# df11.loc[:,"竞争比"] = df["竞争比"].str.replace(":","").astype('int32')
#第一个
print('===================================================================================')
print('\n地区职位数:\n')
print('2023不同地区职位数:\n')
print(pd.DataFrame(df['地区'].value_counts()),'\n')
print('2022不同地区职位数:\n')
print(pd.DataFrame(df2['地区'].value_counts()),'\n')
print('===================================================================================')
#第二个
print('岗位报考人数（部分）:\n')
print('2023报考人数最多的5个岗位:\n')
print(pd.DataFrame(df['报考人数']).set_index(df['职位名称'],inplace=False).sort_values(by='报考人数',ascending=False).head(),'\n')
print('2023报考人数最少的5个岗位:\n')
print(pd.DataFrame(df['报考人数']).set_index(df['职位名称'],inplace=False).sort_values(by='报考人数',ascending=False).tail(),'\n')

print('2022报考人数最多的5个岗位:\n')
print(pd.DataFrame(df2['报考人数']).set_index(df2['职位名称'],inplace=False).sort_values(by='报考人数',ascending=False).head(),'\n')
print('2022报考人数最少的5个岗位:\n')
print(pd.DataFrame(df2['报考人数']).set_index(df2['职位名称'],inplace=False).sort_values(by='报考人数',ascending=False).tail())
print('===================================================================================')
#第三个
print('岗位竞争比（部分）:\n')
print('2023岗位竞争最激烈的5个岗位:\n')
print(pd.DataFrame(df['竞争比']).set_index(df['职位名称'],inplace=False).head(),'\n')
print('2023岗位竞争最缓和的5个岗位:\n')
print((pd.DataFrame(df['竞争比']).set_index(df['职位名称'],inplace=False).tail()),'\n')
print('2022岗位竞争最激烈的5个岗位:\n')
print(pd.DataFrame(df2['竞争比']).set_index(df2['职位名称'],inplace=False).head(),'\n')
print('2022岗位竞争最缓和的5个岗位:\n')
print((pd.DataFrame(df2['竞争比']).set_index(df2['职位名称'],inplace=False).tail()),'\n')
print('===================================================================================')
#第四个
print('访问人数（部分）:\n')
print('2023访问人数最多的5个岗位\n')
print(pd.DataFrame(df['访问人数']).set_index(df['职位名称'],inplace=False).sort_values(by='访问人数',ascending=False).head(),'\n')
print('2023访问人数最少的5个岗位\n')
print((pd.DataFrame(df['访问人数']).set_index(df['职位名称'],inplace=False).sort_values(by='访问人数',ascending=False).tail()),'\n')
print('2022访问人数最多的5个岗位\n')
print(pd.DataFrame(df2['访问人数']).set_index(df2['职位名称'],inplace=False).sort_values(by='访问人数',ascending=False).head(),'\n')
print('2022访问人数最少的5个岗位\n')
print((pd.DataFrame(df2['访问人数']).set_index(df2['职位名称'],inplace=False).sort_values(by='访问人数',ascending=False).tail()),'\n')
print('===================================================================================')
#第五个
print('岗位所属部门统计（部分）:\n')
print('2023岗位所属最多部门统计情况\n')
print(pd.DataFrame(df['部门名称'].value_counts()).head(),'\n')
print('2023岗位所属最少部门统计情况\n')
print(pd.DataFrame(df['部门名称'].value_counts()).tail(),'\n')
print('2022岗位所属最多部门统计情况\n')
print(pd.DataFrame(df2['部门名称'].value_counts()).head(),'\n')
print('2022岗位所属最少部门统计情况\n')
print(pd.DataFrame(df2['部门名称'].value_counts()).tail(),'\n')
print('===================================================================================')
#第六个
print('招考人数统计情况（部分）:\n')
print('2023岗位招考人数最多的5个岗位\n')
print(pd.DataFrame(df['招考人数']).set_index(df['职位名称'],inplace=False).sort_values(by='招考人数',ascending=False).head(),'\n')
print('2023岗位招考人数最少的5个岗位\n')
print(pd.DataFrame(df['招考人数']).set_index(df['职位名称'],inplace=False).sort_values(by='招考人数',ascending=False).tail(),'\n')
print('2022岗位招考人数最多的5个岗位\n')
print(pd.DataFrame(df2['招考人数']).set_index(df2['职位名称'],inplace=False).sort_values(by='招考人数',ascending=False).head(),'\n')
print('2022岗位招考人数最少的5个岗位\n')
print(pd.DataFrame(df2['招考人数']).set_index(df2['职位名称'],inplace=False).sort_values(by='招考人数',ascending=False).tail(),'\n')


