
class Node:
        def __init__(self):
            self.children = {}
            self.end = False
class WordDictionary:

   

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        word = list(word)
        for index, letter in enumerate(word):
            if letter not in cur.children:
                cur.children[letter] = Node()
            cur = cur.children[letter]
        cur.end = True
            
    

    def search(self, word: str) -> bool:
        # cur = self.root
        # word = list(word)

        # for index, letter in enumerate(word):
        #     if letter == ".":

        #     if letter not in cur.children:
        #         return False
        #     else:
        #         if index == (len(word)-1):
        #             return cur.children[letter].end
        #         cur = cur.children[letter]

        def dfs(j,root):
            cur = root
      
            for i in range(j,len(word)):
                letter = word[i]
                if letter == ".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                
                else:
                    if letter not in cur.children:
                        return False
                    print("here", letter, cur.end)
                    cur = cur.children[letter]
            return cur.end

        return dfs(0,self.root)






wordDictionary =  WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
wordDictionary.search("say")
wordDictionary.search("day")
wordDictionary.search(".ay")
wordDictionary.search("b..")
        
        
