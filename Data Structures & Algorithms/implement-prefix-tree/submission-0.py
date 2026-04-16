class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if word is None:
            return
        
        trieNode = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not trieNode.children[index]:
                trieNode.children[index] = TrieNode()

            trieNode = trieNode.children[index]
        
        trieNode.isEnd = True

        

    def search(self, word: str) -> bool:
        if word is None:
            return
        
        trieNode = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not trieNode.children[index]:
                return False
            
            trieNode = trieNode.children[index]

        return trieNode.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        if prefix is None:
            return
        
        trieNode = self.root

        for char in prefix:
            index = ord(char) - ord('a')

            if not trieNode.children[index]:
                return False
            
            trieNode = trieNode.children[index]

        return True
        
        