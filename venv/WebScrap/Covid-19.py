import requests
from bs4 import BeautifulSoup
import texttable as tt

# URL domain for scraping date
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# send request to the website to get data, in html.parser format
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

data = [500]

# find all data in url's table
data_iterator = iter(soup.find_all('td'))

# data iterator is the iterator of the table
# This loop will keep repeating until find data available in the iterator
while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text
        data.append((
            country,
            int(confirmed.replace(',', '')),
            int(deaths.replace(',','')),
            continent
        ))

    except StopIteration:
        break

data.sort(key = lambda row:row[1], reverse=True)

table = tt.Texttable()

table.add_row([(None, None, None, None)] + data)

table.set_cols_align(('c', 'c', 'c', 'c'))
table.header((' Country ', ' Number of cases ', ' Deaths ' , ' Continent '))

print(table.draw())