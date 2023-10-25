'''
Spreadsheets often use an alphabetical encoding of the successive columns. Specifically, columns are identified by "A"
"B", "C", "D", ...

Implement a function that converts a spreadsheet column id to the corresponding integer with "A" corresponding to 1
For example, you should return 4 for D, 27 for AA 
BB
'''
def spreadSheetEncoder(column):
    # the alphabet is of base 26
    id = 0
    po = 0
    for i in range(len(column)-1, -1,-1):
        id += pow(26,po) * (ord(column[i]) - ord("A") + 1)
        po+=1
    return id

print(spreadSheetEncoder("AA"))

