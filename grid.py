import pygame
import pygame.font
import os

grey = (32, 32, 32)

class Grid:
	"""A class that will display the playing grid"""

	def __init__(self, filler):
		"""Init grid"""

		self.screen = filler.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = filler.settings

		self.width, self.height = 450, 450
		self.grid_colour = grey

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.rect.bottom = self.screen_rect.bottom - 50

	def draw_board(self):
		"""draw the grid"""
		self.screen.fill(self.grid_colour, self.rect)



