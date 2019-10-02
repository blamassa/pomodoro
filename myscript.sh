#!/bin/bash
cd ~/apps/pomodoro
./pomodoro-cmdln && notify-send 'Fim do pomodoro!' && python3 save_db.py $1
