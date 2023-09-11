import requests
from bs4 import BeautifulSoup

i = 1
print("Input nickname: ")
nickname = str(input())
for i in range(119):
    page_url = f"https://pl.grepolis.com/start/hall_of_fame?world_id=pl{i}&action=index"
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content,'html.parser')
    if len(soup.find_all(string=nickname)) != 0:
        print(f"Player {nickname} won pl{i}")