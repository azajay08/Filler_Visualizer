import pygame
import os
import sys

grey = (32, 32, 32)
p1_old = (155,48,255)
p1_new = (190, 140, 229)
p2_old = (0,238,238)
p2_new = (0,139,139)
orange = (254, 184, 70)
navy = (0, 0, 25)
peach = (248, 118, 154)
purple = (155,48,255)
yellow = (255, 247, 0)
pink = (255, 0 , 127)
green = (7, 252, 203)

class Settings:
	"""A class to store all the settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = navy

		# delay and fps
		self.delay = 100
		self.fps = 120

		#grid settings 
		self.get_player_info()
		self.get_grid_info()

	def get_player_info(self):
		"""Read from stdin to get player info"""
		for line in range(5):
			sys.stdin.readline()
		line = sys.stdin.readline()
		line_tmp = line.split("/")
		self.p1 = line_tmp[-1]
		self.p1 = self.p1.rstrip("\n")
		line = sys.stdin.readline()
		line = sys.stdin.readline()
		line_tmp = line.split("/")
		self.p2 = line_tmp[-1]
		self.p2 = self.p2.rstrip("\n")
		line = sys.stdin.readline()
				

	def get_grid_info(self):
		"""Read from stdin to get Plateau size"""
		self.line = sys.stdin.readline()
		self.line = self.line.rstrip(':\n').split(' ')
		self.m_height = int(self.line[1])
		self.m_width = int(self.line[2])
		if (self.m_height < self.m_width):
			self.grid_scale = int(self.m_width)
		else:
			self.grid_scale = int(self.m_height)
		self.grid_side = 450 / self.grid_scale - 1

		self.p1_old_piece = pygame.Surface((self.grid_side, self.grid_side))
		self.p1_old_piece.fill(p1_old)
		self.p1_new_piece = pygame.Surface((self.grid_side, self.grid_side))
		self.p1_new_piece.fill(peach)
		self.p2_old_piece = pygame.Surface((self.grid_side, self.grid_side))
		self.p2_old_piece.fill(p2_old)
		self.p2_new_piece = pygame.Surface((self.grid_side, self.grid_side))
		self.p2_new_piece.fill(green)
		self.empty = pygame.Surface((self.grid_side, self.grid_side))
		self.empty.fill(grey)