import pandas as pd
import pygal as pg
import numpy as np
from pygal.style import DarkStyle

crimes = pd.read_csv('C:/Users/Nattarika/Desktop/CrimesinChicago/DATA/css.csv')
lineread = pg.HorizontalBar(style=DarkStyle)
lineread.title = ('Location Description')
all_lo = np.array(crimes.groupby(['Location Description'], as_index=False).count()[['Location Description','Date']]).tolist()
dict_lo = {}
list_count, top_twen, temp, top_twen_lo = [], [], [], []
for i in all_lo:
	dict_lo[i[1]] = i[0]
	list_count.append(i[1])
list_count = sorted(list_count, reverse = True)
for i in range(21):
	top_twen.append(list_count[i])

for i in top_twen:
	temp = [dict_lo[i], i]
	top_twen_lo.append(temp)

for i in top_twen_lo:
	lineread.add(i[0], i[1])

lineread.render_to_file('C:/Users/Nattarika/Desktop/CrimesinChicago/svg_grap/location.svg')
