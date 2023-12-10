'''
5.13 Sample online data
This problem is motivated by the design of a packet sniffer
that provides a uniform sample of packets for a network
session.

Design a program that takes as input a size k, and reads 
packets, continuosly maintaining a uniform random subset
of size k of the read packets.

Hint: Suppose you have a procedure which selects k packets
from the first n >= k packets as specified. How would
you deal with the (n+1)th packet?

input:
    K: a size

'''

def sample_online_data():


def online_random_sample(it,k):
    sampling_results = list(itertools.islice(it,k))

    num_seen_so_far = k
    for x in it:
        num_seen_so_far +=1
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    return sampling_results
