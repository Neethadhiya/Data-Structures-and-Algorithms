class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
    def search(self,word):
        current =self.root
        while current:
            for char in word:
                if char not in self.children:
                    return False
            current = current.children[char]
        return current.end_of_word
