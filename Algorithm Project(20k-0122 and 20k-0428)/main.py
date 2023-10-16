import pygame
from draw_bars import initial_list,initial_setup
from bar_define import BarGraphDraw
from sorting_algo import *

pygame.init()
run = True
clock = pygame.time.Clock()

width = 1200
height = 800
screen = pygame.display.get_surface()

lst = initial_list()
graph_info = BarGraphDraw(width, height, lst)

sorting = False
sorting_algo_name = "Sorting Visualizer"
generator = None

while run:
	clock.tick(5)
	if sorting:
		try:
			next(generator)
		except StopIteration:
			sorting = False
	else:
		initial_setup(graph_info, sorting_algo_name)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r or sorting == True:
				lst = initial_list()
				graph_info.set_list(lst)
				sorting = False

			elif event.key == pygame.K_SPACE and sorting == False:
				sorting = True
				generator = sorting_algorithm(graph_info)

			elif event.key == pygame.K_i and not sorting:
				sorting_algorithm = insertion_sort
				sorting_algo_name = "Insertion Sort"

			elif event.key == pygame.K_b and not sorting:
				sorting_algorithm = bubble_sort
				sorting_algo_name = "Bubble Sort"

			elif event.key == pygame.K_h and not sorting:
				sorting_algorithm = heapSort
				sorting_algo_name = "Heap Sort"

			elif event.key == pygame.K_q and not sorting:
				sorting_algorithm = quick_Sort
				sorting_algo_name = "Quick Sort"

			elif event.key == pygame.K_m and not sorting:
				sorting_algorithm = merge_sort(lst, graph_info)
				sorting_algo_name = "Merge Sort"
			
			elif event.key == pygame.K_c and not sorting:
				sorting_algorithm = countSort
				sorting_algo_name = "Count Sort"
			
			elif event.key == pygame.K_k and not sorting:
				sorting_algorithm = bucketSort
				sorting_algo_name = "Bucket Sort" # remember to switch start list

			elif event.key == pygame.K_x and not sorting:
				sorting_algorithm = radix_sort
				sorting_algo_name = "Radix Sort"

			elif event.key == pygame.K_n and not sorting:
				sorting_algorithm = book_sort1
				sorting_algo_name = "7.4.5"

pygame.quit()