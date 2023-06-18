import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("ol", class_="row")

# print(results.prettify())

book_elements = results.find_all("article", class_="product_pod")

for book_element in book_elements:
    title_element = book_element.find("h3")
    print(title_element.text)
    print()