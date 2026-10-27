from bs4 import BeautifulSoup, SoupStrainer
import sys

with open(sys.argv[1], encoding="utf-8") as f:
  ids = SoupStrainer(id=True)
  soup = BeautifulSoup(f, "html.parser", parse_only=ids)
  print(soup.prettify())