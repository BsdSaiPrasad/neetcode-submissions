# For Design Add and Search Word Data Structure, let L = length of the word.
# addWord(word):
# - TC: O(L)
# - SC: O(L) worst case for new Trie nodes
# search(word):
# - Best/normal case: O(L) if there are no "." wildcards
# - Worst case: O(26^L) if the word is mostly "." and the Trie branches heavily
# - Aux SC: O(L) recursion depth
# Overall Trie storage:
# - O(total characters stored across all words)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True
        
    def search(self, word: str) -> bool:
        
        def dfs(index, node):
            if index == len(word):
                return node.end_of_word
            
            c = word[index]

            if c == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            if c not in node.children:
                return False

            return dfs(index + 1, node.children[c])
        
        return dfs(0, self.root)
