import sys
import pygame
import os
from settings import Settings

# make the squares eventually pink and light pink, cyan and light cyan
# black background, white and yellow text

class Filler:

	def __init__(self):
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("FILLER")

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			self.screen.fill(self.settings.bg_colour)
			pygame.display.flip()

if __name__ == '__main__':
	fil = Filler()
	fil.run_game()



