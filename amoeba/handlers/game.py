#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

import consts
import events
import attributes

from utils.vector import *

def handle_collision(event):
    player = None
    other = None
    
    if event.entity1.affiliation == 'player1':
        player, other = event.entity1, event.entity2
    elif event.entity2.affiliation == 'player1':
        other, player = event.entity1, event.entity2
    else:
        return
        
    if 'instakill' in other:
        _instakill(player, other)
    elif 'size_increase_powerup' in other:
        _size_increase_powerup(player, other)
    elif 'inflicts_damage' in other:
        _inflicts_damage(player, other)
        
def _inflicts_damage(player, other):
    if player.health <= 0:
        player.add_attributes(attributes.Dead)
        events.post(consts.ENTITY_DEATH, dead=player)
    else:
        events.post(
            consts.HEALTH_CHANGED, 
            target=player, 
            previous=player.health, 
            new=player.health - other.inflicts_damage)
            
        player.health -= other.inflicts_damage
        
def handle_health_changed(event):
    delta = event.new - event.previous
    diff = delta * 0.1
    
    for circle in event.target.circles:
        circle.radius += diff
        
def _instakill(player, other):
    if 'instakill' in other:
        player.add_attributes(attributes.Dead)
        events.post(consts.ENTITY_DEATH, dead=player)
        events.post(consts.HEALTH_CHANGED, target=player, previous=player.health, new=0)
        
        player.health = 0

def _size_increase_powerup(player, other):
    events.post_delayed_event(
        consts.REMOVE_POWERUP, 10, 
        player=player, 
        original_health=player.health,
        increase = other.size_increase_powerup)
    events.post(
        consts.HEALTH_CHANGED,
        target=player,
        previous=player.health,
        new=player.health + other.size_increase_powerup)
        
    player.health += other.size_increase_powerup
    other.add_attributes(attributes.RemoveMe)
    other.size_increase_powerup = 0
    
def handle_removed_powerups(event):
    current_health = event.player.health
    
    if current_health < event.original_health:
        return
        
    prev = event.player.health
    event.player.health -= event.increase
    if event.player.health < event.original_health:
        event.player.health = event.original_health
        
    
    events.post(
        consts.HEALTH_CHANGED,
        target=event.player,
        previous=prev,
        new=event.player.health)
        
    print 'done', event.player.health
    
    
    
class Fling(object):
    def __init__(self, entity):
        self.entity = entity
        self.circle = None
        self.start = None
        
    def __call__(self, event):
        if 'user_controllable' not in self.entity:
            return
        if 'dead' in self.entity:
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
        