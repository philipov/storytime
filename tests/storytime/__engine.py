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


from storytime.engine import tick_controller
def test__tick_controller( universe ):
    tick_event = tick_controller( universe )
    tick_event(universe.gametime)


from storytime.engine import player_controller
def test__player_controller( universe ):
    player_event = player_controller( universe )

    player_event( universe.gametime, "t" )
    player_event( universe.gametime, "e" )
    stop_iteration = player_event( universe.gametime, "q" )


#----------------------------------------------------------------------#

from storytime.engine import Engine
def test__Engine():
    engine = Engine()


#----------------------------------------------------------------------#
