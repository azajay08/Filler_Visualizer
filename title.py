import pygame
import pygame.font
import os

purple = (155,48,255)
yellow = (255, 247, 0)
grey = (32, 32, 32)
t_colour = (255, 0 , 127)
font_path = os.path.dirname(os.path.abspath(__file__))
retro_font = os.path.join(font_path, 'fonts', 'filler_font.otf')

class Title:
	"""A class that will display the title"""

	def __init__(self, filler):
		"""Init title"""
		self.screen = filler.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = filler.settings

		# self.width, self.height = 400, 400
		# self.grid_colour = grey
		self.title_colour = t_colour
		self.font = pygame.font.Font(retro_font, 150)


	def draw_title(self):
		"""draw the grid"""
		title_str = "filler"
		self.title = self.font.render(title_str, True,
					self.title_colour, self.settings.bg_colour)
		self.title_rect = self.title.get_rect()
		self.title_rect.center = self.screen_rect.center
		self.title_rect.top = self.screen_rect.top + 40
		self.screen.blit(self.title, self.title_rect)