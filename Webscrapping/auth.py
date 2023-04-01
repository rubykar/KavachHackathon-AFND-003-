import requests
from bs4 import BeautifulSoup
import csv

urls = [
    {'url': 'https://www.bbc.com/news', 'author': 'BBC News'},
    {'url': 'https://www.news18.com/opinion/', 'author': 'News18 Opinion'}
]

# Open a CSV file in write mode
with open('headlines.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the headers to the CSV file
    csvwriter.writerow(['Source', 'Author', 'Headline'])

    # Iterate over the URLs and scrape the headlines for each one
    for url in urls:
        response = requests.get(url['url'])
        soup = BeautifulSoup(response.content, 'html.parser')

        if url['url'] == 'https://www.bbc.com/news':
            headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        elif url['url'] == 'https://www.news18.com/opinion/':
            headlines = soup.find_all('h4', class_='jsx-3621759782')

        # Write the headlines to the CSV file
        for headline in headlines:
            csvwriter.writerow([url['url'], url['author'], headline.text.strip()])

# Print a message to confirm that the CSV file was created
print('headlines.csv has been created successfully.')
