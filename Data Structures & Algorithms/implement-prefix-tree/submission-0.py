class Node: 
    def __init__(self): 
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word: 
            if letter not in curr.children: 
                curr.children[letter]= Node()
            curr = curr.children[letter]
        curr.isEnd = True


    def search(self, word: str) -> bool:
        ithLetter = 0
        curr = self.root
        while ithLetter<len(word) and word[ithLetter] in curr.children:
            
            curr= curr.children[word[ithLetter]]
            ithLetter+=1
        if ithLetter == len(word) and curr.isEnd:
            return True
        return False

        

    def startsWith(self, prefix: str) -> bool:
        word = prefix
        ithLetter = 0
        curr = self.root
        while ithLetter<len(word) and word[ithLetter] in curr.children:
            curr= curr.children[word[ithLetter]]
            ithLetter+=1
        if ithLetter == len(word):
            return True
        return False

        return True
        
        