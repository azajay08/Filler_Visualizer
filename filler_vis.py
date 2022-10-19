import sys
import pygame
import os
import time
from time import sleep
from score import Score
from grid import Grid
from pieces import Piece
from players import Players
from settings import Settings
from title import Title

clock = pygame.time.Clock()

# make the squares eventually pink and light pink, cyan and light cyan
# black background, white and yellow text

class Filler:

	def __init__(self):
		pygame.init()
		# pygame.mixer.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("FILLER")

		# self.score = Score(self)
		
		self.title = Title(self)
		self.player = Players(self)
		self.grid = Grid(self)
		self.score = Score(self)

	def run_game(self):
		while True:
			self.screen.fill(self.settings.bg_colour)
			self._check_events()
			self.title.draw_title()
			self.score.draw_score_title()
			self.player.draw_players()
			self.grid.draw_board()
			clock.tick(self.settings.fps)
			
			pygame.display.flip()
			# pygame.display.update()
			pygame.time.delay(int(self.settings.delay))

	def _check_events(self):
		"""Function that check events in the program"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				elif event.key == pygame.K_1:
					self.settings.delay = 100
				elif event.key == pygame.K_2:
					self.settings.delay = 200
				elif event.key == pygame.K_3:
					self.settings.delay = 300
				elif event.key == pygame.K_4:
					self.settings.delay = 400
				elif event.key == pygame.K_5:
					self.settings.delay = 500
				#check buttons or speed

if __name__ == '__main__':
	filler = Filler()
	filler.run_game()

