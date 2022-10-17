import pygame.font
import os
import pygame
from title import Title

peach = (248, 118, 154)
purple = (155,48,255)
yellow = (255, 247, 0)
grey = (32, 32, 32)
orange = (254, 184, 70)
pink = (255, 0 , 127)
font_path = os.path.dirname(os.path.abspath(__file__))
retro_font = os.path.join(font_path, 'fonts', 'filler_grad.otf')

class Score:
	"""A class that will display the score"""

	def __init__(self, filler):
		"""Init scores"""
		self.screen = filler.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = filler.settings
		self.title = filler.title
		self.title_rect = self.title.title_rect

		# sep is a separator
		self.title_colour = peach
		self.sep_colour = orange
		self.title_font = pygame.font.Font(retro_font, 60)
		self.sep_font = pygame.font.Font(retro_font, 60)

		self.prep_score_title()

	def prep_score_title(self):
		"""draw the score title"""
		score_str = "score"
		self.score_title = self.title_font.render(score_str, True,
					self.title_colour, self.settings.bg_colour)
		self.score_title_rect = self.score_title.get_rect()
		self.score_title_rect.centerx = self.title_rect.centerx
		self.score_title_rect.top = self.title_rect.bottom
		# self.score_title_rect.center = self.screen_rect.center
		# self.score_title_rect.top = self.screen_rect.top + 175
		

		# Inserts a separator for scores
		sep_str = "|"
		self.sep_title = self.sep_font.render(sep_str, True,
					self.sep_colour, self.settings.bg_colour)
		self.sep_title_rect = self.sep_title.get_rect()
		self.sep_title_rect.centerx = self.score_title_rect.centerx
		self.sep_title_rect.top = self.score_title_rect.bottom


	def draw_score_title(self):
		"""Draw score title to screen"""
		self.screen.blit(self.score_title, self.score_title_rect)
		self.screen.blit(self.sep_title, self.sep_title_rect)