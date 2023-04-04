import csv
import requests
from bs4 import BeautifulSoup

# specify the URLs of the 10 news websites
urls = ['https://www.ndtv.com/',
'https://timesofindia.indiatimes.com/',
'https://www.hindustantimes.com/',
'https://indianexpress.com/',
'https://www.news18.com/'
'https://www.abplive.com/',
'https://www.indiatoday.in/',
'https://www.republicworld.com/',
'https://zeenews.india.com/',
'https://www.news18.com/cnn-news18/trending', 'https://www.thehindu.com/',
'https://www.deccanherald.com/',
'https://economictimes.indiatimes.com/',
'https://www.livemint.com/',
'https://www.indiatvnews.com/',
'https://www.newsx.com/',
'https://www.oneindia.com/',
'https://www.outlookindia.com/',
'https://www.timesnownews.com/',
'https://thewire.in/'
'https://www.thestatesman.com/',
'https://www.firstpost.com/',
'https://scroll.in/',
'https://www.india.com/',
'https://www.news24online.com/',
'https://www.dnaindia.com/',
'https://www.tribuneindia.com/',
'https://www.thequint.com/',
'https://www.news9live.com/',
'https://www.newindianexpress.com/']

# create empty lists to store the headlines, sources, and status
headlines = []
sources = []
status = []

# loop through the URLs and scrape the headlines
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for headline in soup.find_all(['h1', 'h2', 'h3']):
        headlines.append(headline.text.strip())
        sources.append(url)
        status.append(True)

# write the headlines, sources, and status to a CSV file
with open('news_update.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'Source', 'Status'])
    for i in range(len(headlines)):
        writer.writerow([headlines[i], sources[i], status[i]])

print('CSV file written successfully!')
