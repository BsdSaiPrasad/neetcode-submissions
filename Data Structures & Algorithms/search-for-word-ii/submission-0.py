# For Word Search II:
# Let:
# - R = rows
# - C = columns
# - W = number of words
# - L = maximum word length
# Trie construction:
# - TC: O(total characters across all words) ≈ O(W · L)
# - SC: O(total characters across all words)
# Board search:
# - Worst case roughly O(R · C · 4^L)
# - More precisely after the first move, you usually have at most 3 choices because you cannot reuse the previous cell, so often written as O(R · C · 3^L)
# Auxiliary DFS space:
# - O(L) recursion depth
# Including Trie storage:
# - SC: O(W · L + L) → simplified to O(W · L)

# TC: O(WL + RC·3^L)
# SC: O(WL + L) ≈ O(WL)

class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root

            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()

                node = node.children[c]
            
            node.word = word
        
        rows = len(board)
        cols = len(board[0])

        res = []

        def dfs(row, col, node):
            c = board[row][col]

            # current letter is not useful
            if c not in node.children:
                return

            # move inside Trie
            node = node.children[c]

            # complete word found
            if node.word:
                res.append(node.word)
                node.word = None

            # mark visited
            board[row][col] = "#"

            # explore neighbors
            if row > 0:
                dfs(row - 1, col, node)

            if row < rows - 1:
                dfs(row + 1, col, node)

            if col > 0:
                dfs(row, col - 1, node)

            if col < cols - 1:
                dfs(row, col + 1, node)

            # restore
            board[row][col] = c

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return res