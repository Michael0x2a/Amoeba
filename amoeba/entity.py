#!/usr/bin/env python

from __future__ import division, absolute_import

import collections

import attributes

def Player(position, velocity):
    return Entity(
        attributes.Position(position.x, position.y),
        attributes.Velocity(velocity.magnitude, velocity.angle),
        attributes.Acceleration(velocity.magnitude, velocity.angle),
        attributes.Drawable(),
        attributes.Radius(20),
        attributes.Color(255, 255, 255)
        attributes.CircleAnimation(),
        attributes.Affiliation('player1'))

class Entity(object):
    def __init__(self, *attributes):
        self.__dict__['attributes'] = {a.name: a for a in attributes}
        
    def __contains__(self, other):
        if isinstance(other, (tuple, list)):
            return all(o.name in self.attributes for o in other)
        else:
            return other.name in self.attributes
            
    def add_attributes(self, *attributes):
        for attribute in attributes:
            self.attributes[attribute.name] = attribute
        
    def remove_attributes(self, *attributes):
        for attribute in attributes:
            del self.attributes[attribute.name]
            
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
        
    def __len__(self):
        return len(self.entities)
        
    def __iter__(self):
        return self.entities.__iter__()
        
    def __contains__(self, item):
        return item in self.entities
        