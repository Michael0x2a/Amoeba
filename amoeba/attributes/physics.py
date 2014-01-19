#!/usr/bin/env python

from __future__ import division, absolute_import

from utils.vector import *

class Circles(list):
    name = 'circles'

class AmoebaPhysics(object):
    name = 'amoeba_physics'

    '''
    Given ints i and j, springs[i][j] describes a tuple that 
    describe a spring in the format:
        (constant, default_radius')
    '''
    def __init__(self, nodes, springs):
        self.nodes = nodes
        self.springs = springs

    def update_acceleration(self, time=00000000.1):
        """iterates through each edge and updates acceleration"""
        
        def _calculate_spring_acceleration(constant, equilibrium_length, length, direction):
            """assume mass=1, returns cartesian vector"""
            displacement = math.fabs(equilibrium_length - length)
            if length < equilibrium_length:
                direction+= math.pi
            magnitude = constant*(displacement)
            return Polar(magnitude, direction)

        def _calculate_repulsion(distance, direction):
            magnitude = 100 * (1.0/(distance**2))
            return Polar(magnitude, direction + math.pi)

        size = len(self.nodes)
        for i in xrange(size):
            # get a node
            current_node = self.nodes[i]
            for j in xrange(size):
                # compare it to every node besides itself
                if i != j:
                    other_node = self.nodes[j]

                    # calculate distance and direction
                    distance = current_node.position.distance(other_node.position)
                    direction = current_node.position.direction(other_node.position)

                    # spring_force is zero by default
                    spring_force = Cartesian(0, 0)

                    # calculate repulsion
                    repulsion = _calculate_repulsion(distance, direction) 

                    # calculate sprint spring_force if available
                    spring = self.springs[i][j]
                    if spring != None:
                        spring_force = _calculate_spring_acceleration(spring[0], spring[1], distance, direction)

                    # add acceleration vectors to current acceleration
                    current_node.acceleration += spring_force*time + repulsion*time
