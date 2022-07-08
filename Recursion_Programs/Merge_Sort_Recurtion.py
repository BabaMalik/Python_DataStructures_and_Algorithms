"""
 Method that perform the merge operation with two lists.
"""
def merge(left, right):
	result = []
	i, j = 0, 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j] :
			result.append(left[i])
			i = i + 1
		else:
			result.append(right[j])
			j = j + 1

	while i < len(left):
		result.append(left[i])
		i = i + 1

	while j < len(right):
		result.append(right[j])
		j = j + 1

	return result

""" 
 Mergesort algorithm recursive implementation.
"""
def mergesort(l):
	print(l)
	if len(l) < 2:
		return l[:]
	else:
		middle = len(l) // 2
		left = mergesort(l[:middle])
		right = mergesort(l[middle:])

		merged_list = merge(left, right)
		print('Merged ', merged_list)
		return merged_list


n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
lst = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
ordered_lst = mergesort(lst)
print(ordered_lst)