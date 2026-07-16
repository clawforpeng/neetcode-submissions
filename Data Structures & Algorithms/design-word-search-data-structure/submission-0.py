class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        chars = [c for c in word]
        cur = self.root

        for c in chars:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(cur: Optional[Node], partial: str) -> bool:
            if not cur:
                return False
            
            if not partial and cur.isEnd:
                return True
            if not partial and not cur.isEnd:
                return False
            
            char = partial[0]

            if char in cur.children:
                if len(partial) > 1:
                    return dfs(cur.children[char], partial[1:])
                else:
                    return dfs(cur.children[char], "")
            elif char == ".":
                for node in cur.children.values():
                    if len(partial) > 1 and dfs(node, partial[1:]):
                        return True
                    elif len(partial) == 1 and dfs(node, ""):
                        return True
            return False

        return dfs(cur, word)


class Node:
    def __init__(self):
        self.isEnd = False
        self.children = {}