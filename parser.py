import requests
from bs4 import BeautifulSoup


start_url = 'https://3d-galleru.ru/archive/cat/kalendar-42/'
base_url = 'https://3d-galleru.ru/'

r = requests.get(start_url)

soup = BeautifulSoup(r.text, 'html.parser')


dates = []
titles = []
cards_urls = []


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


def run():
    print(dates)
    print(titles)
    print(cards_urls)
