import requests
from bs4 import BeautifulSoup

def recommend_products(keywords):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    url = f"https://www.amazon.com/s?k={keywords}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for item in soup.select('.s-result-item'):
        title = item.select_one('h2 a span')
        link = item.select_one('h2 a')

        if title and link:
            product = {
                'title': title.get_text(),
                'url': 'https://www.amazon.com' + link['href']
            }
            products.append(product)
        
        if title:
            products.append(title.get_text())

    return products