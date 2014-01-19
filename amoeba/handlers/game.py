#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

import consts
import events
import entity
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

    # remove enemy from screen
    if other.affiliation == 'enemy':
        if len(player.circles) > len(other.circles):
            player.amoeba_physics.eat(player, other)
            other.add_attributes(attributes.RemoveMe)
        else:
            other.amoeba_physics.eat(other, player)
            player.add_attributes(attributes.RemoveMe)
            player.add_attributes(attributes.Dead)
            # events.post(consts.ENTITY_DEATH, dead=player)
        
    if 'instakill' in other:
        _instakill(player, other)
    elif 'size_increase_powerup' in other:
        _size_increase_powerup(player, other)
    elif 'increase_health' in other:
        _increase_health(player, other)
    elif 'inflicts_damage' in other:
        pass
        # _inflicts_damage(player, other)
    elif 'trigger' in other:
        events.post(consts.TRIGGER, origin=other, tag=other.trigger)
        
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
        
def _increase_health(player, other):
    # events.post(
    #     consts.HEALTH_CHANGED,
    #     target=player,
    #     previous=player.health,
    #     new=player.health + other.increase_health)
    
    player.amoeba_physics.add_random_circle(player)
    other.add_attributes(attributes.RemoveMe)

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
    

class RevealText(object):
    def __init__(self, text_map, entities_manager):
        self.text_map = text_map
        self.entities_manager = entities_manager
        self.triggered = []
        
    def __call__(self, event):
        if event.tag in self.triggered:
            return
        if event.tag in self.text_map:
            self.triggered.append(event.tag)
            text, position = self.text_map[event.tag]
            self.entities_manager.add(entity.Text(position, text))
    
    
class Fling(object):
    def __init__(self, entity):
        self.entity = entity
        self.circles = None
        self.start = None
        
    def __call__(self, event):
        if 'user_controllable' not in self.entity:
            return
        if 'dead' in self.entity:
            return

        self.entity.amoeba_physics.damage(1, self.entity)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start = event.pos
            self.circles = self.entity.circles
        if event.type == pygame.MOUSEBUTTONUP:
            if self.start is None:
                return
            
            v = Vector(*event.pos) - Vector(*self.start)
            cap = 150
            v.magnitude = v.magnitude if v < cap else cap
            v.magnitude *= 0.01
            for circle in self.circles:
                circle.acceleration -= v
            
            self.start = None
            
            events.post(consts.OBJECT_FLUNG, target=self.entity)
        
    def get_clicked(self, event):
        for circle in self.entity.circles:
            if circle.contains_point(event.pos):
                return self.entity.circles
        return None
        