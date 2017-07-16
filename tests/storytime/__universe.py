#!/Anaconda3/python
# storytime

'''
description
'''


#----------------------------------------------------------------------#

from storytime.universe import Location
def test__Location( ):
    location = Location( 0 )


#----------------------------------------------------------------------#

from storytime.universe import SurfacePlane
def test__Surface( ) :
    surface = SurfacePlane( )


#----------------------------------------------------------------------#

from storytime.universe import Planet
def test__Planet( ):
    planet = Planet( )


#----------------------------------------------------------------------#

from storytime.universe import Universe
def test__Universe( ) :
    universe = Universe( )


#----------------------------------------------------------------------#


from storytime.universe import Spacetime
from storytime.time import GameTurn
from storytime.time import __Season as Season

def test__Spacetime( ) :
    universe = Universe()
    start_time = GameTurn( Season )
    spacetime = Spacetime( start_time, universe )

#----------------------------------------------------------------------#
