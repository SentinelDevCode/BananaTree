import os
os.system("cls")
os.system("title ♥")
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pystyle import * 

RED = '\033[1;91m'
WHITE = '\033[0m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
GOLD = '\033[0;33m'
PURPLE = '\033[0;35m'

def Opening(): 
    art = """
    ____  ___    _   _____    _   _____     __________  ____________
   / __ )/   |  / | / /   |  / | / /   |   /_  __/ __ \/ ____/ ____/
  / __  / /| | /  |/ / /| | /  |/ / /| |    / / / /_/ / __/ / __/
 / /_/ / ___ |/ /|  / ___ |/ /|  / ___ |   / / / _, _/ /___/ /___
/_____/_/  |_/_/ |_/_/  |_/_/ |_/_/  |_/  /_/ /_/ |_/_____/_____/
"""
    print()
    print()
    print()
    print(Colorate.Horizontal(Colors.red_to_blue, Center.XCenter(art)))
    print()
    print(Center.XCenter(f"  Fork By : {RED}Protected{WHITE}"))
    print()

def Starting():
    url = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} Url > ")
    web_crawler(url)

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f" {PURPLE}[{RED}!{PURPLE}]{PURPLE} >{RED}  ERROR {WHITE}: 404")
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
        print(RED + f" {PURPLE}[{GREEN}!{PURPLE}] > " + WHITE, current_url)
        
        html = fetch_page(current_url)
        if not html:
            continue
        
        links = extract_links(html, current_url)
        for link in links:
            queue.append((link, current_depth + 1))

Opening()
Starting()
