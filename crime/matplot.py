import pandas as pd
import matplotlib.pyplot as plt
reading = pd.read_csv('css.csv')
plt.figure(figsize=(12,10))
reading.groupby([reading['Primary Type']]).size().sort_values(ascending=True).plot(kind='barh')
plt.title('Number of crimes by type')
plt.ylabel('Crime Type')
plt.xlabel('Number of crimes')
plt.savefig('grap.png')
plt.show()
