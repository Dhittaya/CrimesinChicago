import pandas as pd
import pygal as pg
reading = pd.read_csv('css.csv')
lineread = pg.HorizontalBar()
lineread.title = ('Location')
dct = {}
for i in reading['Location Description']:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
for j in dct:
    lineread.add(j, dct[j])
lineread.render_to_file('location.svg')