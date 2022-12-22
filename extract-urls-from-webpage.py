import requests
from bs4 import BeautifulSoup

url = "http://inside.mines.edu/~rammerma/EGGN281/index.htm"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, "html.parser")
links = soup.find_all("a")
urls = [link.get("href") for link in links]
