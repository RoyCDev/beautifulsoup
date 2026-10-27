from bs4 import BeautifulSoup, SoupStrainer
import sys

with open(sys.argv[1], encoding="utf-8") as f:
  links = SoupStrainer("a")
  soup = BeautifulSoup(f, "html.parser", parse_only=links)
  print(soup.prettify())