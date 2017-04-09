#!/Anaconda3/python
# storytime

'''
description
'''


#----------------------------------------------------------------------#

from storytime.time import Year

from copy import deepcopy

def test__Year( ) :
    turn1 = Year( 2017 )
    turn2 = deepcopy(turn1)
    turn3 = Year( 2018 )

    print( turn1 )
    print( turn2 )
    print( turn3 )

    assert turn1 != turn3


#####################
def test__next_Year( ) :
    gametime = Year( )
    print( gametime )
    for turn in range( 0, 5 ) :
        next( gametime )
        print( gametime )


#----------------------------------------------------------------------#

from storytime.time import Cycle

def test__Phase( ) :
    print( "Length:", len( Cycle ) )
    # assert False


#####################

from storytime.time import __Season as Season
def test__next_Season( ) :
    print( "Season:" )
    gametime = Year( Season.NULL )
    print( gametime )
    for turn in range( 0, 5 ) :
        next( gametime )
        print( gametime )

    print( "Length:", len( Season ), Season.phase_length() )
    # assert False


#####################


from storytime.time import __Turn as Turn
def test__next_Turn( ) :
    print( "Turn:" )
    gametime = Year( Turn.NULL )
    print( gametime )
    for turn in range( 0, 5 ) :
        next( gametime )
        print( gametime )

    print( "Length:", len( Turn ),  Turn.phase_length() )
    print( Year.__doc__ )
    # assert False


#----------------------------------------------------------------------#
