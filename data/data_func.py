import pandas as pd


# 不同地区职位数
def zhiweishu_data(df_path):
    df = pd.read_csv(df_path)
    return pd.DataFrame(df['地区'].value_counts())


# 职位类型: 税务局、气象局...
def bumenshu_data(df_path):
    df = pd.read_csv(df_path)
    df1 = df.groupby('部门名称')
    # 转换成每个部门的数量，转换成字典
    # {'上海出入境边防检查总站': 6, '上海市邮政管理局': 2, '中国人民银行': 6,
    bumen_counts = {key: len(df1.groups[key]) for key in df1.groups.keys()}
    # [('税务局', 7154), ('监管局', 530), ('消防', 449),
    sorted_result = sorted(bumen_counts.items(), key=lambda item: item[1], reverse=True)
    # 保留前6个，由于第7个values小于100，所以用这个判断
    sorted_result_shaixuan = [(key, value) for (key, value) in sorted_result if value > 100]
    return sorted_result_shaixuan


def baokaoshu_data(df_path):
    df = pd.read_csv(df_path)
    df1 = df.groupby('地区').agg({'报考人数': sum, '招考人数': sum, '过审人数': sum, '访问人数': sum})
    data1 = [(df1.index.tolist()[i], df1.values.tolist()[i][0]) for i in range(len(df1.index.tolist()))]
    data2 = [(df1.index.tolist()[i], df1.values.tolist()[i][1]) for i in range(len(df1.index.tolist()))]
    data3 = [(df1.index.tolist()[i], df1.values.tolist()[i][2]) for i in range(len(df1.index.tolist()))]
    data4 = [(df1.index.tolist()[i], df1.values.tolist()[i][3]) for i in range(len(df1.index.tolist()))]
    return data1, data2, data3, data4


def jingzhengbi_data(df_path, df_save_path):
    df = pd.read_csv(df_path)
    # 去除竞争比冒号后面的1,方便排序
    df['竞争比'] = [x.split(":")[0] for x in df['竞争比'].values]
    # 转换数据类型再进行排序
    df['竞争比'] = df['竞争比'].astype('float32')
    df1 = df.sort_values(by='竞争比', ascending=False).iloc[0:10]
    df1.to_csv(df_save_path, index=False, sep=',', encoding='utf_8_sig')


def hengzhifang_data(df_path):
    df = pd.read_csv(df_path)
    df1 = df.groupby(['地区', '部门名称'])
    # {('上海', '上海出入境边防检查总站'): 6,...
    gediqubumen_counts = {key: len(df1.groups[key]) for key in df1.groups.keys()}
    sorted_result = sorted(gediqubumen_counts.items(), key=lambda item: item[1], reverse=True)
    # {('山东', '税务局'): 474,...
    sorted_result_dict = {key: value for (key, value) in sorted_result}
    provinces = ['山东', '浙江', '广东', '辽宁', '福建', '湖南', '江苏']
    jus = ['税务局', '监管局', '海关', '消防', '海事局']
    # 将上面两个表组合一下 [(('山东', '税务局'),('山东', '监管局')....
    zuhe = [(x, y) for x in provinces for y in jus]
    # {('山东', '税务局'): 474, ('山东', '监管局'): 37, ('山东', '海关'): 17, ('山东', '公安局'): 19
    # 获取这些结果
    result = {key: sorted_result_dict[key] for key in zuhe}
    shuiwuju = [result[(province, '税务局')] for province in provinces]
    jianguanju = [result[(province, '监管局')] for province in provinces]
    haiguan = [result[(province, '海关')] for province in provinces]
    xiaofang = [result[(province, '消防')] for province in provinces]
    haishiju = [result[(province, '海事局')] for province in provinces]
    return provinces, shuiwuju, jianguanju, haiguan, xiaofang, haishiju


if __name__ == '__main__':
    # jingzhengbi_data('D:\\PycharmProjects\\keshe2\\data\\2023repack.csv',
    #                  'D:\\PycharmProjects\\keshe2\\data\\jingzhengbi23.csv')
    # jingzhengbi_data('D:\\PycharmProjects\\keshe2\\data\\2022repack.csv',
    #                  'D:\\PycharmProjects\\keshe2\\data\\jingzhengbi22.csv')
    hengzhifang_data('D:\\PycharmProjects\\keshe2\\data\\bumen23.csv')
