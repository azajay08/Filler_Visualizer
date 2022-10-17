import sys
import pygame
import os
from time import sleep
from score import Score
from grid import Grid
from pieces import Piece
from players import Players
from settings import Settings
from title import Title

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
		self.grid = Grid(self)
		self.title = Title(self)
		self.player = Players(self)
		self.score = Score(self)

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			self.screen.fill(self.settings.bg_colour)
			self.title.draw_title()
			self.score.draw_score_title()
			self.player.draw_p1()
			self.player.draw_p2()
			self.grid.draw_board()
			pygame.display.flip()

if __name__ == '__main__':
	filler = Filler()
	filler.run_game()



