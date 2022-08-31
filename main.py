from requests import get

base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_item ='python'

response = get(f'{base_url}{search_item}')
print(response)
