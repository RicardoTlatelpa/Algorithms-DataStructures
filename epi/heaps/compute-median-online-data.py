'''
10.5 Compute the median of online data
'''

# in the odd case, it's the middle element
# in the even case, it's the middle element idx + middle element idx + 1 / 2 

def compute_median(sequence):
    ans = []
    median_array = [] # maintain a sort
    for n in sequence:
        median_array.append(n)
        median_array.sort()# nLogn * n => n^2
        odd = len(median_array)%2!=0 or len(median_array) == 1
        mid_idx = (len(median_array)-1)//2
        if odd:
            ans.append(median_array[mid_idx])
        else:
            compute_median = (median_array[mid_idx] + median_array[mid_idx+1])/2
            ans.append(compute_median)
    return ans


print(compute_median([1,0,3,5,2,0,1]))
