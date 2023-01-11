def inversion_count(lst, n):
	temp = [0] * n
	return inversion_count_recursive(lst, temp, 0, n-1)

def inversion_count_recursive(lst, temp, left,right):
	inv_count = 0
	if left < right:
		mid = (left + right)//2
		inv_count += inversion_count_recursive(lst,temp,left,mid)
		inv_count += inversion_count_recursive(lst, temp, mid + 1, right)
		inv_count += find_inversion_count(lst,temp,left,mid,right)
	return inv_count

def find_inversion_count(lst, temp, left, mid, right):
	i = left
	j = mid + 1
	k = left
	inv_count = 0
    
	print(left,mid,right)

	while i <= mid and j <= right:
		if lst[i] <= lst[j]:
			temp[k] = lst[i]
			k+=1
			i+=1
		else:
			temp[k] = lst[j]
			inv_count += (mid - i + 1)
			k += 1
			j += 1
	while i <= mid:
		temp[k] = lst[i]
		k += 1
		i += 1
	while j <= right:
		temp[k] = lst[j]
		k += 1
		j += 1
	for index in range(left,right + 1):
		lst[index] = temp[index]
	print(lst,temp)
	return inv_count

# Test cases

list1 = [3,2,8,4]
list2 = [7, 6, 5, 8]
list3 = [10, 9, 8, 7, 6]
list4 = [1, 2, 3, 4, 5]
diegolist = [5.4,17.20,10.2,-5.04, 3]
print(list1,inversion_count(list1, len(list1)))
print(list2,inversion_count(list2, len(list2)))
print(list3,inversion_count(list3, len(list3)))
print(list4,inversion_count(list4, len(list4)))
print(diegolist, inversion_count(diegolist, len(diegolist)))