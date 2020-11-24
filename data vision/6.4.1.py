from pyecharts.charts import WordCloud
import pandas as pd
import pyecharts.options as opts
from pyecharts.globals import ThemeType
post_data = pd.read_csv('post_data.csv')
post_data2 = post_data.groupby(by=['category']).agg({'views': sum}).reset_index().values
wordcloud = (
    WordCloud(init_opts=opts.InitOpts(theme=ThemeType.DARK, bg_color='white'))
    .add("", post_data2, word_size_range=[20, 100])
)
wordcloud.render("词云图.html")