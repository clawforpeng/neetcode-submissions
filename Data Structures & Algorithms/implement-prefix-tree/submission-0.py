class Node:
    def __init__(self):
        self.children = {}
        self.isLast = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        chars = deque()
        for c in word:
            chars.append(c)
        
        cur = self.root
        while chars:
            char = chars.popleft()
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        
        cur.isLast = True


    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]

        if cur.isLast:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True