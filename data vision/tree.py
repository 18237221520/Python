import os
import json
import codecs
from pyecharts import options as opts
import csv
from pyecharts.charts import Tree
with codecs.open(os.path.join("./tree.json"), "r", encoding="utf-8") as f:
        data = csv.reader(f)
c=(
    Tree()
    .add("", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="树图"))
    .render()
)
os.system("树图.html")