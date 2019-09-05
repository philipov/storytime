# storytime.core.vmap

"""
voronoi tiles
"""

from powertools import AutoLogger
log = AutoLogger()
##############################

from ..agent import Agent
from ..math import Field, VorMap2D

#----------------------------------------------------------------------------------------------#

class World:
    ''' game controller
        progress the state one tick
    '''

    __field__ =  Field

    def __init__(self,
                 name:str = None,
                 *args, **kwargs):
        self.name   = name
        self.agents = list()
        self.tiles  = None
        self.field  = type(self).__field__(*args, **kwargs)


    #########################
    def add_agent(self,
                  agent_cls:type = Agent,
                  *args, **kwargs):
        ''' create an agent and add it to the world
        '''
        next_index  = len(self.agents)
        agent       = agent_cls(*args, index = next_index, **kwargs)
        self.agents.append(agent)
        return agent


#----------------------------------------------------------------------------------------------#

class Voronoi2D(World):
    __field__ = VorMap2D



#----------------------------------------------------------------------------------------------#
