# Word Connect
A tool to find out if two words are connected via their synonyms. This is a fun and simple way to explore the relationship between two words.

A tree of synonyms is built out from the source word. That tree is then traveresed using breadth-first-search to see if there's a path of synonyms to the target word.

A word's synonyms are found using [wordnet](http://www.nltk.org/howto/wordnet.html)'s `synsets`

```
def synonyms(self):
    syns = set()
    for syn in wordnet.synsets(self.word):
        for l in syn.lemmas():
            syns.add(WordNode(l.name()))
    return syns
```
