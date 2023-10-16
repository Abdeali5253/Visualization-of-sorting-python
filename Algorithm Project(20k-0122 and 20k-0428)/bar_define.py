import pygame
import math

pygame.init()
class BarGraphDraw:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	Yellow = 255,255,0
	BACKGROUND_COLOR = BLACK

	GRADIENTS = [
		(128, 128, 128), #grey color
		(160, 160, 160), #light grey
		(192, 192, 192)  # dark grey
	]

	FONT = pygame.font.SysFont('comicsans', 20)
	LARGE_FONT = pygame.font.SysFont('comicsans', 30)

	SIDE_PAD = 100
	TOP_PAD = 150

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height
		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting Algorithm Visualization")
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
		self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2