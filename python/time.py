import pandas as pd
import pygal
import numpy as np
from pygal.style import DarkStyle

crimes = pd.read_csv('../DATA/css.csv')
date = crimes['Date']
midnight = 0
moring = 0
noon = 0
after = 0
eve = 0
twit = 0
for i in date:
    time = int(i[-5:].replace(":",""))
    if time <= 359:
        midnight += 1
    elif time <= 759:
        moring += 1
    elif time <= 1159:
        noon += 1
    elif time <= 1559:
        after += 1
    elif time <= 1959:
        eve += 1
    elif time <= 2359:
        twit += 1
    print(i)
total = midnight+moring+noon+after+eve+twit
print(midnight+moring+noon+after+eve+twit)
time_midnight = (midnight*100 / total)
time_moring = (moring*100 / total)
time_noon = (noon*100 / total)
time_after = (after*100 / total)
time_eve = (eve*100 / total)
time_twit = (twit*100 / total)

pie_chart = pygal.Pie(style=DarkStyle)
pie_chart.title = 'Crime Frequency'
pie_chart.add("00:00-03:59",int(time_midnight*100)/100)
pie_chart.add("04:00-07:59",int(time_moring*100)/100)
pie_chart.add("08:00-11:59",int(time_noon*100)/100)
pie_chart.add("12:00-15:59",int(time_after*100)/100)
pie_chart.add("16:00-19:59",int(time_eve*100)/100)
pie_chart.add("20:00-23:59",int(time_twit*100)/100)
pie_chart.render_to_file('../svg_grap/pie.svg')
