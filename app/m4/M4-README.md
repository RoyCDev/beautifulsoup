## Technical Brief
With this milestone, we're now able to iterate every node in the soup object without needing to save them into a list first. This is achieved using an iterator where we only load up the node we need to process. Once that's done, it'll load the next node, until we've gone through the entire collection. This saves memory and avoids the potental of exhausting all memory (if we have a large list of nodes)

## Updates I made 
- (bs4/__init__.py, bs4/test/test.soup.py)
- added an __iter__ in BeautifulSoup class that returns self.descendants
- 5 test cases to check it's implemented correctly