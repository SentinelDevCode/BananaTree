import os
os.system("cls")
os.system("title ♥")
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pystyle import * 
import time 

RED = '\033[1;91m'
WHITE = '\033[0m'
BLUE = '\033[1;34m'

art = """
 ▄▄▄▄    ▄▄▄       ███▄    █  ▄▄▄       ███▄    █  ▄▄▄         ▄▄▄█████▓ ██▀███  ▓█████ ▓█████ 
▓█████▄ ▒████▄     ██ ▀█   █ ▒████▄     ██ ▀█   █ ▒████▄       ▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀ 
▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄     ▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   ▒███   
▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██    ░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄ 
░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒     ▒██▒ ░ ░██▓ ▒██▒░▒████▒░▒████▒
░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░     ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░
▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░       ░      ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░
 ░    ░   ░   ▒      ░   ░ ░   ░   ▒      ░   ░ ░   ░   ▒        ░        ░░   ░    ░      ░   
 ░            ░  ░         ░       ░  ░         ░       ░  ░               ░        ░  ░   ░  ░
      ░  
"""

def Starting():
    try:
        url = input(f" {BLUE}[ {WHITE}? {BLUE}]{WHITE} Enter URL -> ")
        web_crawler(url)
    except KeyboardInterrupt:
        time.sleep(0.5)
        print()
        print(f" {BLUE}[ {RED}X{BLUE} ]{RED} Stopped by user!{WHITE}")
        print()
        time.sleep(0.5)
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f" {BLUE}[ {RED}X{BLUE} ]{RED} ERROR -> {WHITE}000x404")
        return None

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for link in soup.find_all('a', href=True):
        absolute_url = urljoin(base_url, link['href'])
        links.add(absolute_url)
    return links

def web_crawler(start_url, max_depth=10):
    visited = set()
    queue = [(start_url, 0)]

    while queue:
        current_url, current_depth = queue.pop(0)
        
        if current_url in visited or current_depth > max_depth:
            continue
        
        visited.add(current_url)
        os.system("cls")
        print()
        print()
        print()
        print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(art)))
        print()
        print(Center.XCenter(f"  Fork By : {RED}Protected{WHITE}"))
        print()
        print(RED + f" {BLUE}[ {WHITE}${BLUE} ]{WHITE} ->" + WHITE, current_url)
        
        html = fetch_page(current_url)
        if not html:
            continue
        
        links = extract_links(html, current_url)
        for link in links:
            queue.append((link, current_depth + 1))

print()
print()
print()
print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(art)))
print()
print(Center.XCenter(f"  Fork By : {RED}Protected{WHITE}"))
print()
Starting()
