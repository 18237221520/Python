from pyecharts.charts import Page
from pyecharts import options as opts
from pyecharts.charts import Bar
import os
import csv
page = Page()
filename = "hot-dog-places.csv"
data = []
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for datarow in reader:
        data.append(datarow)
datax = data[0]
datay_A = data[1]
datay_B = data[2]
datay_C = data[3]

# 制作图表
stack_bar = (
    Bar()
    .add_xaxis(datax) # LabelOpts是标记数据的，False去除数值
    .add_yaxis("第一名", datay_A, stack="stack1",label_opts = opts.LabelOpts(is_show=False))
    .add_yaxis("第二名", datay_B, stack="stack1",label_opts = opts.LabelOpts(is_show=False))
    .add_yaxis("第三名", datay_C, stack="stack1",label_opts = opts.LabelOpts(is_show=False))
    # 在系列设置中设置标签属性
    .set_global_opts(title_opts=opts.TitleOpts(title="热狗大胃王比赛", subtitle="副标题"),
                    # LegendOpts是显示图例的，False去除图例
                     legend_opts=opts.LegendOpts(is_show=False))
    # 再次使用可以覆盖标题
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
    .render("c.html")
)

