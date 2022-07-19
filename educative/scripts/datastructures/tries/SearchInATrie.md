# Search in a Trie

## Search Algorithm
If we want to check whether a word is present in the trie or not, we just need to keep tracing the path in the trie corresponding the characters/letters in the word.

The logic isn't too complex, but there are a few cases we need to take care of.

#### Case 1: None-Existent Word

If we are searching for a word that doesn't exist in the trie and is not a subset of any other, by principle we will find None before the last character of the word can be found.

#### Case 2: Word exists as a Substring

This is the case where our word can be found as a substring of another word, but the isEndWord property for it has been set to False.

In the example below, we are searching for the word be. It is a subset of the already existing word bed, but the e node has not been flagged as the end of a word. Hence, be will not be detected.

#### Case 3: Word Exists

The success case is when there exists a path from the root to the node of the last character and the node is also marked as isEndWord:


The function takes in a string key as an argument and return True if the key is found. Otherwise, it returns False.

Much like the insertion process, None keys aren't allowed and all characters are stored in lowercase.

Beginning from the root, we will traverse the trie and check if the sequence of characters is present. Another thing we need to make sure is that the last character node has the isEndWord flag set to True. Otherwise, we will fall into case2.

### Time Complexity
If the length of the word is h, the worse case time complexity is O(h). In the worst case, we have to look at h consecutive levels of a trie for a character in the key being searched for. The presence or absence of each character from the key in the trie can be determined in O(1) because the size of the alphabet is fixed. Thus, the running time of search in a trie is O(h).