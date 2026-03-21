
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


players_raw = soup.find_all("span", attrs={"data-testid": "set-player-element-participant-name"})


# In[5]:


players_formatted = []


# In[6]:


players = [players_raw[i] for i in range(0, n_players)]



# In[7]:


for player in players_raw: 
    raw_text = player.text.strip()
    
    if raw_text.upper() == "BYE":
        continue
        
    clean_name = raw_text.split('(')[0].strip()
    names = clean_name.split()
    
    if len(names) >= 2:
        first_initial = names[0][0]
        last_name = " ".join(names[1:])
        formatted_name = f"{last_name} {first_initial}."
        players_formatted.append(formatted_name)
    elif len(names) == 1:
        players_formatted.append(names[0])
        
    if len(players_formatted) == n_players:
        break

players_json = json.dumps(players_formatted, ensure_ascii=False)
print(players_json)



