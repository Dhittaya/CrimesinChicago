import pandas as pd
import pygal as pg
import numpy as np
from pygal.style import DarkStyle

crimes = pd.read_csv('C:/Users/USER/Desktop/ming/CrimesinChicago/DATA/css.csv')
lineread = pg.HorizontalBar(style=DarkStyle)
lineread.title = ('Location Description')
dct = {}
print(np.array(crimes.groupby(['Location Description'], as_index=False).count()[['Location Description','Date']]).tolist())
lineread.render_to_file('location.svg')
