import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')

df = pd.read_csv('/home/blamassa/apps/pomodoro/db.csv', header = None)
df.columns = ['date','project']

fig, ax = plt.subplots()
count_df = df.groupby('date').count()
ax.bar(count_df.index, count_df['project'])

plt.ylabel('Pomodoros')
plt.xlabel('Datas')
plt.title('Sessões Pomodoro por datas')
plt.show()
