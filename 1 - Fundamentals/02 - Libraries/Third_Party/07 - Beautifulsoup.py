"""
BEAUTIFULSOUP — Third-Party Library

BeautifulSoup is used 5.1 - For:
- web scraping
- HTML parsing
- extracting elements from pages
"""

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------
# BASIC SCRAPING
# ---------------------------------------------------------

url = "https://example.com"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

# ---------------------------------------------------------
# EXTRACT TITLE
# ---------------------------------------------------------

print(soup.title.string)

# ---------------------------------------------------------
# FIND ALL LINKS
# ---------------------------------------------------------

links = soup.find_all("a")
for link in links:
    print(link.get("href"))
