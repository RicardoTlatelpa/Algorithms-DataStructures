'''
9.15
Write a program that computes the exterior of a binary tree.
'''

def exterior(root):
    exterior = []
    r_ext = []
    def getExterior(root,lc,rc):
        nonlocal exterior,r_ext
        if root is None:
            return
        if (root and root.left == None and root.right == None) or lc > 0 and rc == 0 or lc == 0 and rc == 0:
            exterior.append(root.val)
        elif lc == 0 and rc > 0:
            r_ext.append(root.val)
        getExterior(root.left,lc+1,rc)
        getExterior(root.right,lc,rc+1)
    getExterior(root,0,0)

    while(r_ext):
        exterior.append(r_ext.pop())
    return exterior

