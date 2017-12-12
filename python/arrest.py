import pandas as pd
import pygal as pg
import numpy as np
from pygal.style import DarkStyle
reading = pd.read_csv('C:/Users/Nattarika/Desktop/CrimesinChicago/DATA/css.csv')
pie_chart = pg.Pie(style=DarkStyle)
pie_chart.title = 'Arrest'
dct = {}
data = np.array(reading.groupby('Arrest', as_index = False).count()[['Arrest','Date']]).tolist()
for i in data:
    pie_chart.add(str(i[0]), i[1])
pie_chart.render_to_file('C:/Users/Nattarika/Desktop/CrimesinChicago/svg_grap/arrest.svg')
