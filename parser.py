import requests
from bs4 import BeautifulSoup

URL = "https://tj.sputniknews.ru/archive"
URL_TJ = "https://sputnik-tj.com/news"

page_tj = requests.get(URL_TJ)
soup_tj = BeautifulSoup(page_tj.content, "html.parser")

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

post_tjk = soup_tj.find("a", class_="list__title").text.strip()
url_tj = soup_tj.find("a", class_="list__title", href=True)["href"].strip()
f_url_tj = URL_TJ+url_tj

post = soup.find("a", class_="list__title").text.strip()
url = soup.find("a", class_="list__title", href=True)["href"].strip()
f_url = URL+url
