from bs4 import BeautifulSoup
import requests

def scrape_data(page):
    url = 'https://books.toscrape.com/'

    books = []

    for i in range(1,page):
        url2 = f'https://books.toscrape.com/catalogue/page-{i}.html'
        response = requests.get(url2)
        soup = BeautifulSoup(response.text,'html.parser')
        articles = soup.find_all('article', class_= 'product_pod')
    
        for article in articles:
            title = article.find('h3').find('a')['title']
            price = article.find('p', class_='price_color').text
            rating = article.p['class'][1]
            status_stok = article.find('p', class_= 'instock availability').text
            link = url + 'catalogue/' + article.find('h3').find('a')['href']
            books.append({
                        'Title' : title,
                        'Price' : price,
                        'Rating' :rating,
                        'Status Stok' : status_stok,
                        'Link' : link
                    })

    return books