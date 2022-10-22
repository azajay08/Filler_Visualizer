import pygame.font
import os

p1_colour = (255, 0, 127) # pink
p2_colour = (0,238,238) # light cyan

class Piece:
	"""A class that will display the pieces"""

	def __init__(self, filler):
		"""Init piece"""
		self.screen = filler.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = filler.settings
		self.player = filler.player



	def draw_piece(self, p_num):
		"""Draws the piece underneath the respective player"""
		line = self.settings.line.rstrip(':').split(' ')
		print(self.settings.line)
		p_height = int(line[1])
		p_width = int(line[2])
		print(p_height, p_width)
		if p_height < p_width:
			p_scale = int(p_width)
		else:
			p_scale = int(p_height)
		p_size = 100 / p_scale
