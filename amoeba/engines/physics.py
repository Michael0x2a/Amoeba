import math
import events
import consts

class PhysicsEngine(object):
    '''PhysicsEngine is constructed with a list of entities and a time duration

        Usage:
            milliseconds = 10
            physics_engine = PhysicsEngine(entities, 10) 
            physics_engine.process()

        PhysicsEngine.process() does these in order:
            - updates the position of entities with velocity and acceleration
            - processes collisions of entities with radius
    '''
    def __init__(self, entities, time):
        self.entities = entities
        self.time = time

    def process(self):
        entities = self.entities.get('circles')
        self.update_position(entities)
        self.process_collisions(entities)

    def update_position(self, entities):
        width, height = consts.SCREEN_SIZE
        for entity in entities:
            if 'amoeba_physics' in entity:
                entity.amoeba_physics.update_acceleration()

            for circle in entity.circles:
                circle.velocity += circle.acceleration * self.time
                circle.position += circle.velocity * self.time
                circle.acceleration.magnitude = 0
                
                if not 10 < circle.position.x < width - 10:
                    circle.velocity.x *= -1
                if not 10 < circle.position.y < height - 10:
                    circle.velocity.y *= -1
                    
                circle.velocity.magnitude *= entity.friction

    def process_collisions(self, entities):
        for entity1 in entities:
            for entity2 in entities:
                if entity1 is entity2:
                    continue
                for circle1 in entity1.circles:
                    for circle2 in entity2.circles:
                        if circle1.is_intersecting(circle2):
                            events.post(consts.COLLIDE_EVENT, entity1=entity1, entity2=entity2)

    def _is_collided(self, entity1, entity2):
        min_distance = entity1.radius + entity2.radius
        actual_distance = (entity1.position - entity2.position).magnitude
        return actual_distance <= min_distance
        