# DECOMPILED BY KR1SHNA
# DONT MESS WITH ME
import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('clear')
logo = """
\033[1;32;40mdb   db d88888b d8888b. d888888b 
\033[1;37;40m88   88 88'     88  `8D   `88'   
\033[1;32;40m88ooo88 88ooooo 88   88    88    
\033[1;37;40m88~~~88 88~~~~~ 88   88    88    
\033[1;32;40m88   88 88.     88  .8D   .88.   
\033[1;37;40mYP   YP Y88888P Y8888D' Y888888P  

     \033[41m\033[1;37m Codded by  \033[41m\033[1;37mMr Hedi\x1b[0m
      """

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;32;1m W E L C O M E ....!'
    print ''
    time.sleep(1)
    
    try:
        to = open('/data/data/com.termux/files/usr/bin/.gshsh-cov', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/HackedDok/h/main/lol.txt').text
    if to in r:
        ip()
    else:
        os.system('clear')
        print logo
        print '\tN O T       F O U N D    ....!'
        print '+=========================================+ '
        print '\x1b[1;97m N O T E  : AGAR KESII KO BAR BAR!'
        print '\x1b[1;97m TOKEN PROBLEM HO RAHII HAIN TU'
        print '\x1b[1;97m EK BAR TOKEN LAGO OUR AGAIN'
        print '\x1b[1;97m OUR COMMAND DOBARA RUN KaRO '
        print '\x1b[1;97m           O N E R  : SOMAIL-BRAND '
        print '+=========================================+ '
        print ' \x1b[1;97m Y O U R    T O K E N : ' + to
        raw_input('\x1b[1;92m      E N T E R    ')
        os.system('xdg-open https://wa.me/message/OTSYSP224GB2L1')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tN O T    OK....!'
    print ' \x1b[1;92m Copy and press enter , then select WhatsApp to continue'
    id = uuid.uuid4().hex[:10]
    print ' YOUR TOKEN : ' + id
    print ''
    raw_input(' Press enter to go to WhatsApp ')
    os.system('xdg-open https://chat.whatsapp.com/OTSYSP224GB2L1')
    sav = open('/data/data/com.termux/files/usr/bin/.gshsh-cov', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;97m    E N T E R ')
    reg()


def ip():
    os.system('clear')
    print logo
    print '\tP L E A S E     W A I T...!'
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print ' +==========================+'
    print '\x1b[1;97m YOUR IP: ' + ips
    time.sleep(1)
    print '\x1b[1;97m YOUR COUNTRY: ' + country
    time.sleep(1)
    print '\x1b[1;97m YOUR REGION: ' + regi
    os.system('clear')
    print logo
    print 47 * '-'
    print ' +=========================================+'
    print '\x1b[1;92m[1] \x1b[1;97m | START'
    print ' +========================================+'
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa4 ')
    if ms == '1':
        os.system('rm -rf $HOME/Zbqjab')
        os.system('cd $HOME && git clone https://github.com/ZX3704/Zbqjab && cd Zbqjab && python SOMAIL-BRAND.py')
        os.system('xdg-open https://chat.whatsapp.com/GXMSk7Nz4apE5jhENU8kdI')
    else:
        print ''
        print '\tSELECT VALID OPITION'
        print ''
        menu_s()

if __name__ == '__main__':
    reg()
