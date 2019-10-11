import matplotlib.pyplot as plt
from matplotlib import dates
import pandas as pd
import datetime

plt.style.use('ggplot')

df = pd.read_csv('/home/blamassa/apps/pomodoro/db.csv', header = None)
df.columns = ['date','project']
df['value'] = [1]*len(df)
df['date'] = [pd.datetime.strptime(i, '%d/%m/%Y').date() for i in df['date']]

dff = df.groupby(['date','project'],as_index=False).sum()
pivot_df = dff.pivot(index='date', columns='project',values='value')

### Plotting data
fig, ax = plt.subplots(figsize = (20,10))

pivot_df.loc[:,pivot_df.columns].plot.bar(stacked=True, ax = ax)
# I want to plot all days until today. For this, I first need to know the number of days since the begining of the count.
diff_days = (datetime.date.today() - pivot_df.index[0]).days
datelist = [str(i)[:10] for i in pd.date_range(start = pivot_df.index[0], periods = diff_days)]
plt.xticks(ticks = range(diff_days), labels = datelist)

plt.ylabel('Pomodoros')
plt.xlabel('Datas')
plt.title('Sessões Pomodoro por datas')
plt.xticks(rotation = 0)
plt.show()
