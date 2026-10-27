from . import SoupTest
from ..filter import SoupReplacer

class TestReplacer(SoupTest):
  def test_no_replaces_if_no_match(self):
    data = "<div><ul><li><img src=''>Image1</li><li><img src=''>Image2</li></ul></div>"
    h1_to_ul = SoupReplacer("h1", "ul")
    soup = self.soup(data, replacer=h1_to_ul)

    assert 0 == len(soup.find_all("h1"))
    assert 1 == len(soup.find_all("ul")) # that's the <ul> from data string

  def test_replace_all_matched_tags(self):
    data = "<div><ul><li><img src=''>Image1</li><li><img src=''>Image2</li></ul></div>"
    li_to_span = SoupReplacer("li", "span")
    soup = self.soup(data, replacer=li_to_span)

    assert 0 == len(soup.find_all("li"))
    assert 2 == len(soup.find_all("span"))