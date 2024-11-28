import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pystyle import Colors, Colorate, Center
import time

RED = '\033[1;91m'
WHITE = '\033[0m' 
BLUE = '\033[1;34m'

BANNER = """
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

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_banner():
    print("\n" * 3)
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(BANNER)))
    print()
    print(Center.XCenter(f"  Fork By : {RED}Observant{WHITE}"))
    print()

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        print(f" {BLUE}[ {RED}X{BLUE} ]{RED} ERROR -> {WHITE}000x404")
        return None

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    return {urljoin(base_url, link['href']) for link in soup.find_all('a', href=True)}

def web_crawler(start_url, max_depth=10):
    visited = set()
    queue = [(start_url, 0)]

    while queue:
        current_url, current_depth = queue.pop(0)
        
        if current_url in visited or current_depth > max_depth:
            continue
        
        visited.add(current_url)
        clear_screen()
        display_banner()
        print(f" {BLUE}[ {WHITE}${BLUE} ]{WHITE} -> {current_url}")
        
        html = fetch_page(current_url)
        if html:
            links = extract_links(html, current_url)
            queue.extend((link, current_depth + 1) for link in links)

def main():
    os.system("title ♥")
    clear_screen()
    display_banner()
    
    try:
        url = input(f" {BLUE}[ {WHITE}? {BLUE}]{WHITE} Enter URL -> ")
        web_crawler(url)
    except KeyboardInterrupt:
        print(f"\n {BLUE}[ {RED}X{BLUE} ]{RED} Stopped by user!{WHITE}\n")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
