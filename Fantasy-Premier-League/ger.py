import pandas as pd

import matplotlib.pyplot as plt


pd.set_option('display.width', 400)

pd.set_option('display.max_columns', 18)

playerName ="Aaron_Cresswell"

df = pd.read_csv(path)
#
# print (df)

points= df['total_points']

years= df['season_name']



# plot

plt.plot(years,points)
plt.title('%s'% playerName)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()


