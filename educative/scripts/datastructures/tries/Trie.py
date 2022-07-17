from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def get_index(self,t):
        return ord(t) - ord('a')

    def insert(self,key):
        if key is None:
            return False
        key = key.lower()
        current = self.root
        
        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)
            
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")
            current = current.children[index]
        current._is_end_word = True
        print("'" + key + "' inserted")
    
    # Function to search a given key in Trie
    def search(self,key):
        return False
    # Function to delete given key from Trie
    def delete(self,key):
        pass

keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

t = Trie()
print("Key to insert:\n", keys)

for words in keys:
    t.insert(words)

"""
The function takes in a string key indicating a word. None keys are not allowed, and all keys
are stored in lowercase.

To make things easier, weuse the get_index() method to return the index of a character. The 
get_index method subtracts the ordinal value of 'a' from the character to return a numerical
value in the range of 0 to 25.

To insert a key, we iterate over the characters in the key. For each character, we check if 
a TrieNode exists for it. If it does not exist, we insert a new TrieNode in the children array
at the index returned by the get_index function. However, if a TrieNode already exists, we simply
move on to the next character by setting our current node to the TrieNode at the chracter's index.

Once we have iterated over all the letters, we mark the last node as leaf since the word has ended.

Time Complexity
    For a key with n characters, the worst case time complexity turns out to be O(N) since we need to make n
    insertions.
"""