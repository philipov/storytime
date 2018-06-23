# storytime.scenario

""" initial conditions
"""

from powertools import AutoLogger
log = AutoLogger()
##############################

from .world import World
from .agent import Agent


#----------------------------------------------------------------------------------------------#

class Scenario:
    ''' generate a world
        populate it with actors
    '''

    def __init__(self, world_class=World):
        self.actors = dict()
        self.world  = world_class()
        self.create_world()

    def create_world(self):
        raise NotImplementedError()



#----------------------------------------------------------------------------------------------#

class Test(Scenario):
    ''' test case
    '''

    def create_world(self):
        self.actors['1'] = Agent()
        self.actors['2'] = Agent()

        return self.world
