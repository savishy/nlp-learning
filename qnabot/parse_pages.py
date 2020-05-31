from bs4 import BeautifulSoup
import json,requests
with open('config.json','r') as f:
    config = json.load(f)

topic = 'dynatrace'
for page in config[topic]:
    r = requests.get(page)
    soup = BeautifulSoup(r.text,'lxml')
    content_main = soup.find_all('div',class_ = 'content--main')
    if len(content_main == 0):
        print(f'Fetching Content failed for {page}')
        continue
