

'''
methods for executing the simulation
'''

import code
from .utils import prepare_object
from pprint import pprint

from .time import GameTime

#----------------------------------------------------------------------------------------------#

class Engine:
    def __init__( self
                , actors:list = ()
                , zone = None
                , start = None
                , end = None
                ):
        self._actors = [*actors]
        self._zone = zone
        self._time = GameTime(start, end)

    def tick(self):
        pprint(self.actors)
        for actor in self.actors:
            next(actor)
        print('')

    def run(self, ticks):
        for tick in range(ticks):
            self.tick()

    @property
    def actors(self):
        return self._actors


    def zone(self, cls):
        pass

    def __getitem__(self, key):
        pass

#----------------------------------------------------------------------------------------------#

def tick_controller( engine ) :
    """create a callback to control the simulation"""

    def tick_event( gametime ) :
        """advance the game from now_time to gametime"""
        engine.tick(gametime)

    ###
    return tick_event


#----------------------------------------------------------------------------------------------#

# ToDo: Fix skipping of the first turn

def loop_fixed( gametime, end_time, tick_event ) :

    stop_iteration = False
    while not stop_iteration :
        if gametime == end_time :
            stop_iteration = True

        ### tick event
        else :
            print( "--- TURN: ", gametime )
            tick_event( gametime )
            gametime = next( gametime )

            # time.sleep(1)


def loop_interactive( gametime, tick_event, player_event ) :
    try:
        while True :
            print( "--- TURN: ", gametime )
            player_input = input( "> " )

            ### player event
            if player_input != "" :
                player_event( gametime, player_input )

            ### tick event
            else :
                tick_event( gametime )
                gametime = next( gametime )
            print( "" )
    except StopIteration:
        print("")



#----------------------------------------------------------------------------------------------#
