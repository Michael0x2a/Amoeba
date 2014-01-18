import pygame

class Renderer(object):
	def __init__(self, entity_manager, screen):
		self.entity_manager = entity_manager
		self.screen = screen

	def render():
		clear_screen()
		draw_entities()

	def clear_screen():
		screen.fill((0,0,0))

	def draw_entities():
		for entity in entity_manager.get('animation','drawable'):
			entity.draw(entity, screen)
