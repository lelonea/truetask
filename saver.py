import urllib.request
from parser import *


for card_url in cards_urls:
    print(card_url.index)
    r2 = requests.get(card_url)
    soup = BeautifulSoup(r2.text, 'html.parser')
    last_page = page_count(soup)

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
            img_name = f'{card_url.index}{name_ind}{(str(img))[-4:]}'
            urllib.request.urlretrieve(img, img_name)
            name_ind += 1


def run():
    print(dates)
    print(titles)
    print(cards_urls)
    print(img_urls)
