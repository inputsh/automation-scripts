#!/usr/bin/python3

import requests
import json
import sys, os

#TODO: Speed this script up. It currently takes ~28 seconds to finish.
#TODO: Add Wallabag integration as bonus points.

# Fetches the IDs of top HN stories at the moment.
r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')

simplepush_id = "{{ SIX CHARACTER SIMPLEPUSH ID HERE}}"
hn_id = ""
i = 0
score = 0

# Fetches the details from the first 30 story IDs (since the HN homepage contains 30 stories).
while i < 30:
    hn_id = json.loads(r.text)[i]
    r2 = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(hn_id) + '.json?print=pretty')
    # Gets the score of the ID
    score = json.loads(r2.text)['score']
    # Checks if the score is bigger than 500 and proceeds if it is.
    if score > 500:
        print ("\nHN ID: " + str(hn_id))
        # Open the history file
        with open(".hn-to-simplepush.history", "r+") as history_file:
            # Checks if the ID is already in the notification history.
            line_found = any(str(hn_id) in line for line in history_file)
            print("line_found = " + str(line_found))
            if not line_found:
                # Append the ID to a file so that this ID wouldn't trigger notifications over and over again every time you run the script.
                history_file.write(str(hn_id) + "\n")
                # Send a Simplepush notification
                cmd = "curl --data 'key=" + simplepush_id + "&title=HN500: " + json.loads(r2.text)['title'] + "'" + " --data-urlencode 'msg=" + json.loads(r2.text)['url'] + "' https://api.simplepush.io/send"
                os.system(cmd)
    i = i + 1
