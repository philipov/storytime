#!/Anaconda3/python
# storytime

'''
description
'''

import pytest


#----------------------------------------------------------------------#
from storytime.time import GameTurn
from storytime.time import __Season as Season

@pytest.fixture
def start_time( ) :
    season = Season.SUMMER
    gametime = GameTurn( season )
    print( "fixture START_TIME", gametime, season )
    return gametime


@pytest.fixture
def next_time( ) :
    season = Season.WINTER
    gametime = GameTurn( 1, season )
    print("fixture NEXT_TIME", gametime, season)
    return gametime


@pytest.fixture
def end_time( ) :
    season = Season.SUMMER
    gametime = GameTurn( 3, season )
    print( "fixture END_TIME", gametime, season )
    return gametime

#----------------------------------------------------------------------#
from storytime.universe import Universe


@pytest.fixture
def universe( ) :
    return Universe( )

#----------------------------------------------------------------------#
from storytime.engine import Engine

@pytest.fixture
def engine( start_time, universe ):
    print("fixture ENGINE", start_time, universe)
    return Engine(start_time, universe)


#----------------------------------------------------------------------#
