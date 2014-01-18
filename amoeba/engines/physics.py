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
		self.time

	def process(self):
		update_position()
		process_collisions()
		process_deaths()

	def update_position(self):
		entities = [for entity in entities if entity.Acceleration and entity.Velocity]
		entity.Velocity += entity.Acceleration * self.time
		entity.Position += entity.Velocity * self.time

	def process_collisions(self):
		for i in xrange(len(entities)):
			for k in xrange(i, 1, len(entities)):
				entity1 = entities[i]
				entity2 = entities[k]
				if k != i:
					if _is_collided(entity1, entity2):
						events.post(consts.COLLIDE_EVENT, entity1=entity1, entity1=entity2)

	def _is_collided(entity1, entity2):
		return entity1.Radius + entity2.Radius > _calculate_distance(entity1.pos, entity2.pos)

	def _calculate_distance(self, pos1, po2):
		dx = math.fabs(pos1.x - pos2.x)
		dy = math.fabs(pos1.y - pos2.y)
		return (dx**2 + dy**2)**0.5