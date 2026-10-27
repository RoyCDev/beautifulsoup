# use code from local bs4
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bs4 import BeautifulSoup, SoupReplacer

with open(sys.argv[1], encoding="utf-8") as read_f:
  b_to_blockquote = SoupReplacer("th", "blockquote")
  soup = BeautifulSoup(read_f, "html.parser", replacer=b_to_blockquote)

  with open("t6output.html", "w", encoding="utf-8") as output_f:
    output_f.write(soup.prettify())