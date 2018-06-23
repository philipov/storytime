# storytime.simulation

""" begin with a scenario and step through the consequences
    receive input from players
    simultaneous turns, or initiative
    actors perform speculative computation while it's not their turn
"""

from powertools import AutoLogger
log = AutoLogger()
##############################

from collections import namedtuple
import curio
from copy import deepcopy

#----------------------------------------------------------------------------------------------#
from .scenario import Scenario

class Simulation:
    ''' game controller
        progress the state one tick
    '''

    def __init__(self, scenario:Scenario, *, realtime = True):

        scenario.create_world()
        self.scenario       = scenario
        self.actors         = deepcopy(scenario.actors)
        self.world          = deepcopy(scenario.world)

        self.turn_count     = 0

        self.input          = curio.UniversalQueue()
        self.turn_ready     = None if realtime == True else False
        self.actors_ready   = 0

    ############################
    async def timer(self):

        for name, actor in self.actors.items():
            log.print(f'ACTOR: {name}, {actor}')

        command = None
        while True:
            self.turn_count +=1
            log.print(f'TURN: {self.turn_count}' )
            command = await self.prompter()
            log.print(f'CMD:  {command}' )


    ############################
    async def prompter(self):
        ### realtime
        if self.turn_ready is None:
            await curio.sleep(1)

        ### turn-based
        else:
            while self.input.empty():
                await curio.sleep(0.1)

        ### return input, if any
        result = None
        if not self.input.empty():
            result = await self.input.get()

        return result


    ############################
    def next_turn(self, command:str = ''):
        self.input.put(command)




#----------------------------------------------------------------------------------------------#
