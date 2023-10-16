import pygame
time_taken = 0.0
def initial_setup(graph_info, algo_name):
	graph_info.window.fill(graph_info.BACKGROUND_COLOR)

	title = graph_info.LARGE_FONT.render(f"{algo_name}", 1, graph_info.WHITE)
	graph_info.window.blit(title, (graph_info.width/2 - title.get_width()/2 , 5))

	sorting = graph_info.FONT.render("I - Insertion | B - Bubble | H - Heap | Q - Quick | M - Merge | C - Count | K - Bucket | X - Radix | N - 7.4.5"
											, 1, graph_info.WHITE)
	graph_info.window.blit(sorting, (graph_info.width/2 - sorting.get_width()/2 , 45))
	
	options = graph_info.FONT.render("R - Reset | SPACE - Start Sorting", 1, graph_info.WHITE)
	graph_info.window.blit(options, (graph_info.width/2 - options.get_width()/2 , 75))

	draw_bars(graph_info , time_taken , algo_name)
	pygame.display.update()


def draw_bars(graph_info , time_taken , algo_name ,color_positions={} , clear_bg=False):
	
	timing = graph_info.FONT.render(f"Time : {round(time_taken, 2)}", 1 , graph_info.WHITE)
	graph_info.window.blit(timing, (graph_info.width/2 - timing.get_width()/2 , 110))

	lst = graph_info.lst

	if clear_bg:
		graph_info.window.fill(graph_info.BACKGROUND_COLOR)

		title = graph_info.LARGE_FONT.render(f"{algo_name}", 1, graph_info.Yellow)
		graph_info.window.blit(title, (graph_info.width/2 - title.get_width()/2 , 5))

		timing = graph_info.FONT.render(f"Time : {round(time_taken, 2)}", 1 , graph_info.WHITE)
		graph_info.window.blit(timing, (graph_info.width/2 - timing.get_width()/2 , 110))

		clear_rect = (graph_info.SIDE_PAD//2, graph_info.TOP_PAD, 
						graph_info.width - graph_info.SIDE_PAD, graph_info.height - graph_info.TOP_PAD)
		
		pygame.draw.rect(graph_info.window, graph_info.BACKGROUND_COLOR, clear_rect)
		
	for i, val in enumerate(lst):
		x = graph_info.start_x + i * graph_info.block_width
		y = graph_info.height - (val - graph_info.min_val) * graph_info.block_height

		color = graph_info.GRADIENTS[i % 3]

		if i in color_positions:
			color = color_positions[i] 
		
		pygame.draw.rect(graph_info.window, color, (x, y, graph_info.block_width, graph_info.height))

	pygame.display.update()

def initial_list():
	lst = []

	with open("number_s.txt") as f:
		lst = [int(x) for x in f.read().split()]
	return lst 