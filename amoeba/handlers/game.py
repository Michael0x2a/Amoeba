#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

import events

from utils.vector import *

def handle_collision(event):
    player = None
    enemy = None
    if 'player1' in event.entity1:
        player, enemy = event.entity1, event.entity2
    else:
        enemy, player = event.entity1, event.entity2
        
    if 'instakill' in enemy:
        print 'instakill'
        player.health = 0
        if 'user_controllable' in player:
            player.remove_attributes('user_controllable')

    
    #if 'size_increase' in power_up:
    #    print 'SIZE'
    #    player.size
    
class Fling(object):
    def __init__(self, entity):
        self.entity = entity
        self.circle = None
        self.start = None
        
    def __call__(self, event):
        if 'user_controllable' not in self.entity:
            return
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle = self.get_clicked(event)
            if circle is None:
                return
            self.start = event.pos
            self.circle = circle
        if event.type == pygame.MOUSEBUTTONUP:
            if self.start is None:
                return
            
            v = Vector(*event.pos) - Vector(*self.start)
            cap = 150
            v.magnitude = v.magnitude if v < cap else cap
            v.magnitude *= 0.01
            self.circle.acceleration -= v
            
            print self.circle.acceleration
            
            self.start = None
        
    def get_clicked(self, event):
        for circle in self.entity.circles:
            if circle.contains_point(event.pos):
                return circle
        return None
        