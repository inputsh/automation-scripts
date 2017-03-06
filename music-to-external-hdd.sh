#!/bin/bash

if [ "$(nmcli -t -f name con show --active | grep '<ESSID NAME>')" = '<ESSID NAME>' ]; then
    echo "Connected to the home network. Proceeding..."
    current_date=$(date +%Y-%m)
    scp -r ~/music/$current_date pi@192.168.X.X:/media/XXXX/music/$current_date
fi
