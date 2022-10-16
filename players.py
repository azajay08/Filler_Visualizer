import pygame.font
import os

white = (245,245,245)

font_path = os.path.dirname(os.path.abspath(__file__))
retro = os.path.join(font_path, 'fonts', 'Retro.ttf')

class Players:
	"""A class that will display the players"""

	def __init__(self, filler):
		"""Init players"""
		self.screen = filler.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = filler.settings

		self.p_name_colour = white
		self.p1_title = pygame.font.Font(retro, 40)
		self.p2_title = pygame.font.Font(retro, 40)

	def draw_p1(self):
		"""draw player 1 name"""
		p1_str = "mtissari.filler"
		self.player1 = self.p1_title.render(p1_str, True,
					self.p_name_colour, self.settings.bg_colour)
		self.player1_rect = self.player1.get_rect()
		self.player1_rect.left = self.screen_rect.left + 40
		self.player1_rect.top = self.screen_rect.top + 100
		self.screen.blit(self.player1, self.player1_rect)

	def draw_p1(self):
		"""draw player 2 name"""
		p2_str = "ajones.filler"
		self.player2 = self.p2_title.render(p2_str, True,
					self.p_name_colour, self.settings.bg_colour)
		self.player2_rect = self.player2.get_rect()
		self.player2_rect.right = self.screen_rect.right - 40
		self.player2_rect.top = self.screen_rect.top + 100
		self.screen.blit(self.player2, self.player2_rect)