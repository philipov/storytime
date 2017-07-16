#!/Anaconda3/python
# storytime

'''
description
'''

import pytest

#----------------------------------------------------------------------#

# ToDo: test for null constructor
# ToDo: null constructor should __init__ empty list for list-colors parameters

# ToDo: test for existance of copy constructor with deepcopy

# ToDo: test constructor with random values based on parameter colors annotations

# ToDo: test for string representation

# ToDo: if a class should have an interface, test for the interface methods

# ToDo: Parametrize above tests with a class variable for an arbitrary list of classes

# ToDo: Construct list of classes by checking the associated module


#----------------------------------------------------------------------#
from storytime.engine import Engine

def test__Engine( start_time ) :
    engine = Engine( start_time )

    # assert False


#----------------------------------------------------------------------#
from storytime.engine import tick_controller

def test__tick_controller( engine, next_time ):
    tick_event = tick_controller( engine )
    with pytest.raises(RuntimeError):
        tick_event( next_time )

    engine.initialize( next_time )
    tick_event( next_time )

    # assert False


#----------------------------------------------------------------------#
from storytime.engine import player_controller
def test__player_controller( engine, next_time ):

    player_event = player_controller( engine )
    player_event( next_time, "t" )
    player_event( next_time, "e" )

    with pytest.raises( StopIteration ) :
        player_event( next_time, "q" )

    # assert False


#----------------------------------------------------------------------#
from storytime.engine import loop_fixed

def test__loop_fixed(start_time, end_time, engine ) :
    engine.initialize( start_time )
    tick_event = tick_controller( engine )
    loop_fixed(start_time, end_time, tick_event)

    # assert False

#----------------------------------------------------------------------#

