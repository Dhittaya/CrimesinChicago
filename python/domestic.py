import pandas as pd
import pygal as pg
import numpy as np
from pygal.style import DarkStyle
reading = pd.read_csv('../DATA/css.csv')
pie_chart = pg.Pie(style=DarkStyle)
pie_chart.title = 'Domestic Crime'
dct = {}
data = np.array(reading.groupby('Domestic', as_index = False).count()[['Domestic','Date']]).tolist()
for i in data:
    pie_chart.add(str(i[0]), i[1])
pie_chart.render_to_file('../svg_grap/Domestic.svg')
