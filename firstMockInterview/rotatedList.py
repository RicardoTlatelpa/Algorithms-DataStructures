'''
Write a function that rotates a list by k
elements. For example [1,2,3,4,5,6] 
rotated by two becomes [3,4,5,6,1,2]

'''

def rotateList(l,k):
    for i in range(len(l)):
        newIdx = (i + k)%(len(l))
        l[newIdx] = i
    return l
l = [1,2,3,4,5]
for i in range(0,11):
    print(rotateList(l, i))
