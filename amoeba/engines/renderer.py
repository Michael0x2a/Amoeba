import pygame

class Renderer(object):
    def __init__(self, entity_manager):
        self.entity_manager = entity_manager

    def render(self, screen):
        self.clear_screen(screen)
        self.draw_entities(screen)

    def clear_screen(self, screen):
        screen.fill((0,0,0))

    def draw_entities(self, screen):
        for entity in self.entity_manager.get('animation','drawable'):
            entity.animation.draw(entity, screen)
