import matplotlib.pyplot as plt
import numpy as np

f = open('/home/blamassa/apps/pomodoro-database/db.csv')
data = f.read()
f.close()

data = data.split('\n')
data.pop()

x_list = []
y_list = []
for i in data:
      if i not in x_list:
          x_list.append(i)
          y_list.append(data.count(i))
print(x_list)

x = np.arange(len(y_list))
fig, ax = plt.subplots()
plt.bar(x, y_list)
plt.xticks(x,x_list)
plt.ylabel('Pomodoros')
plt.xlabel('Datas')
plt.title('Sessões Pomodoro por datas')

plt.show()
