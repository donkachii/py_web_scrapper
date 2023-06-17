import requests

URL = "https://books.toscrape.com/"
page = requests.get(URL)

print(page.text)