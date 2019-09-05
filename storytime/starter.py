# storytime.simulation

""" begin with a scenario and step through the consequences
    receive input from players
    simultaneous turns, or initiative
    actors perform speculative computation while it's not their turn
"""

from powertools import AutoLogger
log = AutoLogger()
##############################

import sys
import code
import curio

#----------------------------------------------------------------------------------------------#
from .simulation import Simulation
from . import scenario
from .controller import interactive_interpreter

##############################
class CommandWord:
    ''' call 0-param functions without using ()
        used to create convenient controller commands
    '''
    def __init__(self, func):
        self.func = func
    def __repr__(self):
        return str(self.func())
    def __str__(self):
        return f'<CommandWord {self.func.__name__}>'

def commandword(func):
    return CommandWord(func)

#----------------------------------------------------------------------------------------------#
###     start a game server with repl
##########################################

async def starter(auto):

    this        = await curio.current_task()

    engine      = Simulation(scenario.Test(), realtime=auto)
    timer       = await curio.spawn(engine.timer())

    ### convenience commands
    @commandword
    def q():
        raise SystemExit

    ### spawn task to run python repl in a thread
    controller:curio.Task  = await curio.spawn(curio.run_in_thread(
        interactive_interpreter, {**globals(),**locals()}
    ))

    ### wait
    try:
        while True:
            await curio.sleep(10)
    except SystemExit:
        controller.join()


#----------------------------------------------------------------------------------------------#
