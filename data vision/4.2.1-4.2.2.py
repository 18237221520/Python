from pyecharts.charts import Pie
import os
import csv
from pyecharts import options as opts
#vote_result = pd.read_csv('./result.csv', encoding='utf-8')
x_data = []
y_data = []
with open('result.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for data in reader:
        x_data.append(data[0])
        y_data.append(data[1])
# 饼图用的数据格式是[(key1,value1),(key2,value2)]，所以先使用 zip函数将二者进行组合
data_pair = [list(z) for z in zip(x_data, y_data)]
# 初始化配置项，内部可设置颜色
(
    Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
    .add(
        # 系列名称，即该饼图的名称
        series_name="感兴趣的领域",
        # 系列数据项，格式为[(key1,value1),(key2,value2)]
        data_pair=data_pair,
        # 通过半径区分数据大小 “radius” 和 “area” 两种，设置rosetype为玫瑰图，否则默认饼图
        # radius：扇区圆心角展现数据的百分比，半径展现数据的大小
        # area：所有扇区圆心角相同，仅通过半径展现数据大小
        rosetype=None,
        # 饼图的半径，设置成默认百分比，相对于容器高宽中较小的一项的一半。没有这一项就是饼图。
        radius=["10%", "35%"],
        # 饼图的圆心，第一项是相对于容器的宽度，第二项是相对于容器的高度
        center=[450, 250],
        # 标签配置项
        label_opts=opts.LabelOpts(is_show=True, position="left"),
    )
    # 全局设置
    .set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(
            # 名字
            title="数据可视化-用户感兴趣领域",
            # 组件距离容器左侧的位置
            pos_left="left",
            # 组件距离容器上方的像素值
            pos_top="20",
            # 设置标题颜色
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            subtitle="以下是读者的投票结果。\n读者对金融、医疗保障、市场业3个领域最感兴趣"
        ),
        # 图例配置项，参数 是否显示图里组件：图例距离左侧70%，并且垂直显示，
        legend_opts=opts.LegendOpts(is_show=True,pos_left="75%",orient="vertical"),
    )
    # 系列设置
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        # 设置标签颜色
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("test.html")
)