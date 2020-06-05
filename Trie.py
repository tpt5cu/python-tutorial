class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        c = self.root
        for i in word:
            c[i] = c.get(i, {})
            c = c[i]
        c['end'] = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        child = self.root
        for i in word:
            if i in child:
                child = child[i]
            else:
                return False
        if 'end' in child: 
			return True
        return False
            
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        child = self.root
        for i in prefix:
            if i not in child:
                return False
            child = child[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)