import pygame.font
import os

white = (245,245,245)
light_cyan = (0,238,238)
dark_cyan = (0,139,139)
deep_pink = (255,20,147)
dark_pink = (139,10,80)
yellow = (255, 247, 0)

font_path = os.path.dirname(os.path.abspath(__file__))
retro = os.path.join(font_path, 'fonts', 'Retro.ttf')
retro_p = os.path.join(font_path, 'fonts', 'filler_grad.otf')

class Players:
	"""A class that will display the players"""

	def __init__(self, filler):
		"""Init players"""
		self.screen = filler.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = filler.settings

		self.p_name_colour = white
		self.p1_colour = yellow
		self.p2_colour = light_cyan
		self.p1_name = pygame.font.Font(retro, 40)
		self.p2_name = pygame.font.Font(retro, 40)
		self.p1 = pygame.font.Font(retro_p, 50)
		self.p2 = pygame.font.Font(retro_p, 50)


	def draw_p1(self):
		"""draw player 1 name"""
		p1_name_str = "mtissari.filler"
		self.player1_name = self.p1_name.render(p1_name_str, True,
					self.p_name_colour, self.settings.bg_colour)
		self.player1_rect = self.player1_name.get_rect()
		self.player1_rect.left = self.screen_rect.left + 100
		self.player1_rect.top = self.screen_rect.top + 350
		self.screen.blit(self.player1_name, self.player1_rect)

		p1_str = "Player.1"
		self.player1 = self.p1.render(p1_str, True,
					self.p1_colour, self.settings.bg_colour)
		self.p1_rect = self.player1.get_rect()
		self.p1_rect.left = self.screen_rect.left + 60
		self.p1_rect.top = self.screen_rect.top + 250
		self.screen.blit(self.player1, self.p1_rect)

	def draw_p2(self):
		"""draw player 2 name"""
		p2_name_str = "ajones.filler"
		self.player2_name = self.p2_name.render(p2_name_str, True,
					self.p_name_colour, self.settings.bg_colour)
		self.player2_rect = self.player2_name.get_rect()
		self.player2_rect.right = self.screen_rect.right - 100
		self.player2_rect.top = self.screen_rect.top + 350
		self.screen.blit(self.player2_name, self.player2_rect)

		p2_str = "Player.2"
		self.player2 = self.p2.render(p2_str, True,
					self.p2_colour, self.settings.bg_colour)
		self.p2_rect = self.player2.get_rect()
		self.p2_rect.right = self.screen_rect.right - 60
		self.p2_rect.top = self.screen_rect.top + 250
		self.screen.blit(self.player2, self.p2_rect)