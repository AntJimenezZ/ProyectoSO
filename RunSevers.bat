@echo off
cd Server
start py Server1.py
start py Server2.py
cd.. 
cd video-player
start npm run preview