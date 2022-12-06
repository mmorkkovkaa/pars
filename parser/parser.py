import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.gadget.kg'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='hit__slide')
    phone_x1 = []

    for item in items:
        phone_x1.append(
            {
                'title': URL + item.find('a').get('href'),
                'title_text': item.find('h6', class_='hit__slide__title').get_text(),
                'image': URL + item.find('div', class_='hit__slide__pic').find('img').get('src'),
            }
        )
    return phone_x1

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        phone_x = []
        for page in range(0, 1):
            html = get_html(f'https://www.gadget.kg/catalog/telefony/xiaomi', params=page)
            phone_x.extend(get_data(html.text))
        return phone_x
    else:
        raise Exception('Error in parser func........')