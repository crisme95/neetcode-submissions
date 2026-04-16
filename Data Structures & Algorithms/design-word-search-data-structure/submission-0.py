class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        if word is None:
            return
        
        node = self.root

        for char in word:
            index = ord(char) - ord('a')

            if not node.children[index]:
                node.children[index] = TrieNode()

            node = node.children[index]
        
        node.isEnd = True
    

    def search(self, word: str) -> bool:
        if word is None:
            return False

        node = self.root

        for i, char in enumerate(word):
            if char == '.':
                return self.findMatch(node, i, word)
            
            index = ord(char) - ord('a')

            if not node.children[index]:
                return False
            
            node = node.children[index]
        
        return node.isEnd
    
    def findMatch(self, node: 'TrieNode', index: int, word: str) -> bool:
        if not node:
            return False
        
        if index == len(word):
            return node.isEnd
        
        char = word[index]

        if char == '.':
            for child in node.children:
                if child:
                    if self.findMatch(child, index + 1, word):
                        return True
        else:
            i = ord(char) - ord('a')

            if not node.children[i]:
                return False
            
            node = node.children[i]

            return self.findMatch(node, index + 1, word)
        
        return False
