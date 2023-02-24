def sort(arr):
	length = len(arr)
	for i in range(1, length):
		x = arr[i]
		for j in range(i, -1, -1):
			if x < arr[j - 1]:
				arr[j] = arr[j - 1]
			else:
				break
		arr[j] = x
		print(arr)


def printArr(arr):
	for item in arr:
		print(item)


if __name__ == '__main__':
	arr = [1, 2, 4, 643, 64, 23, 53, 12, 53, 435, 32]
	sort(arr)
	printArr(arr)
	print(arr)
