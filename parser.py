import requests
from bs4 import BeautifulSoup


base_url = 'https://3d-galleru.ru/'
start_url = 'https://3d-galleru.ru/archive/cat/kalendar-42/page-1/'

r = requests.get(start_url)

soup = BeautifulSoup(r.text, 'html.parser')


def page_count(b_soup):
    pages = b_soup.find('div', {'id': 'pages'})
    if pages.text == '':
        last_page_find = 1
    else:
        all_pages = str(pages.text)
        if '123456...' in all_pages:
            last_page_find = all_pages[10:]
        else:
            last_page_find = all_pages[-1]
    return int(last_page_find)


last_page = page_count(soup)
dates = []
titles = []
cards_urls = []


for page_num in range(1, last_page+1):
    url = f'https://3d-galleru.ru/archive/cat/kalendar-42/page-{page_num}'
    r1 = requests.get(url)
    soup = BeautifulSoup(r1.text, 'html.parser')

    card_dates = soup.find_all('p', {'class': 'name'})
    for card_date in enumerate(card_dates):
        if card_date[0] % 2:
            dates.append(card_date[1].text.replace('\ue818', ''))

    titles_list = soup.find_all('strong')
    for title in titles_list:
        titles.append(title.text)

    products = soup.find_all('a', {'class': 'card-image'})
    for product in products:
        url = product.get('href')
        cards_urls.append(url)


