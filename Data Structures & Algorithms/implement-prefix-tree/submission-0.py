# For Trie operations, if the word/prefix length is L:
# - insert() → TC: O(L)
# - search() → TC: O(L)
# - startsWith() → TC: O(L)
# Space:
# - Each new inserted word can create up to L new Trie nodes → O(L) extra space for that insertion.
# - Overall Trie space is O(total number of stored characters).

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True


    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        