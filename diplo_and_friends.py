#!/usr/bin/env python
import requests
import sys, os
from bs4 import BeautifulSoup

r = requests.get('http://www.bbc.co.uk/programmes/b01dmw90/episodes/player')
soup = BeautifulSoup(r.text, 'html.parser')

mydivs = soup.findAll("div", { "class" : "programme programme--radio programme--episode block-link highlight-box--list br-keyline br-blocklink-page br-page-linkhover-onbg015--hover" })

for div in mydivs:
    name = div.find('span', {'property' : 'name'})
    link = div['data-pid']
    print name.text + ': ' + link
    cmd = "cd ~/music/BBC_Radio_1 && get_iplayer --pid=%s"%(link)
    os.system(cmd)
