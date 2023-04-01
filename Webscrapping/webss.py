import requests
from bs4 import BeautifulSoup

# url = 'https://www.bbc.com/news'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# headlines = soup.select('.gs-c-promo-heading__title.gel-paragon-bold.nw-o-link-split__text')

# for headline in headlines:
#     print(headline.text.strip())


#urls = ['https://www.bbc.com/news', 'https://www.bbc.com/sport', 'https://www.bbc.com/weather']
#for url in urls:
#    response = requests.get(url)
url = ['https://www.bbc.com/news','https://www.news18.com/']
headlines = []
for i in url:
    response = requests.get(i)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines.extend(soup.find_all('h3', class_='gs-c-promo-heading__title'))

for headline in headlines:
    print(headline.text.strip())
