#!/Anaconda3/python
# storytime

'''
description
'''


#----------------------------------------------------------------------#

from storytime.time import GameTurn

from copy import deepcopy

def test__Turn( ) :
    turn1 = GameTurn( 2017 )
    turn2 = deepcopy(turn1)
    turn3 = GameTurn( 2018 )

    print( turn1 )
    print( turn2 )
    print( turn3 )

    assert turn1 != turn3

    # assert False


#####################
def test__Turn_next( ) :
    gametime = GameTurn( )
    print( gametime )
    for tick in range( 0, 5 ) :
        assert gametime.tick == tick
        gametime = next( gametime )
        print( gametime )


#----------------------------------------------------------------------#

from storytime.time import Cycle

def test__Cycle( ) :
    print( "Length:", len( Cycle ) )
    # assert False


#####################

from storytime.time import __Season as Season
def test__Season( ) :

    print( "Cycle Length:", len( Season ), Season.cycle_duration() )
    assert len( Season) == 2
    assert Season.cycle_duration( ) == 2

    print( "DURATION", Season.SUMMER.duration, Season.SUMMER )
    assert Season.SUMMER.duration == 1

    print( "DURATION", Season.WINTER.duration, Season.WINTER )
    assert Season.WINTER.duration == 1
    print( "" )

    print( "Season:" )
    gametime = GameTurn( Season )
    print( gametime )
    print( "" )

    for index in range( 0, 10 ) :
        direct_time = GameTurn.from_index( index, Season )
        print( "INDEX:", index, gametime, direct_time )
        assert gametime == direct_time

        gametime = next( gametime )
        print( "" )

    gametime0 = GameTurn( Season.WINTER )
    gametime1 = GameTurn( 2, Season.WINTER )
    print( "0:", gametime0 )
    print( "1:", gametime1 )
    assert gametime0.tick == 1
    assert gametime1.tick == 3

    # assert False


#####################


from storytime.time import __Battle as Battle
def test__Battle( ) :

    print( "Cycle Length:", len( Battle ), Battle.cycle_duration( ) )
    assert len( Battle ) == 3
    assert Battle.cycle_duration( ) == 15

    print( "DURATION", Battle.DEAL.duration, Battle.DEAL )
    assert Battle.DEAL.duration == 9

    print( "DURATION", Battle.BET.duration, Battle.BET )
    assert Battle.BET.duration == 1

    print( "DURATION", Battle.DRAW.duration, Battle.DRAW )
    assert Battle.DRAW.duration == 5
    print( "" )

    print( "Battle:" )
    gametime = GameTurn( Battle.DEAL )
    print( gametime )
    print("")

    for index in range( 0, 10 ) :
        direct_time = GameTurn.from_index( index, Battle)
        print( "INDEX:",index, gametime, direct_time )
        assert gametime == direct_time
        gametime = next( gametime )
        print("")

    # assert False


#----------------------------------------------------------------------#
