import requests
from bs4 import BeautifulSoup
import urllib.request


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

r2 = requests.get(cards_urls[0])
soup = BeautifulSoup(r2.text, 'html.parser')
card = soup.find_all('div', {'class': 'card-image'})
img_urls = []

for card_img in card:
    img_urls.append(card_img.find('a').get('href'))

url_ind = 0
name_ind = 1
for img_url in img_urls:
    r3 = requests.get(img_urls[url_ind])
    soup = BeautifulSoup(r3.text, 'html.parser')
    file_url = soup.find('div', {'id': 'card-image'})
    url_container = file_url.find('img', {'class': 'cardContent'})
    url_ind += 1

    if url_container is None:
        pass
    else:
        print(end='#')
        img = url_container.get('src')
        img_name = f'{name_ind}{(str(img))[-4:]}'
        urllib.request.urlretrieve(img, img_name)
        name_ind += 1


def run():
    print(dates)
    print(titles)
    print(cards_urls)
    print(img_urls)
