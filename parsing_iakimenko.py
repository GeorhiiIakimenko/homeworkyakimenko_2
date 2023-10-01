import requests
from bs4 import BeautifulSoup

URL = "https://uk.wikipedia.org/wiki/Головна_сторінка"

response = requests.get(URL)
response_content = response.content


soup = BeautifulSoup(response_content, 'html.parser')

headers_h1 = soup.find_all('h1')

for header in headers_h1:
    print(header.text)


headers_h2 = soup.find_all('h2')

for header in headers_h2:
    print(header.text)

