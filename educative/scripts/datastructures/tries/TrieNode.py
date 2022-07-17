class TrieNode:
    def __init__(self,char=''):
        self.children = [None] * 26 # This will store pointers to the children
        self._is_end_word = False
        self.char = char