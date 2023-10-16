from time import sleep, time
from draw_bars import draw_bars

def insertion_sort(graph_info):
	start_time = time()
	lst = graph_info.lst

	for i in range(1, len(lst)):
		current = lst[i]

		while True:
			sort = i > 0 and lst[i - 1] > current 
			if not sort:
				break

			lst[i] = lst[i - 1]
			i = i - 1
			lst[i] = current
			time_taken = time() - start_time
			draw_bars(graph_info, time_taken , "Insertion Sort" ,{i - 1: graph_info.Yellow, i: graph_info.RED}, True)
			yield True
	sleep(7)

def bubble_sort(graph_info):
	start_time = time()
	
	lst = graph_info.lst

	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			if (lst[j] > lst[j + 1]):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				time_taken = time() - start_time
				draw_bars(graph_info, time_taken , "Bubble Sort" ,{j: graph_info.Yellow, j + 1: graph_info.RED}, True)
				yield True
	sleep(7)

def buildMaxHeap(arr, n):
 
	for i in range(n):
        # if child is bigger than parent
		if arr[i] > arr[int((i - 1) / 2)]:
			j = i
     
            # swap child and parent until parent is smaller
			while arr[j] > arr[int((j - 1) / 2)]:
				(arr[j],arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],arr[j])
				j = int((j - 1) / 2)

