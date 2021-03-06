from nltk.corpus import wordnet


class WordNode:
    def __init__(self, word):
        self.word = word
        self.children = []
        self.parent = None
        self.on_path = False

    def add_parent(self, parentNode):
        if (self not in parentNode.children):
            parentNode.children.append(self)
        self.parent = parentNode

    def add_child(self, childNode):
        childNode.add_parent(self)

    def synonyms(self):
        syns = set()
        for syn in wordnet.synsets(self.word):
            for l in syn.lemmas():
                syns.add(WordNode(l.name()))
        return syns

    def set_found(self):
        self.on_path = True
        self.parent and self.parent.set_found()

    def to_dict(self):
        return {
            'parent': self.parent.word if self.parent else '',
            'name': self.word,
            'on_path': self.on_path,
            'children': [child.to_dict() for child in self.children]
        }
