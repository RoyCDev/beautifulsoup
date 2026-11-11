# use code from local bs4
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bs4 import BeautifulSoup, SoupReplacer

def modify_p_class_attr(tag):
  if tag.name != "p":
    return tag.attrs

  copied_attrs = tag.attrs.copy()
  copied_attrs["class"] = "test"
  return copied_attrs

with open(sys.argv[1], encoding="utf-8") as read_f:
  replacer = SoupReplacer(attrs_xformer=modify_p_class_attr)
  soup = BeautifulSoup(read_f, "html.parser", replacer=replacer)
  print(soup.prettify())