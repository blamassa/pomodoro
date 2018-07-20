# pomodoro
Scripts that saves each pomodoro session in a csv file and plots the data

I use it together with [this command line pomodoro timer](https://github.com/carlmjohnson/pomodoro) as an alias in .bashrc, so everytime a pomodoro session is completed, the date is appended in a csv file. The `plot_db.py` gathers the data and plots it as a bar chart(number of sessions by date).

I also used notify-send and beep to notify that a session is over. 

My alias:

    `alias pom = pomodoro-cli && /path/to/file/save_db.py`

    `alias pomstat = /path/to/file/plot_db.py `
