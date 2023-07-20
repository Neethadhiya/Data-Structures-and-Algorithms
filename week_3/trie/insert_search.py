class TrieNode:
    def __init__(self):
        self.children ={}
        self.end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current = current.children[char]
        current.end_of_word=True
    def search(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current =  current.children[char]
        return current.end_of_word
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")
print(trie.search("banana"))
