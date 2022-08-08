"""
Word Chaining
Statement:
    Given a list of words, figure out whether the given words can form a circular chain. Assume that a single 
    word can never form a chain.

    Two words be chained togetherif the first's last letter is equal to the second word's first letter.

    Note: Assume that all the words are lower case.

Example:
    Consider the following words: eve,eat,ripe,tear
    These words can form the following chain:
    eve -> eat -> tear -> ripe -> eve
"""

class vertexChain:
    def __init__(self, value, visited):
        self.value = value
        self.visited = visited
        self.adj_vertices = []
        self.in_vertices = []


class graphChain:
    def __init__(self,g):
        self.g = g
    def can_chain_words(self,list_size):
        # TODO: Write - Your Code
        return False
        