#!/bin/bash
cd ~/apps/pomodoro

# Making sure that the user will choose a project
if [ $1 -eq ""]
then
	# "cut" selects an specific column. Takes two arguments:-d (delimiter) and -f (column index to be selected)
	# Sort just sorts it and uniq prints the unique classes. (if you add -c to uniq it is just as the groupby.count)
	cut -d "," -f 2 db.csv | sort | uniq
else
	./pomodoro-cmdln && kdialog --warningyesno 'Pomodoro is over!!!' --yes-label OK --no-label 'Stop working' --title 'pom' && python3 save_db.py $1
fi
