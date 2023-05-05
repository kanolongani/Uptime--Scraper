import requests
import pandas as pd
from bs4 import BeautifulSoup


url="https://uptimeinstitute.com/uptime-institute-awards/list"
print(url)
data = requests.get(url)

soup = BeautifulSoup(data.content,'html.parser')

all_data=soup.find_all('ul',class_ ="data-list")

# client=all_data.find_all("li",id="company")

arr = []
for d in all_data:
    print(d)
    try:
        arr.append({
            'company':d.find("li",id="company").find('a').text.strip(),
            'location':d.find("li",id="location").text.strip(),
            "certification":d.find("li",id="certification").text.strip(),
            "datacenter":d.find("li",id="company").find('a').text.strip()
        })
    except:
        pass


pd.DataFrame(arr).to_csv("uptime.csv",index=False)
















    














