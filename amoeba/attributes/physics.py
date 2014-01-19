#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

from utils.vector import *

class Position(Vector):
    name = 'position'

class Circles(list):
    name = 'circles'
    
    @property
    def centroid(self):
        return sum([c.position for c in self], Vector(0, 0)) / len(self) 
    
class Friction(float):
    name = 'friction'
    
    
class AmoebaPhysics2(object):
    name = 'amoeba_physics_2'
    
    def __init__(self, circles, inner_contraction=0.05, inner_repulsion=100, membrane_contraction=0.05, membrane_repulsion=100):
        self.inner_contraction = inner_contraction
        self.inner_repulsion = inner_repulsion
        self.membrane_contraction = membrane_contraction
        self.membrane_repulsion = membrane_repulsion
        self.membrane = None
        
    def construct_membrane(self, entity):
        centroid = entity.circles.centroid
        amount = 24
        interval = 5
        for i in xrange(amount):
            extrusion = Polar(100, i * 2*math.pi/amount)
            for i in xrange(5, 15):
                temp = extrusion.copy()
                temp.magnitude = i * interval
                if self.calculate_force(entity, centroid + temp) < 3:
                    yield centroid + temp
                    break
            else:
                yield centroid + extrusion
            #yield centroid + extrusion
            
    def calculate_force(self, entity, temp):
        force = Cartesian(0, 0)
        for circle in entity.circles:
            vec = circle.position - temp
            vec.magnitude = 1 / vec.magnitude**2
            force += vec
        vec = entity.circles.centroid - temp
        vec.magnitude = 1 / vec.magnitude**2
        force += vec
        #print force.magnitude * 1000
        return force.magnitude * 1000
            
    def process(self, entity):
        self.membrane = list(self.construct_membrane(entity))
            
        for circle in entity.circles:
            for circle2 in entity.circles:
                if circle is circle2:
                    continue
                v = circle2.position - circle.position
                attraction = v.copy()
                repulsion = v.copy()
                
                attraction.magnitude *= self.inner_contraction
                repulsion.magnitude *= self.inner_repulsion / v.magnitude**2
                circle.velocity += attraction - repulsion
        
        
        '''
        centroid = entity.circles.centroid
        output = []
        for i, vertex in enumerate(self.membrane):
            for j, vertex2 in enumerate(self.membrane):
                if vertex is vertex2:
                    continue
                    
                v = vertex2 - vertex
                if v.magnitude < 100:
                    v.magnitude = 0.1 #self.membrane_repulsion / v.magnitude**2
                    vertex -= v
                
            v1 = centroid - vertex
            v1.magnitude *= self.membrane_contraction
            vertex += v1
            for circle in entity.circles:
                v2 = circle.position - vertex
                if v2.magnitude <= circle.radius:
                    v2.magnitude = circle.radius - v2.magnitude
                    vertex += v2
            output.append(vertex)
        self.membrane = output'''
            
    def draw(self, entity, surface):
        points = [p.pos for p in self.membrane]
        pygame.draw.polygon(surface, (90,90,90), points)
        for circle in entity.circles:
            pygame.draw.circle(surface, (255,255,255), circle.position.pos, int(circle.radius))
        

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
