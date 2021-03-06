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


##############################
class CommandWord:
    def __init__(self, func):
        self.func = func
    def __repr__(self):
        self.func()
    def __str__(self):
        return f'<CommandWord {self.func.__name__}>'

def commandword(func):
    return CommandWord(func)


#----------------------------------------------------------------------------------------------#

def raise_sys_exit( ) :
    """Called inside interactive console to return to player_function"""
    raise SystemExit
extra_locals = { "exit" : raise_sys_exit }  # other locals go in here

def interactive_interpreter( local_vars:dict ) :
    """Enter the interactive interpreter"""

    local_vars.update(extra_locals)
    #try :
    code.interact( local=local_vars )
    #except SystemExit :
     #   pass


##############################
async def controller(simulation:Simulation):
    #stdin = curio.io.Stream(sys.stdin.buffer)
    while True:
        await curio.sleep(1)


class Controller:
    ''' game controller
        progress the state one tick
    '''

    def __init__(self, simulation):
        self.simulation = simulation


    async def monitor(self):
        stdin = curio.io.Stream(sys.stdin.buffer)
        while True:
            pass

#----------------------------------------------------------------------------------------------#
