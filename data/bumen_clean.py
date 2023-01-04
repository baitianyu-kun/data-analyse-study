import pandas as pd


def clean(df, savepath):
    # 去除竞争比冒号后面的1
    df['竞争比'] = [x.split(":")[0] for x in df['竞争比'].values]
    # 将所有带税务局的都去掉前缀只留下税务局
    df['部门名称'] = [x[-3:] if '税务局' in x else x for x in df['部门名称'].values]
    # 将所有带公安局的都去掉前缀只留下公安局
    df['部门名称'] = [x[-3:] if '公安局' in x else x for x in df['部门名称'].values]
    # 将所有带海事局的都去掉前缀只留下海事局
    df['部门名称'] = [x[-3:] if '海事局' in x else x for x in df['部门名称'].values]
    # 将所有带监管局的都去掉前缀只留下监管局
    df['部门名称'] = [x[-3:] if '监管局' in x else x for x in df['部门名称'].values]
    # 将所有带海关的都去掉前缀只留下海关
    df['部门名称'] = [x[-2:] if '海关' in x else x for x in df['部门名称'].values]
    # 将所有带消防的都去掉前缀只留下消防
    df['部门名称'] = ['消防' if '消防' in x else x for x in df['部门名称'].values]
    df.to_csv(savepath, index=False, sep=',', encoding='utf_8_sig')


filepath22 = r'D:\PycharmProjects\keshe2\data\2022repack.csv'
temp22_save = 'D:\PycharmProjects\keshe2\data\\bumen22.csv'
filepath23 = r'D:\PycharmProjects\keshe2\data\2023repack.csv'
temp23_save = 'D:\PycharmProjects\keshe2\data\\bumen23.csv'

df22 = pd.read_csv(filepath22)
df23 = pd.read_csv(filepath23)

clean(df22, temp22_save)
clean(df23, temp23_save)
