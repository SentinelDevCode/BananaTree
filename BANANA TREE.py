import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pystyle import Colors, Colorate, Center
import time
from datetime import datetime

RED = '\033[1;91m'
WHITE = '\033[0m' 
BLUE = '\033[1;34m'
GRAY = '\033[1;90m'

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

forkAM = f"""
                       {BLUE}╭────────────────────────╮
                       │ {WHITE}   Fork By: {RED}Sentinel  {BLUE} │
                       ╰────────────────────────╯{WHITE}   
"""

def get_domain_name(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    return domain.split('.')[-2] if len(domain.split('.')) > 1 else domain

def ensure_log_directory():
    log_dir = "webLog"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return log_dir

def log_url(url, start_url):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    domain = get_domain_name(start_url)
    log_dir = ensure_log_directory()
    log_file_path = os.path.join(log_dir, f"{domain}.log")
    
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] - {url}\n")

def artPrint():
    print("\n" * 3)
    print(Colorate.Vertical(Colors.red_to_white, Center.XCenter(art)))
    print()
    print(Center.XCenter(forkAM))
    print()

def fetch_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f" {BLUE}[ {RED}X{BLUE} ]{RED} ERROR -> {WHITE}404 {GRAY}- Website not found.")
            return None
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        print(f" {BLUE}[ {RED}X{BLUE} ]{RED} ERROR -> {WHITE}Request failed {GRAY}- Invalid URL or other issues.")
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
        log_url(current_url, start_url)
        
        os.system("cls")
        artPrint()
        print(f" {BLUE}[ {WHITE}${BLUE} ]{WHITE} -> {current_url}")
        
        html = fetch_page(current_url)
        if html:
            links = extract_links(html, current_url)
            queue.extend((link, current_depth + 1) for link in links)

def main():
    os.system("title ♥")
    os.system("cls")
    artPrint()
    
    try:
        url = input(f" {BLUE}[ {WHITE}? {BLUE}]{WHITE} Enter URL -> ")
        web_crawler(url)
    except KeyboardInterrupt:
        print(f"\n {BLUE}[ {RED}X{BLUE} ]{RED} Stopped by user!{WHITE}\n")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
