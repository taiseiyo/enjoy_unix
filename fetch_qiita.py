#!/usr/bin/env python3
import requests
from pyfzf.pyfzf import FzfPrompt
from bs4 import BeautifulSoup

url = "https://qiita.com/tags/python"
html = requests.get(url)


soup = BeautifulSoup(html.text, "html.parser")
pair_url_topic = {}

for url in soup.find_all("a", class_="css-eebxa eomqo7a4"):
    pair_url_topic[url.get_text()] = url["href"]

fzf = FzfPrompt()
print(pair_url_topic[fzf.prompt(pair_url_topic)[0]])
