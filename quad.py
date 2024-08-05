class Solution:
  def searchQuadruplets(self, arr, target):
    quadruplets = []
    arr.sort()
    n = len(arr)
    for i in range(n):
      if i > 0 and arr[i] == arr[i-1]:
        continue
      for j in range(i+1,n):
        if j > i+1 and arr[j] == arr[j-1]:
          continue
        low, high = j+1, n-1
        while(low < high):
          s = arr[i] + arr[j] + arr[low] + arr[high]
          if s == target:
            quadruplets.append([arr[i],arr[j],arr[low],arr[high]])
            low+=1
            high-=1
            while low < high and arr[low] != arr[low+1]:
              low+=1
            while high > low and arr[high] != arr[high-1]:
              high-=1
          elif s > target:
            high-=1
          else:
            low+=1

    # TODO: Write your code here
    return quadruplets
