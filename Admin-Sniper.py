import os
from concurrent.futures import ThreadPoolExecutor
from requests import get
import argparse
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Wh='\033[1;37m'
os.system('clear')
print(f'''{Re}

 █████  ██████  ███    ███ ██ ███    ██     ███████ ███    ██ ██ ██████  ███████ ██████  
██   ██ ██   ██ ████  ████ ██ ████   ██     ██      ████   ██ ██ ██   ██ ██      ██   ██ 
███████ ██   ██ ██ ████ ██ ██ ██ ██  ██     ███████ ██ ██  ██ ██ ██████  █████   ██████  
██   ██ ██   ██ ██  ██  ██ ██ ██  ██ ██          ██ ██  ██ ██ ██ ██      ██      ██   ██ 
██   ██ ██████  ██      ██ ██ ██   ████     ███████ ██   ████ ██ ██      ███████ ██   ██ 
                                                                                         
                                                                                         

''')


parser = argparse.ArgumentParser(description='Admin Sniper tool For Find Admin Login In Web Site ')
parser.add_argument('-u', help='Target Url')
args = parser.parse_args()
site = "http://" + args.u
url_file = 'url.txt'

with open(url_file, "r") as file:
    urls = file.read().splitlines()

def check_url(url):
    address = site + "/" + url
    response = get(address)
    if response.status_code == 200:
        print(f'{Gr} [+] Page Found: {address}')
    else:
        print(f"{Re} [-] Not Found: {address} ")

with ThreadPoolExecutor() as executor:
    executor.map(check_url, urls)
