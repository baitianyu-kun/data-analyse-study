from random import randrange

import pandas as pd
from pyecharts import options as opts
from flask import Flask, render_template
import csv
import codecs
from data.data_func import *
from pyecharts.charts import Bar, ThemeRiver

df = pd.read_csv('../data/bumen22.csv')
df1 = df.groupby('部门名称')
# 转换成每个部门的数量，转换成字典
# {'上海出入境边防检查总站': 6, '上海市邮政管理局': 2, '中国人民银行': 6,
bumen_counts = {key: len(df1.groups[key]) for key in df1.groups.keys()}
# [('税务局', 7154), ('监管局', 530), ('消防', 449),
sorted_result = sorted(bumen_counts.items(), key=lambda item: item[1], reverse=True)
# {'税务局': 7154, '监管局': 530, '消防': 449,
sorted_result_dict = {key: value for (key, value) in sorted_result}
print(sorted_result)
print(sorted_result_dict)
