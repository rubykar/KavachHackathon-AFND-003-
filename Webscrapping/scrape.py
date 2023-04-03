import csv
import requests
from bs4 import BeautifulSoup

# specify the URLs of the 10 news websites
urls = [   'https://www.ndtv.com/', 
'https://www.timesnownews.com/' ,
 'https://www.republicworld.com/' , 
 'https://www.indiatoday.in/', 
   'https://www.abplive.com/',
'https://zeenews.india.com/',
'https://www.thehindu.com/',
'https://www.hindustantimes.com/'
 'https://www.business-standard.com/',
'https://economictimes.indiatimes.com/',
'https://www.news18.com/',
' https://www.indiatvnews.com/',
'https://www.news18.com/',
'https://indianexpress.com/',
'https://www.firstpost.com/',
'https://www.telegraphindia.com/',
' https://www.deccanchronicle.com/']
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
with open('news_headlines.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'Source', 'Status'])
    for i in range(len(headlines)):
        writer.writerow([headlines[i], sources[i], status[i]])

print('CSV file written successfully!')
