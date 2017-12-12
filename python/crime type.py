import pandas as pd
import pygal as pg
from pygal.style import DarkStyle

crimes = pd.read_csv('DATA/css.csv')
lineread = pg.HorizontalBar(style=DarkStyle)
lineread.title = ('Crimes Type')
dct = {}
for i in crimes['Primary Type']:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
print(dct)
for j in dct:
    lineread.add(j, dct[j])
lineread.render_to_file('C:/Users/Nattarika/Desktop/CrimesinChicago/crimemoremore.svg')