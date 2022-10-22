import readline
import sys
import pygame
import os
import time
import subprocess
from time import sleep
from score import Score
from grid import Grid
from pieces import Piece
from players import Players
from settings import Settings
from title import Title

white = (255, 255, 255)

clock = pygame.time.Clock()


class Filler:

	def __init__(self):
		pygame.init()
		# pygame.mixer.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("FILLER")

		self.title = Title(self)
		self.player = Players(self)
		self.grid = Grid(self)
		self.score = Score(self)
		self.piece = Piece(self)
		self.screen.fill(self.settings.bg_colour)
		self.title.draw_title()
		self.score.draw_score_title()
		self.player.draw_players()

	def run_game(self):
		while True:
			self._check_events()
			if 'Plateau' in self.settings.line:
				self.grid.draw_board()
			self.settings.line = sys.stdin.readline().rstrip('\n')
			if 'Piece' in self.settings.line:
				print(self.settings.line)
				self.piece.draw_piece(1)
			print(self.settings.line)
			if 'fin' in self.settings.line:
				self.settings.line = self.settings.line.split(' ')
				p1_score = int(self.settings.line[3])
				self.settings.line = sys.stdin.readline().rstrip('\n').split(' ')
				p2_score = int(self.settings.line[3])
				# self.player.print_winner(p1_score, p2_score)
				if p1_score == p2_score:
					winner = 0
				elif p1_score > p2_score:
					self.screen.blit(self.player.winner_g, self.player.p1_winner_rect)
				else:
					self.screen.blit(self.player.winner_g, self.player.p2_winner_rect)

			clock.tick(self.settings.fps)
			pygame.display.flip()
			# pygame.display.update()
			pygame.time.delay(int(self.settings.delay))
			# sleep(10)

	def _check_events(self):
		"""Function that check events in the program"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				#check buttons or speed
				if event.key == pygame.K_1:
					self.settings.delay = 75
				if event.key == pygame.K_2:
					self.settings.delay = 25
				if event.key == pygame.K_3:
					self.settings.delay = 12
				if event.key == pygame.K_4:
					self.settings.delay = 5
				if event.key == pygame.K_5:
					self.settings.delay = 1
				if event.key == pygame.K_6:
					self.settings.delay = 0.5
				if event.key == pygame.K_7:
					self.settings.delay = 0.01
				if event.key == pygame.K_8:
					self.settings.delay = 0.0001
				if event.key == pygame.K_9:
					self.settings.delay = 0.000001
				# if event.key == pygame.K_SPACE:
				# 	pause_game()
				

if __name__ == '__main__':
	filler = Filler()
	filler.run_game()

