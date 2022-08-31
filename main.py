from email.mime import base
from re import search
from tkinter import N
from requests import get
from bs4 import BeautifulSoup



base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_item = 'python'

app_info ={
  'maker' : 'sky4564',
  'base_url' : base_url,
  'search_item' : search_item,
}
welcome = ('!! welcome to web data scrapper !! \n' \
            '    maker : ' + app_info['maker'] + '\n'            
            '    base_url : ' + app_info['base_url'] + '\n'            
            '    search_item : ' + app_info['search_item'] + '\n')



response = get(f'{base_url}{search_item}')

if response.status_code == 200:
  print(welcome)
  print(f' ///////////////// this status_code  : {response.status_code}')
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_= 'jobs')
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    for post in job_posts:
      # print(post)
      print('////////////////////////////')
# else:
  # print(f'this error : {response.status_code}')