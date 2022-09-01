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
            ':::: [maker] : ' + app_info['maker'] + '\n'                  # 제작자 
            ':::: [base_url] : ' + app_info['base_url'] + '\n'            # 작업사이트         
            ':::: [search_item] : ' + app_info['search_item'] + '\n'      # 핵심 키워드        
            '---------------------------------------------------------------------')



response = get(f'{base_url}{search_item}')

if response.status_code == 200:
  print(welcome)
  print(f'app initiating')
  print(f'this status_code  : {response.status_code}')
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_= 'jobs')
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for post in job_posts:
      anchors = post.find_all('a')      
      anchor = anchors[1]
      company, kind, region = anchor.find_all('span', class_= 'company')
      title = anchor.find('span', class_= 'title')
      print(title)
      print(kind)
      print(company.string, kind.string, region.string, title.string)            
      print('////////////////////////////')
      print('fin////////////////////////////')
# else:
  # print(f'this error : {response.status_code}')
  