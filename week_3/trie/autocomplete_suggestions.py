class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        
        return self._get_suggestions(current, prefix)

    def _get_suggestions(self, current, prefix):
        suggestions = []
        if current.is_end_of_word:
            suggestions.append(prefix)
        for char, child in current.children.items():
            suggestions.extend(self._get_suggestions(child, prefix + char))
        return suggestions

# Example usage
trie = Trie()
words = ["apple", "banana", "application", "apricot", "ball", "bat", "cat"]
for word in words:
    trie.insert(word)

prefix = "ap"
suggestions = trie.search(prefix)
print(f"Suggestions for prefix '{prefix}':")
for suggestion in suggestions:
    print(suggestion)
