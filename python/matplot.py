import pandas as pd
import matplotlib.pyplot as plt
reading = pd.read_csv('css.csv')
plt.figure(figsize=(12,10))
reading.groupby([reading['Location Description']]).size().sort_values(ascending=True).plot(kind='barh')
plt.title('Number of crimes by location')
plt.ylabel('Crime Location')
plt.xlabel('Number of crimes')
plt.savefig('grap.png')
plt.show()
