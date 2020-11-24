from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
import os
import csv
name=[]
x=[]
y=[]
with open('hot-dog-contest-winners.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for data in reader:
        if reader.line_num != 1:
            name.append(data[1])
            x.append(data[0])
            y.append(data[2])
# 制作图表
c = (
    # 定义Bar()柱状图
    Bar()
        # x坐标
        .add_xaxis(x)
        # y坐标
        .add_yaxis("成绩", y)
        # 设置标题
        .set_global_opts(title_opts=opts.TitleOpts(title="1980-2010年美国热狗大胃王比赛", subtitle="副标题"))
        # 渲染网页,输出图表的所有配置项
        .render("1980-2010年美国热狗大胃王比赛.html")
)

