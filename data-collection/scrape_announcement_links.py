from bs4 import BeautifulSoup
import requests
import time

def scrape_page_links(url):

    # Data request
  page = requests.get(url)

    # Check request was succesful
  if page.status_code == 200:
    pass
  else:
    return

    # Make some soup
  soup = BeautifulSoup(page.content, 'html.parser')

    # Find hyperlinks that don't point to a stats/research series
  raw_links = []

  for link in soup.find_all('a'):
    if link.has_attr('href') and link.get('class') != ['series-link']:
      raw_links.append(link['href'])

    # Subset the list of links to just the actual stats and research outputs

  start = raw_links.index('/announcements/search') + 1

  end = (i for i, val in enumerate(raw_links) if val.startswith('?keywords'))
  end = list(end)[0]

  raw_links = raw_links[start:end]

  time.sleep(1)

  return raw_links



def fetch_ma_links(num_pages):

  # Loop the function through all the search pages
  base_url = 'https://gov.wales/announcements/search?keywords=&published_after=&published_before=&page='

  url_list = []

  for num in range(0, num_pages):
    page_url = base_url + str(num)
    url_list.append(scrape_page_links(page_url))

  # Flatten everything into one list
  url_list_flat = [item for sublist in url_list for item in sublist]

  return url_list_flat
