import math
import events
import consts
import attributes

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
                entity.amoeba_physics.update_acceleration(entity, self.time)
            # if 'amoeba_physics_2' in entity:
            #     entity.amoeba_physics_2.process(entity)

            for circle in entity.circles:
                circle.velocity += circle.acceleration * self.time
                circle.position += circle.velocity * self.time
                circle.acceleration.magnitude = 0
                
                if not 10 < circle.position.x < width - 10:
                    circle.velocity.x *= -1
                if not 10 < circle.position.y < height - 10:
                    circle.velocity.y *= -1
                    
                if 'friction' in entity:
                    circle.velocity.magnitude *= entity.friction

    def process_collisions(self, entities):
        for i in xrange(len(entities)-1, -1, -1):
            entity1 = entities[i]
            for j in xrange(len(entities)-1, -1, -1):
                entity2 = entities[j]
                if entity1 is entity2:
                    # skip if comparing same entities
                    continue
                if self._are_entities_collided(entity1, entity2):
                    player = None
                    other = None
                    if not 'user_controllable' in entity1 and not 'user_controllable' in entity2:
                        continue
                        # enemy = None
                        # other2 = None
                        # if entity1.affiliation == 'enemy':
                        #     enemy, other2 = entity1, entity2
                        # elif entity2.affiliation == 'enemy':
                        #     enemy, other2 = entity2, entity1
                        # else:
                        #     continue
                        # if other2.affiliation == 'power_up':
                        #     enemy.amoeba_physics.add_random_circle(enemy)
                        #     entities.pop(j)
                        # continue

                    elif 'user_controllable' in entity1:
                        player, other = entity1, entity2
                    else:
                        player, other = entity2, entity1
                    if other.affiliation == 'enemy':
                        if len(player.circles) > len(other.circles):
                            # yum!
                            player.amoeba_physics.eat(player, other)
                            other.add_attributes(attributes.RemoveMe)
                            entities.pop(j)
                        else:
                            # dead!
                            other.amoeba_physics.eat(other, player)
                            player.add_attributes(attributes.RemoveMe)
                            player.add_attributes(attributes.Dead)
                    elif other.affiliation == 'power_up':
                        player.amoeba_physics.add_random_circle(player)
                        other.add_attributes(attributes.RemoveMe)
                        entities.pop(j)


    def _are_entities_collided(self, entity1, entity2):
        for circle1 in entity1.circles:
            for circle2 in entity2.circles:
                if circle1.is_intersecting(circle2):
                    return True
        return False
        
    def _is_collided(self, entity1, entity2):
        min_distance = entity1.radius + entity2.radius
        actual_distance = (entity1.position - entity2.position).magnitude
        return actual_distance <= min_distance
        