class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True
    def longest_common_prefix(self):
        current = self.root
        common_prefix = ""
        while len(current.children) == 1 and not current.end_of_word:
            for char in current.children:
                common_prefix += char
            current = current.children[char]
           
        return common_prefix
trie =Trie()
trie.insert("apple")
trie.insert("appleication")
trie.insert("app")
print(trie.longest_common_prefix())