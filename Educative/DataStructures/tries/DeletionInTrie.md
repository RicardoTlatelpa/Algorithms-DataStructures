# Deletion in Trie


## Deleting a Word in a Trie

While deleting a node, we need to make sure that the node that we are trying to delete does not have any furhter children branches. If there are no branches, then we can easily remove the node.

However, if the node contains child branches, this opens up a few scenarios which we will cover below.

#### Case 1: Word with No Suffix or Prefix
If the word to be deleted has no suffix or prefix and all the character nodes of this word do no have any other children, then we will delete all these nodes up to the root.

However, if any of these nodes have other children (are part of another branch), then they will not be deleted. This will be explained further in Case 2.

In the figure below, the deletion of the word bat would mean that we have to delete all characters of bat.


#### Case 2: Word is a Prefix

If the word to be deleted is a prefix of some other word, then the value of is_end_word of the last node of that word is set to False and no node is deleted.

For example, to delete the word the, we will simply unmark e to show that the word doesn't exist anymore.

#### Case 3: Word Has a Common prefix

If the word to be deleted has a common prefix and the last node of that word does not have any children, then this node is deleted along with all the parent nodes in the branch which do not have any other children and are not end characters.

Take a look at the figure below. In order to delete their, we'll traverse the common path up to the and delete the characters i and r.


The delete function takes in a key of type string and then checks if either the trie is empty or the key is None. For each case, it simply returns from the function.

delete_helper() is a recursive function to delete the given key. Its arguments are a key, the key's length, a trie node(root at the beginning), and the level (index) of the key.

It goes through all the cases explained above. The base case for this recursive function is when the algorithm reaches the last node of the key:
``` if level is length:``` 

At this point, we check if the last node has any further children or not. If it does, then we simply unmark it as an end word. On the other hand, if the last node doesn't contain any children, all we have to do is to set the parameter deleted_self to True to mark this node for deletion.

## Time Complexity
if the length of the word is h, the worst-case time complexity is O(h). In the worst case, we have to look at h consecutive levels of a trie for a character in the key being searched for. The presence or absence of each character from the key in the trie can be determined in O(1) because the size of the alphabet is fixed. Subsequently, in the worst case, we may have to dlete h nodes from the trie. Thus, the running time of delete in a trie is O(h).