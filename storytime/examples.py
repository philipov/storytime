#!/Anaconda3/python
# storytime

'''
description
'''

from .time import Year
from .spatial.surfaces import CoordR
from .actors import Actor

from .history import Event
from .history import History
from .universe import Planet
from .universe import Universe

from .setting import Season
from .setting import Theme
from .setting import Animal


#----------------------------------------------------------------------#

def sample_universe( size_x=20, size_y=10 ) :
    # define time
    start_time = Year( 0, Season.NULL )
    end_time = Year( 10, Season.SUMMER )

    # construct terrain
    terrain = Planet( 10, 10 )

    ### initialize Universe container
    universe = Universe( start_time, terrain )

    ### begin history
    history = History( )
    event0 = Event( Theme.START )
    history.add_event( event0 )

    ### initial population
    universe.add_entity( Actor( CoordR( [3, 3] ), start_time, features=[Animal.FEMALE] ) )
    universe.add_entity( Actor( CoordR( [7, 7] ), start_time, features=[Animal.MALE] ) )
    universe.add_entity( Actor( CoordR( [2, 2] ), start_time, features=[Animal.MALE, Animal.DEAD] ) )

    return universe


#----------------------------------------------------------------------#

from .engine import Engine


def sample_engine( ) :
    engine = Engine( )
