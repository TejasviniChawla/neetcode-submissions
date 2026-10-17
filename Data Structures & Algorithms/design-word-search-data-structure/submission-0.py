class Node:
    def __init__(self): 
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word: 
            if letter not in curr.children: 
                curr.children[letter]= Node()
            curr = curr.children[letter]
        curr.isEnd = True 

        

    def search(self, word: str) -> bool:
        def dfs(node, i): 
            #base case

            if i == len(word):
                return node.isEnd

            ch = word[i]

            if ch=='.': 
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            else: 
                if ch not in node.children: 
                    return False
                return dfs(node.children[ch], i+1)

        return dfs(self.root, 0)
        





        
