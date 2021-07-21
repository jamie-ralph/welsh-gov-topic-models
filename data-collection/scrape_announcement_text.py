def read_wg_html_output(url):

  from bs4 import BeautifulSoup
  import requests
  import time
  import re


  # Request URL
  page = requests.get(url)
  if page.status_code == 200:
    pass
  else:
    print("Request returned an error")


  # Turn into soup
  soup = BeautifulSoup(page.content, 'html.parser')

  # Fetch title of document

  title = soup.find_all('h1')

  title = re.sub('<[^<]+?>', '', str(title)).strip('[]')

  # Fetch important dates

  release_date = []

  for div in soup.find_all('div', {'class': 'row first-published'}):
      for nested_div in div.find_all('div'):
        if nested_div.text[0].isdigit():
          release_date.append(nested_div.text)

  release_date = ' '.join(release_date)

  # Fetch all paragraph text

  summary_text = soup.find_all('div', {'class': 'hero-block__summary'})

  summary_text = summary_text[0].get_text().replace('\n', ' ').encode('ascii', 'ignore').decode('utf-8')



  page_text = soup.find_all('div', {'class': 'container-fluid announcement-item__body'})


  page_text = page_text[0].get_text().replace('\n', ' ').encode('ascii', 'ignore').decode('utf-8')

  all_text = summary_text + ' ' + page_text

  time.sleep(1)

  return title, release_date, all_text
