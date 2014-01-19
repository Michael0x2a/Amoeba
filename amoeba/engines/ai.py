#!/usr/bin/env python

from __future__ import division, absolute_import

class AIEngine(object):
    def __init__(self, entities):
        self.entities = entities

    def process(self):
        for entity in self.entities.get('movement_ai'):
            entity.movement_ai.process(entity, self.entities)