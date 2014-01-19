#!/usr/bin/env python

from __future__ import division, absolute_import

class Affiliation(str):
    name = 'affiliation'
    
class InstaKill(object):
    name = 'instakill'
    
class InflictsDamage(float):
    name = 'inflicts_damage'
    
class Health(float):
    name = 'health'

class Size(float):
	name = 'size'

class UserControllable(object):
    name = 'user_controllable'
    
class RemoveMe(object):
    name = 'remove_me'
    
class Dead(object):
    name = 'dead'
    
# Powerups

class SizeIncreasePowerup(float):
	name = 'size_increase_powerup'