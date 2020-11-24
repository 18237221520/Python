from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd
import csv
import os
label = []
support = []
oppose = []
noissue = []
'''
with open('rate.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for data in reader:
        if reader.line_num!=1:
            label.append(data[0])
            support.append(data[1])
            oppose.append(data[2])
            noissue.append(data[3])
stack_bar = (
    Bar()
    .add_xaxis(label)
    .add_yaxis("支持", support,stack="stack1")
    .add_yaxis("反对", oppose,stack="stack1")
    .add_yaxis("不发表意见", noissue,stack="stack1")
    # 在系列设置中设置标签属性
    .set_global_opts(title_opts=opts.TitleOpts(title="柱形图数据堆叠示例"),
                     legend_opts=opts.LegendOpts(is_show=True))
    .render('rate.html')
)
# 打开网页
os.system("rate.html")
'''
issue=[]
i=0
list_support = ['支持','反对','不发表意见']
with open('rate.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for data in reader:
        if reader.line_num!=1:
            (
            Bar()
            .add_xaxis(list_support)
            .add_yaxis(issue.append(data),stack="stack1")

            )
Bar.render('投票总体支持于反对情况.html')


