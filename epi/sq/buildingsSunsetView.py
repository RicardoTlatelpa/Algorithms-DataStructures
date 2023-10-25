'''
You are given a series of buildings that have windows facing west. The buildings
are in a straight line, and any building which is to the east of a building
of equal or greater height cannot view the sunset.

Design an algorithm that processes buildings in east-to-west order and returns
the set of buildings which view the sunset. Each building is specified by its height.
'''


def examine(sequence):
    buildings_that_view_sunset = []
    stack = []
    for i in range(len(sequence)-1,-1,-1):
        num = sequence[i]        
        while stack and stack[-1] <= num:
            stack.pop()
        if len(stack) == 0:
            buildings_that_view_sunset.append(i)        
        stack.append(num)

    return buildings_that_view_sunset

import collections
def examine_buildings_with_sunset(sequence):
    BuildingsWithHeight = collections.namedtuple('BuildingWithHeight', ('id', 'height'))
    candidates = []
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingsWithHeight(building_idx, building_height))
    return [candidate.id for candidate in reversed(candidates)]
print(examine([1,2,3,1,0]))
print(examine_buildings_with_sunset([1,2,3,1,0]))