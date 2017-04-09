#!/Anaconda3/python
# storytime

"""
description
"""

import storytime
import storytime.examples
import storytime.setting

#----------------------------------------------------------------------#

def main( ) :
    ### begin
    print( "### BEGIN Simulation" )

    ### __init__ universe
    start_time  = storytime.Year( 0, storytime.setting.Season.NULL )
    end_time    = storytime.Year( 10, storytime.setting.Season.SUMMER )

    universe    = storytime.examples.sample_universe( 20, 10 )

    ### main loop - with player events

    tick_event      = storytime.tick_controller( universe )
    player_event    = storytime.player_controller( universe )

    storytime.loop_interactive( start_time, tick_event, player_event )

    ### end
    print( "### END Simulation" )

main()


# universe.add_entity( storytime.Actor( storytime.CoordR( [3, 3] ), start_time, features=[storytime.Feature.LIVING, storytime.Feature.FEMALE] ) )
