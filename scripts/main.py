#!/Anaconda3/python
# storytime

"""
description
"""

import storytime
import storytime.examples

#----------------------------------------------------------------------#

def main( ) :
    ### begin
    print( "### BEGIN Simulation" )

    ### __init__ universe
    start_time  = storytime.Year( 0, storytime.Season.NULL )
    end_time    = storytime.Year( 10, storytime.Season.SUMMER )

    universe    = storytime.examples.sample_universe( 20, 10 )

    ### main loop - with player events

    tick_event      = storytime.tick_controller( universe )
    player_event    = storytime.player_controller( universe )

    storytime.loop_interactive( start_time, tick_event, player_event )

    ### end
    print( "### END Simulation" )

main()
