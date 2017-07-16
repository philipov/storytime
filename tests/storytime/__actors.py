#!/Anaconda3/python
# storytime

'''
description
'''

from copy import deepcopy
from enum import Enum

#----------------------------------------------------------------------#

from storytime.spatial.surfaces import CoordR

from storytime.time import __Season as Season
from storytime.time import GameTurn

from storytime.actors import __Feature as Feature
from storytime.actors import Entity

def test__Entity():
    entity0 = Entity( index=0 )
    entity1 = deepcopy(entity0)
    entity2 = Entity( CoordR( [0, 0] ), GameTurn( Season.SUMMER ), [Feature.NULL], index=1 )
    entity3 = Entity( CoordR( [1, 0] ), GameTurn( Season.WINTER ), [Feature.DEAD, Feature.SLEEPING], index=2 )

    print( entity0 )
    print( entity1 )
    print( entity2 )
    print( entity3 )

    assert entity0 == entity1
    assert entity0 != entity2
    assert entity1 != entity2

    # assert False


#----------------------------------------------------------------------#
