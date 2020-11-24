from pyecharts import options as opts
import os
import csv
from pyecharts.charts import Pie
from pyecharts.faker import Faker
x_data = []
y_data = []
with open('result.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for data in reader:
        x_data.append(data[0])
        y_data.append(data[1])
# 饼图用的数据格式是[(key1,value1),(key2,value2)]，所以先使用 zip函数将二者进行组合
data_pair = [list(z) for z in zip(x_data, y_data)]
c = (
    Pie()
    .add("", data_pair)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_set_color.html")
)