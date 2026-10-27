Part 2
BeaitufulSoup() constructor: init.py 209-490
prettify(): element.py 2601-2617
find_all(): element.py 2715-2748
find(): element.py 2684-2713
findParent(): element.py 992-1020
new_tag(): init.py, 682-730
append(): init.py, 2046-2054
SoupStrainer() constructor: filter.py 345-396

Workflow
htmlparser's handle_starttag (name field - holds the record of tag's original name)
- calls soup's handle_starttag (w/ tag's original name)
- soup creates a tag instance (interally, that decides if it should be a self-closing)
- then, change tag.name (that shouldn't affect other properties)
- tag is pushed to tagStack
- soup sends back the tag to htmlparser handle_starttag

- the parser checks tag.is_empty_element (true if it's self closing)
- if so, calls soup's handle_endtag (w/ tag's original name)
- in soup, change the name 1 more time
- tagStack uses the updated name to pop

Updates I made (bs4/__init__.py, bs4/filter.py, bs4/test/test.replacer.py)
- soup's constructor takes a replacer
- soup's handle_starttag: if there's a replacer, change tag.name after a tag instance is created
- soup's handle_endtag: if there's a replacer, change name field before passing that to popToTag
- added a SoupReplacer class
- 2 test cases for SoupReplacer (verify no replaces if no match, and repalces all matched tags)