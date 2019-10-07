import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')

df = pd.read_csv('/home/blamassa/apps/pomodoro/db.csv', header = None)
df.columns = ['date','project']
df['value'] = [1]*len(df)
df['date'] = [pd.datetime.strptime(i, '%d/%m/%Y').date() for i in df['date']]

fig, ax = plt.subplots()

dff = df.groupby(['date','project'],as_index=False).sum()
pivot_df = dff.pivot(index='date', columns='project',values='value')
pivot_df.loc[:,pivot_df.columns].plot.bar(stacked=True, ax = ax)

plt.ylabel('Pomodoros')
plt.xlabel('Datas')
plt.title('Sessões Pomodoro por datas')
plt.xticks(rotation = 0)
plt.show()
