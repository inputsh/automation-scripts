#!/bin/bash

current_date=$(date +%Y-%m)
mkdir -p ~/music/$current_date

cd ~/dnlds
mv *.mp3 *.wav *.flac *.m4a ~/music/$current_date
