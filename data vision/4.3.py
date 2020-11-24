from pyecharts.charts import Line
import pyecharts.options as opts
from pyecharts.globals import ThemeType
import pandas as pd

year_population_age = pd.read_csv('data/us_population_by_age.csv')

line3 = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(year_population_age['year'].tolist())
    .add_yaxis('5岁以下', year_population_age['year_under5'].tolist(), color='red',
               stack='1')
    .add_yaxis('5岁至19岁', year_population_age['year5_19'].tolist(), color='blue',
               stack='1')
    .add_yaxis('20至44岁', year_population_age['year20_44'].tolist(), color='green',
               stack='1')
    .add_yaxis('45至64岁', year_population_age['year45_64'].tolist(), color='yellow',
              stack='1')
    .add_yaxis('65岁以上', year_population_age['year65above'].tolist(), color='orange',
               stack='1')
    .set_series_opts(areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                     label_opts=opts.LabelOpts(is_show=False),
                     markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max'),
                                                             opts.MarkPointItem(type_='min')],
                                                       symbol='pin'))
    .set_global_opts(title_opts=opts.TitleOpts(title='面积折线图'))
)
line3.render('时空比例折线图.html')