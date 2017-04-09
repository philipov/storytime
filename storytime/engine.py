#!/Anaconda3/python
# storytime

'''
description
'''

from .meta import prepare_ndarray
from .meta import prepare_object


#----------------------------------------------------------------------#

# ToDo: Fix skipping of the first turn

def loop_fixed( start_time, end_time, tick_event ) :
    gametime = start_time
    stop_iteration = False
    while not stop_iteration :

        if gametime == end_time :
            stop_iteration = True
        else :
            tick_event( gametime )
        # time.sleep(1)


def loop_interactive( gametime, tick_event, player_event ) :
    stop_iteration = False
    while not stop_iteration :
        player_input = input( "> " )

        if player_input != "" :
            stop_iteration = player_event(gametime, player_input)
        else :
            tick_event( gametime )
        print( "" )



#----------------------------------------------------------------------#
import code

def raise_sys_exit( ) :
    """Called inside interactive console to return to player_function"""
    raise SystemExit

extra_locals = { "exit" : raise_sys_exit }  # other locals go in here

def interactive_interpreter( local_vars:dict ) :
    """Enter the interactive interpreter"""
    local_vars.update(extra_locals)
    try :
        code.interact( local=local_vars )
    except SystemExit :
        pass

def player_controller( universe ) :
    def player_function(gametime, command):
        """return stop_iteration"""

        if command == "q" : # quit
            return True

        elif command == "t": # terrain
            print( "Terrain: " )
            print(universe.str_terrain)

        elif command == "e" : # entities
            print( "Entities: ")
            for entity in universe.entities :
                print(entity)

        elif command == "i": # repl
            interactive_interpreter(locals())

        else:
            print("Invalid Command:")
            print("\\n - advance turn")
            print("t  - show terrain")
            print("e  - show entities")
            print("i  - interactive interpreter; exit() to return")
            print("q  - quit" )

        return False
    ###
    return player_function


#----------------------------------------------------------------------#

def tick_controller( universe ) :
    def tick_function( gametime ) :
        next( gametime )
        print( "--- TURN: ", gametime )

        history = None
        universe.tick_time( gametime, history )

    ###
    return tick_function


#----------------------------------------------------------------------#

from .history import History
from .universe import Spacetime
from .universe import Universe

class Engine :
    def __init__( self, universe:Universe=None ) :
        self._history = History( )
        self._spacetime = Spacetime( prepare_object(universe,Universe) )
        self._parameters = dict()

    def create( self ) :
        pass
        # initialize history
        # begin spacetime

    def run( self ) :
        pass

    def step( self ) :
        pass


#----------------------------------------------------------------------#
