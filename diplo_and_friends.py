#!/usr/bin/env python
import requests
import sys, os
from bs4 import BeautifulSoup

# Simplepush API key. You can get one by installing the app from https://simplepush.io/.
simple_push_key = "{{ SIX CHARACTER CONSUMER KEY GOES HERE}}"

# Change the URL if you want to download episodes of some other BBC show
r = requests.get('http://www.bbc.co.uk/programmes/b01dmw90/episodes/player')
soup = BeautifulSoup(r.text, 'html.parser')

mydivs = soup.findAll("div", { "class" : "programme programme--radio programme--episode block-link highlight-box--list br-keyline br-blocklink-page br-page-linkhover-onbg015--hover" })

i = 1
for div in mydivs:
    name = div.find('span', {'property' : 'name'})
    link = div['data-pid']
    if i == 1:
        cmd = "echo 'DOWNLOADING: '" + name.text + "'(Diplo & Friends)'"
        os.system(cmd)
    print name.text + ': ' + link
    # cd into a directory and download the files
    cmd = "cd /var/www/data/r3bl/files/Music/Collections/diplo_and_friends && get_iplayer --pid=%s"%(link)
    os.system(cmd)
    if i == 1:
        cmd2 = "curl --data 'key=" + simple_push_key + "&title=" + name.text + "&msg=" + "Downloaded:" + name.text + "(Diplo & Friends)" + "' https://api.simplepush.io/send"
        os.system(cmd2)
    i = i + 1
# Do a re-scan of that folder so that they become available on Nextcloud
cmd3 = "cd /var/www/html && sudo -u www-data php occ files:scan --path='/r3bl/files/Music/Collections/diplo_and_friends'"
os.system(cmd3)
