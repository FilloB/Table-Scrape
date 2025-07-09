
from bs4 import BeautifulSoup
import requests 
import csv
import sys
import json


URL = sys.argv[1]
n_players = int(sys.argv[2])


page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


# In[4]:


players_raw = soup.find_all("div", class_="player__name")
players_raw


# In[5]:


players_formatted = []


# In[6]:


players = [players_raw[i] for i in range(0, n_players)]



# In[7]:


for player in players: 
    full_name = player.text.strip()
    names = full_name.split()
    if len(names) >= 2:
        last_name = names[-1]
        first_initial = names[0][0]
        formatted_name = f"{last_name} {first_initial}."
        players_formatted.append(formatted_name)

players_json = json.dumps(players_formatted)
print(players_json)



