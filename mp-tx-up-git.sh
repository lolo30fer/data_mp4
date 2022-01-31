#!/bin/bash
git init
sleep 5
git add -A
sleep 5
git commit -m "tig"
sleep 5
git branch -M main
sleep 5
git remote add origin https://github.com/lolo30fer/data_mp4.git
sleep 5
git push -u origin main