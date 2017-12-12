import pandas as pd
import pygal as pg
reading = pd.read_csv('css.csv')
pie_chart = pg.Pie()
pie_chart.title = 'Arrest'
dct = {}
for i in reading['Arrest']:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
for j in dct:
    pie_chart.add(j, dct[j])
pie_chart.render_to_file('arrest.svg')
