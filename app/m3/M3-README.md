## Technical Brief
The SoupReplacer class now has an alternative way to replace a tag's name. It takes in a function with the tag as its argument, and returns either the original or an alternative tag name. This is actually more powerful than in previous milestone because we could provide multiple transformation rules at once. 

- For instance, in milestone 2: og_tag = li, alt_tag = span 
  - This defines 1 transformation rule (li -> span) which will be applied during parsing. The soupReplacer can't take another rule. So, other transformation will have to wait until AFTER the parsing

- In milestone 3: fn(tag): if tag.name == "li" return "span", elif tag.name == "a" return "h1"
  - This has 2 rules (li -> span, a -> h1) but can easily be expanded to an arbitrary amount by adding more elif cases. Since these rules are defined in the function the SoupReplacer will take, all are applied DURING parsing

In fact, we're not limited to change only the tag's name. The SoupReplacer class can take a more general function that modifies the tag in place. Since it receives the tag as argument, it can access/modify any of its public field. So, we can do the following simply because we have access to the tag's name and attrs field
- fn(tag) if tag.attrs.get("class") is not None tag.name = "p
  - This defines the rule (all tags that have the class attribute -> p)

- fn(tag) if tag.attrs.get("class") is not None tag.attrs['class'] = "updated"
  - This updates the src attribute only for those already have it 

With this milestone, we're letting the user to have more flexibility on how they want to change the tags. They'll be the ones providing the transformation functions (just like og_tag and alt_tag). From our side, we simply need to execute them and store the modified tags. So, this milestone is a nice addition.

## Updates I made 
- (bs4/__init__.py, bs4/filter.py, bs4/test/test.replacer.py)
- arguments are optional in SoupReplacer (will throw error if it doesn't receive the right set of arguments)
  - milestone 2 way: og_tag, alt_tag, no xformers
  - milestone 3 way: any xformers but no og_tag/ alt_tag
- soup's handle_starttag: if there's a replacer, apply xformers on the newly created tag
- soup's handle_endtag: if there's a replacer, apply xformers on a placerholderTag to get tag.name
- 6 test cases for SoupReplacer