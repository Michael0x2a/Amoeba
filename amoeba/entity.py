#!/usr/bin/env python

from __future__ import division, absolute_import

import collections

import attributes

def Player(springs, *circles):
    circles = list(circles)
    return Entity(
        attributes.Circles(circles),
        attributes.Drawable(),
        attributes.Color(255, 255, 255),
        attributes.AmoebaPhysics(springs),
        attributes.Affiliation('player1'),
        attributes.Health(100),
        attributes.UserControllable(),
        attributes.Friction(0.995))
        
def InstakillEnemy(*circles):
    return Entity(
        attributes.Circles(circles),
        attributes.Drawable(),
        attributes.Color(255, 0, 0),
        attributes.CircleAnimation(),
        attributes.Affiliation('enemy'),
        attributes.InstaKill(),
        attributes.Friction(0.995))
        
def Drifter(*circles):
    return Entity(
        attributes.Circles(circles),
        attributes.Drawable(),
        attributes.Color(0, 255, 0),
        attributes.CircleAnimation(),
        attributes.Affiliation('enemy'),
        attributes.DriftMovement(1),
        attributes.Friction(0.995),
        attributes.InflictsDamage(0.1))
        
def Hunter(*circles):
    return Entity(
        attributes.Circles(circles),
        attributes.Drawable(),
        attributes.Color(0, 255, 0),
        attributes.CircleAnimation(),
        attributes.Affiliation('enemy'),
        attributes.ChasingMovement(2),
        attributes.Friction(0.995),
        attributes.InflictsDamage(0.1))
        
def Bullet(position, velocity, affiliation):
    return Entity(
        attributes.Circles(Circle(position, velocity, 3)),
        attributes.Drawable(),
        attributes.Color(0, 0, 255),
        attributes.CircleAnimation(),
        attributes.Affiliation(affiliation),
        attributes.Friction(1))
            
def Powerup(circle, powerup):
    return Entity(
        attributes.Circles([circle]),
        attributes.Drawable(),
        attributes.Color(0, 255, 0),
        attributes.CircleAnimation(),
        attributes.Affiliation('power_up'),
        attributes.Friction(1),
        powerup)
        
def Text(position, text):
    return Entity(
        attributes.Position(position.x, position.y),
        attributes.Drawable(),
        attributes.DisplayText(text),
        attributes.Affiliation('neutral'))
        
def SizeIncreasePowerUp(*circles):
    return Entity(
        attributes.Circles(circles),
        attributes.Drawable(),
        attributes.Color(0, 255, 0),
        attributes.CircleAnimation(),
        attributes.Affiliation('power_up'),
        attributes.SizeIncrease(),
        )
        
def TriggerRegion(circle, trigger_name):
    return Entity(
        attributes.Circles([circle]),
        attributes.Trigger(trigger_name),
        attributes.Affiliation('neutral'))
        
def Food(circle, health_increase):
    return Entity(
        attributes.Circles([circle]),
        attributes.Drawable(),
        attributes.Color(25, 255, 90),
        attributes.CircleAnimation(),
        attributes.Affiliation('power_up'),
        attributes.IncreaseHealth(),
        )
        
def StationaryEnemy(springs, *circles):
    return Entity(
        attributes.Circles(circles),
        attributes.AmoebaPhysics(springs),
        attributes.Drawable(),
        attributes.Color(255, 0, 0),
        attributes.CircleAnimation(),
        attributes.Affiliation('enemy'),
        attributes.Friction(0.995),
        attributes.InflictsDamage(0.1))

class Entity(object):
    def __init__(self, *attributes):
        self.__dict__['attributes'] = {a.name: a for a in attributes}
        
    def __contains__(self, other):
        if isinstance(other, (tuple, list)):
            return all(attr in self.attributes for attr in other)
        else:
            return other in self.attributes
            
    def add_attributes(self, *attributes):
        for attribute in attributes:
            self.attributes[attribute.name] = attribute
        
    def remove_attributes(self, *attributes):
        for attribute in attributes:
            del self.attributes[attribute]
            
    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        return self.attributes[name]
        
    def __setattr__(self, name, value):
        if name in self.attributes:
            self.attributes[name] = value
        else:
            self.__dict__[name] = value
            
class EntityManager(object):
    def __init__(self, *entities):
        self.entities = list(entities)
        self.cache = {}
    
    def get(self, *attributes):
        return [entity for entity in self.entities if attributes in entity]
        
        # Caching currently doesn't work, since it won't update if entities
        # collect new attributes. FIX LATER.
        #
        #if attributes in self.cache:
        #    return self.cache[attributes]
        #else:
        #    output = [entity for entity in self.entities if attributes in entity]
        #    self.cache[attributes] = output
        #    return output
            
    def add(self, *entities):
        self.entities.extend(entities)
        for entity in entities:
            for attributes in self.cache:
                if attributes in entity:
                    self.cache[attributes].append(entity)
                    
    def prune(self):
        output = []
        for entity in self.entities:
            if 'remove_me' in entity:
                print 'gone'
                continue
            else:
                output.append(entity)
        self.entities = output
        
    def __len__(self):
        return len(self.entities)
        
    def __iter__(self):
        return self.entities.__iter__()
        
    def __contains__(self, item):
        return item in self.entities
        
