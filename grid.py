import pygame
import pygame.font
import os

grey = (32, 32, 32)
p1_old = (155,48,255)
p1_new = (190, 140, 229)
p2_old = (0,238,238)
p2_new = (150, 187, 232)
orange = (254, 184, 70)
navy = (0, 0, 25)

class Grid:
	"""A class that will display the playing grid"""

	def __init__(self, filler):
		"""Init grid"""

		self.screen = filler.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = filler.settings

		self.width, self.height = 450, 450
		self.grid_colour = navy

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.rect.bottom = self.screen_rect.bottom - 50

	def draw_board(self):
		"""draw the grid"""
		# clear = pygame.Surface((430, 430))
		# clear.fill(p1_old)
		self.screen.fill(self.grid_colour, self.rect)
		# self.screen.blit(clear, self.rect.topleft)

