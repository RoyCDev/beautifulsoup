from . import SoupTest
from ..filter import SoupReplacer

class TestReplacer(SoupTest):
  # milestone 2
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

  # milestone 3
  def test_replace_via_name_xformer(self):
    data = "<div><ul><li><img src=''>Image1</li><li><img src=''>Image2</li></ul></div>"
    li_to_span = lambda tag: "span" if tag.name == "li" else tag.name
    replacer = SoupReplacer(name_xformer=li_to_span)
    soup = self.soup(data, replacer=replacer)

    assert 0 == len(soup.find_all("li"))
    assert 2 == len(soup.find_all("span"))

  def test_attr_xformer_add_attr(self):
    data = "<div><ul><li><img src=''>Image1</li><li><img src=''>Image2</li></ul></div>"
    def add_attr(tag): # add class attr to all tags
      copied_attrs = tag.attrs.copy()
      copied_attrs["class"] = "test"  
      return copied_attrs

    replacer = SoupReplacer(attrs_xformer=add_attr)
    soup = self.soup(data, replacer=replacer)

    all_tags = soup.find_all()
    for tag in all_tags: # all tags should now have a class attr with "test" as the value
      assert "test" == tag.attrs["class"]

  def test_attr_xformer_modify_attr(self):
    data = "<div><ul><li><img src=''>Image1</li><li><img src=''>Image2</li></ul></div>"
    def modify_attr(tag): # if tag has a src attr, modify its value to "test"
      copied_attrs = tag.attrs.copy()
      if copied_attrs.get("src") is not None:
        copied_attrs["src"] = "test"
      return copied_attrs

    replacer = SoupReplacer(attrs_xformer=modify_attr)
    soup = self.soup(data, replacer=replacer)

    all_tags = soup.find_all()
    for tag in all_tags:
      if tag.name == "img": # only imgs have src attr
        assert "test" == tag.attrs["src"]
      else: # those didn't have src attr still wouldn't have one
        assert "src" not in tag.attrs

  def test_replace_via_xformer(self):
    data = "<div><ul><li><img src=''>Image1</li><li><img src=''>Image2</li></ul></div>"
    def li_to_span(tag):
      if tag.name == "li":
        tag.name = "span"

    replacer = SoupReplacer(xformer=li_to_span)
    soup = self.soup(data, replacer=replacer)
    
    assert 0 == len(soup.find_all("li"))
    assert 2 == len(soup.find_all("span"))

  def test_xformer_add_attr(self):
    data = "<div><ul><li><img src=''>Image1</li><li><img src=''>Image2</li></ul></div>"
    def add_attr(tag):
      tag.attrs["class"] = "test"

    replacer = SoupReplacer(xformer=add_attr)
    soup = self.soup(data, replacer=replacer)

    all_tags = soup.find_all()
    for tag in all_tags:
      assert "test" == tag.attrs["class"]

  def test_xformer_modify_attr(self):
      data = "<div><ul><li><img src=''>Image1</li><li><img src=''>Image2</li></ul></div>"
      def modify_attr(tag):
        if tag.attrs.get("src") is not None:
          tag.attrs["src"] = "test"

      replacer = SoupReplacer(xformer=modify_attr)
      soup = self.soup(data, replacer=replacer)

      all_tags = soup.find_all()
      for tag in all_tags:
        if tag.name == "img":
          assert "test" == tag.attrs["src"]
        else:
          assert "src" not in tag.attrs