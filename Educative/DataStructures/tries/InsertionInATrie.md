# Insertion in a Trie

## Word Insertion
- The insertion process is fairly simple. For each charcter in the key, we check if it exists at the position we desire. If the character is not present, then we insert the corresponding trie node at the correct index in children. While inserting the last node we also set the value of isEndWord to True.

 There are three primary cases we need to consider during insertion. Let's discuss them now.

#### Case 1: No common prefix
- In this situation, we want to insert a word whose characters are not common with any other
        node path.

- We need to create nodes for all the characters of the word any as there is no common 
        subsequence between any and the.

#### Case 2: Common prefix
- This occurs when a portion of the starting characters of your word already in the trie
        starting from the root node.
- For example, if we want to insert a new word there in the trie which consists of a word their,the path till the already exists. After that we need to insert two nodes for r and e as shown below.

#### Case 3: Word Exists
- This occurs if your word is a substring of another word that already exists in the trie.

- For example, if we weant to insert a word the in the trie which already contains their, the path for the already exists. Therefore, we simple need to set the value of isEndWord to true at e in order to represent the end of the word for the as shown below.

        