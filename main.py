from requests import get
from bs4 import BeautifulSoup

base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_item ='python'



response = get(f'{base_url}{search_item}')

if response.status_code == 200:
  print(f'///////////////// this status_code  : {response.status_code}')
  soup = BeautifulSoup(response.text, "html.parser")
  paringData = soup.find_all('title')
  print(paringData)
else:
  print(f'this error : {response.status_code}')
  