def heapSort(graph_info):
	start_time = time()
	arr = graph_info.lst
	n = len(arr)
	buildMaxHeap(arr, n)
 
	for i in range(n - 1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		j, index = 0, 0
         
		while True:
			time_taken = time() - start_time
			index = 2 * j + 1
   			
			if (index < (i - 1) and arr[index] < arr[index + 1]):
				index += 1

			if index < i and arr[j] < arr[index]:
				arr[j], arr[index] = arr[index], arr[j]
				
				draw_bars(graph_info, time_taken, "Heap Sort" ,{j: graph_info.Yellow, j-1: graph_info.RED}, True)
         
			j = index
			if index >= i:
				break
	yield True
	sleep(7)

def partition(arr , l , h , graph_info , time_taken):
	i = ( l - 1 )
	x = arr[h]
 
	for j in range(l , h):
		if arr[j] <= x:
			i = i + 1
			arr[i],arr[j] = arr[j],arr[i]
			draw_bars(graph_info , time_taken, "Quick Sort" , {i+1: graph_info.Yellow , h: graph_info.RED}, True)
	arr[i+1],arr[h] = arr[h],arr[i+1]
	yield i+1

def quick_Sort(graph_info):
	start_time = time()
	arr = graph_info.lst
	l = 0
	h = len(arr) - 1
 	# Create an auxiliary stack
	size = h - l + 1
	stack = [0 for i in range(size)]
 
    # initialize top of stack
	top = -1
 
    # push initial values of l and h to stack
	top = top + 1
	stack[top] = l
	top = top + 1
	stack[top] = h
 
    # Keep popping from stack while is not empty
	while top >= 0:
        # Pop h and l
		h = stack[top]
		top = top - 1
		l = stack[top]
		top = top - 1
 
        # Set pivot element at its correct position in sorted array
		time_taken = time() - start_time
		p = next(partition(arr, l, h  , graph_info , time_taken))
		
        # If there are elements on left side of pivot, then push left side to stack
		if (p-1) > l:
			top = top + 1
			stack[top] = l
			top = top + 1
			stack[top] = p - 1
 
        # If there are elements on right side of pivot,then push right side to stack
		if (p + 1) < h:
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h
		time_taken = time() - start_time
		draw_bars(graph_info, time_taken , "Quick Sort" ,{p: graph_info.Yellow, h: graph_info.RED}, True)
	yield True
	sleep(7)

def merge_sort(arr, graph_info):
	def mergeSort(arr , low , high):
		start_time = time()	
		if low < high:
			m = (low+(high-1))//2
			mergeSort(arr, low, m)
			mergeSort(arr, m+1, high)
			merge(arr, low, m, high , start_time)

	def merge(arr , low , m , high , start_time):
		n1 = m - low + 1
		n2 = high - m
		L = [0 for i in range(n1)]
		R = [0 for i in range(n2)]
		for i in range(0, n1):
			L[i] = arr[low + i]
		for i in range(0, n2):
			R[i] = arr[m + i + 1]
	
		i, j, k = 0, 0, low
		while i < n1 and j < n2:
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
			time_taken2 = 0
			draw_bars(graph_info, time_taken2 , "Merge Sort" ,{j: graph_info.Yellow, k: graph_info.RED}, True)
		while i < n1:
			arr[k] = L[i]
			i += 1
			k += 1
			# time_taken = time() - start_time
			draw_bars(graph_info, time_taken2, "Merge Sort" ,{j: graph_info.Yellow, k: graph_info.RED}, True)
		while j < n2:
			arr[k] = R[j]
			j += 1
			k += 1
			time_taken = time() - start_time
			draw_bars(graph_info, time_taken, "Merge Sort" ,{j: graph_info.Yellow, k: graph_info.RED}, True)	
	mergeSort(arr , 0 , len(arr)-1)
	sleep(7)
	
def countSort(graph_info):
	start_time = time()
	array = graph_info.lst
	size = len(array)
	output = [0 for i in range(size)]

	# Initialize count array
	count = [0] * size

	# Store the count of each elements in count array
	for i in range(0, size):
		count[array[i]] += 1

	# Store the cummulative count
	for i in range(1, size):
		count[i] += count[i - 1]

	# Find the index of each element of the original array in count array place the elements in output array
	i = size - 1
	time_taken = 0
	while i >= 0:
		output[count[array[i]] - 1] = array[i]
		draw_bars(graph_info, time_taken, "Count Sort" ,{i: graph_info.Yellow, i-1: graph_info.RED}, True)
		yield True
		count[array[i]] -= 1
		i -= 1
	time_taken = time() - start_time
	for i in range(0, size):
		array[i] = output[i]
		draw_bars(graph_info, time_taken, "Count Sort" ,{i: graph_info.Yellow, i-1: graph_info.RED}, True)

	sleep(7)

def insertion_Sort2(b , graph_info , start_time):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up: 
			b[j + 1] = b[j]
			j -= 1
			time_taken = time() - start_time
			draw_bars(graph_info, time_taken, "Bucket Sort" ,{j: graph_info.Yellow, j+1: graph_info.RED}, True)
		b[j + 1] = up
	return b
			  
			
def bucketSort(graph_info):
	start_time = time()
	x = graph_info.lst
	insertion_Sort2(x , graph_info , start_time)
	arr = []
	slot_num = 10 # 10 means 10 slots, each slot's size is 0.1
	for i in range(slot_num):
		arr.append([])
		
	# Put array elements in different buckets 
	for j in x:
		index_b = int(slot_num * j) 
		arr[index_b].append(j)
	
	# Sort individual buckets 
	for i in range(slot_num):
		arr[i] = insertion_Sort2(arr[i] , graph_info , start_time)
	time_taken = time() - start_time
	draw_bars(graph_info, time_taken, "Bucket Sort" ,{i: graph_info.Yellow, i+1: graph_info.RED}, True)

	yield True   
	sleep(5)

def countingSort(arr, exp1 , graph_info , start_time):
	n = len(arr)	
	output = [0] * (n)
	count = [0] * (10)

	for i in range(0, n):
		index = (arr[i]/exp1)
		count[int((index)%10)] += 1

	for i in range(1,10):
		count[i] += count[i-1]

	# Build the output array
	i = n-1
	while i >= 0:
		index = (arr[i]/exp1)
		output[ count[int((index)%10) ] - 1] = arr[i]
		time_taken = time() - start_time
		draw_bars(graph_info, time_taken * 3, "Radix Sort" ,{exp1: graph_info.Yellow, i: graph_info.RED}, True)
		count[int((index)%10)] -= 1
		i -= 1
	
	i = 0
	for i in range(0,len(arr)):
		arr[i] = output[i]

def radix_sort(graph_info):
	start_time = time()
	arr = graph_info.lst
	max1 = max(arr)
	threshold = len(str(max1))+1
	exp = 1
	while threshold > 0:
		countingSort(arr , exp , graph_info , start_time )
		exp *= 10
		threshold = threshold-1
	yield True
	sleep(7)

def insertionSort3(arr , low , high , graph_info , time_taken):
	start_time = time()
	for i in range(low, high):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
			arr[j + 1] = arr[j]
			j -= 1
			arr[j + 1] = key
			time_taken2 = time() - start_time
			time_taken = time_taken+time_taken2
			draw_bars(graph_info, time_taken, "7.4.5" ,{j + 1: graph_info.Yellow, j: graph_info.RED}, True)

def partition1(array, low, high , graph_info , time_taken):
	pivot = array[high] 
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:	
			i = i + 1				
			(array[i], array[j]) = (array[j], array[i])
			draw_bars(graph_info , time_taken , " 7.4.5" ,{i+1: graph_info.Yellow , j: graph_info.RED}, True)
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def book_sort1(graph_info):
	start_time = time()
	arr = graph_info.lst
	l = 0
	h = len(arr) - 1
	size = h - l + 1
	stack = [0 for i in range(size)]
	top = -1
 
	top = top + 1
	stack[top] = l
	top = top + 1
	stack[top] = h
 
	while top >= 0:
		if(h+l-1) < size*0.20:
			time_taken = time() - start_time
			insertionSort3(arr , l , h+1 ,graph_info , time_taken)
			break
		else:
			# Pop h and l
			h = stack[top]
			top = top - 1
			l = stack[top]
			top = top - 1
	
			# Set pivot element at its correct position in sorted array
			time_taken = time() - start_time
			p = partition1(arr, l, h , graph_info , time_taken)
			time_taken = time() - start_time
			draw_bars(graph_info, time_taken, "7.4.5" ,{p: graph_info.Yellow, h: graph_info.RED}, True)
			# If there are elements on left side of pivot, then push left side to stack
			if (p-1) > l:
				top = top + 1
				stack[top] = l
				top = top + 1
				stack[top] = p - 1
	
			# If there are elements on right side of pivot,then push right side to stack
			if (p + 1) < h:
				top = top + 1
				stack[top] = p + 1
				top = top + 1
				stack[top] = h
	yield True
	sleep(7)


