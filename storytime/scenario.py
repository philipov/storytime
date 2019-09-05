# storytime.scenario

""" initial conditions
"""

from powertools import AutoLogger
log = AutoLogger()
##############################

from .world import World

#----------------------------------------------------------------------------------------------#


class Scenario:
    ''' base class for defining game instantiation and rules
        subclasses must provide an implementation for create_world()
    '''

    __world__ = World

    def __init__(self,
                 *args, **kwargs):
        self.world  = type(self).__world__(*args, **kwargs)
        self.create_world()


    #########################
    def create_world(self):
        raise NotImplementedError()


#----------------------------------------------------------------------------------------------#

class Test(Scenario):
    ''' test case
    '''
    def create_world(self):
        self.world.add_agent()
        self.world.add_agent()
        self.world.add_agent()

