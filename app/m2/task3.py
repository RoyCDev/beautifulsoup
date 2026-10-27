from bs4 import BeautifulSoup, SoupStrainer
import sys

with open(sys.argv[1], encoding="utf-8") as f:
  all_tags = SoupStrainer()
  soup = BeautifulSoup(f, "html.parser", parse_only=all_tags)
  print(soup.prettify())