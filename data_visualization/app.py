import json
import random
from random import randrange
from pyecharts import options as opts
from flask import Flask, render_template
import csv
import codecs

from pyecharts.faker import Faker

from data.data_func import *
from pyecharts.charts import Bar, ThemeRiver, Pie, Map

web = Flask(__name__)


# 首页
@web.route('/')
def index():
    return render_template('index.html')


@web.route('/chart1')
def chart1():
    return render_template('chart1.html')


@web.route('/chart2')
def chart2():
    return render_template('chart2.html')


@web.route('/chart3')
def chart3():
    return render_template('chart3.html')


@web.route('/chart4')
def chart4():
    return render_template('chart4.html')


@web.route('/chart5')
def chart5():
    return render_template('chart5.html')


@web.route('/chart6')
def chart6():
    return render_template('chart6.html')


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


def zhiweishu_bar():
    filepath22 = r'D:\PycharmProjects\keshe2\data\2022repack.csv'
    filepath23 = r'D:\PycharmProjects\keshe2\data\2023repack.csv'
    zhiwei22 = zhiweishu_data(filepath22)
    zhiwei23 = zhiweishu_data(filepath23)
    c = (
        Bar()
        .add_xaxis(zhiwei22.index.tolist())
        .add_yaxis("2022职位数", zhiwei22['地区'].tolist())
        .add_yaxis("2023职位数", zhiwei23['地区'].tolist())
        .set_colors(["#3fb1e3", "#6be6c1", "#626c91", "#a0a7e6", "#c4ebad", "#96dee8"])
        .set_global_opts()
    )
    return c


def bumenshu_pie(filepath, is22):
    # filepath22 = r'D:\PycharmProjects\keshe2\data\bumen22.csv'
    # filepath23 = r'D:\PycharmProjects\keshe2\data\bumen23.csv'
    bumen = bumenshu_data(filepath)
    c = (
        Pie(init_opts=opts.InitOpts())
        .add(
            series_name="职位占比",
            data_pair=bumen,
        )
        .set_colors(["#3fb1e3", "#6be6c1", "#626c91", "#a0a7e6", "#c4ebad", "#96dee8"])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="2022部门职位数占比" if is22 == True else "2023部门职位数占比",
                pos_left="center",
                pos_top="20",
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c


def baokaoshu_map(filepath, is22):
    data1, data2, data3, data4 = baokaoshu_data(filepath)
    c = (
        Map()
        .add("报考人数", data1, "china", is_map_symbol_show=False)
        .add("招考人数", data2, "china", is_map_symbol_show=False)
        .add("过审人数", data3, "china", is_map_symbol_show=False)
        .add("访问人数", data4, "china", is_map_symbol_show=False)
        .set_global_opts(
            title_opts=opts.TitleOpts(), visualmap_opts=opts.VisualMapOpts(min_=0,
                                                                           max_=200000,
                                                                           is_piecewise=True))
    )
    return c


def hengzhifang_reversebar(filepath):
    provinces, shuiwuju, jianguanju, haiguan, xiaofang, haishiju = hengzhifang_data(filepath)
    c = (
        Bar()
        .add_xaxis(provinces)
        .add_yaxis("税务局", shuiwuju, stack="stack1")
        .add_yaxis("监管局", jianguanju, stack="stack1")
        .add_yaxis("海关", haiguan, stack="stack1")
        .add_yaxis("消防", xiaofang, stack="stack1")
        .add_yaxis("海事局", haishiju, stack="stack1")
        .set_colors(["#3fb1e3", "#6be6c1", "#626c91", "#a0a7e6", "#c4ebad", "#96dee8"])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts()
    )
    return c


@web.route("/zhiweishu")
def zhiweishu():
    c = zhiweishu_bar()
    return c.dump_options_with_quotes()


@web.route("/bumenshu/22")
def bumenshu22():
    c = bumenshu_pie('D:\\PycharmProjects\\keshe2\\data\\bumen22.csv', True)
    return c.dump_options_with_quotes()


@web.route("/bumenshu/23")
def bumenshu23():
    c = bumenshu_pie('D:\\PycharmProjects\\keshe2\\data\\bumen23.csv', False)
    return c.dump_options_with_quotes()


@web.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


@web.route("/map22")
def baokaoshu22():
    c = baokaoshu_map('D:\\PycharmProjects\\keshe2\\data\\2022repack.csv', is22=True)
    return c.dump_options_with_quotes()


@web.route("/map23")
def baokaoshu23():
    c = baokaoshu_map('D:\\PycharmProjects\\keshe2\\data\\2023repack.csv', is22=False)
    return c.dump_options_with_quotes()


def hengzhifangdata():
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), stack="stack1")
        .add_yaxis("商家B", Faker.values(), stack="stack1")
        .add_yaxis("商家C", Faker.values(), stack="stack1")
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）"))
    )
    print(Faker.choose())
    print(Faker.values())
    return c


@web.route("/hengzhifang/22")
def hengzhifang22():
    c = hengzhifang_reversebar('D:\\PycharmProjects\\keshe2\\data\\bumen22.csv')
    return c.dump_options_with_quotes()


@web.route("/hengzhifang/23")
def hengzhifang23():
    c = hengzhifang_reversebar('D:\\PycharmProjects\\keshe2\\data\\bumen23.csv')
    return c.dump_options_with_quotes()


web.run(debug=True)
