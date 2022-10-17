import pygame
import os
import sys

black = (0, 0, 0)
white_smoke = (245,245,245)
light_cyan = (0,238,238)
dark_cyan = (0,139,139)
deep_pink = (255,20,147)
dark_pink = (139,10,80)
purple = (155,48,255)
yellow = (255,165,0)
red = (240, 8, 8)
grey = (160, 160, 160)
orange = (254, 184, 70)
navy = (0, 0, 25)

class Settings:
	"""A class to store all the settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = navy

		#grid settings 
		self.get_player_info()
		self.get_grid_info()

	def get_player_info(self):
		"""Read from stdin to get player info"""

	def get_grid_info(self):
		"""Read from stdin to get Plateau size"""