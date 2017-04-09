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
    start_time = storytime.Year( 0, storytime.Season.NULL )
    end_time = storytime.Year( 10, storytime.Season.WINTER )

    universe = storytime.examples.sample_universe( 20, 10 )

    ### main loop - fixed length

    tick_event = storytime.tick_controller( universe )

    storytime.loop_fixed( start_time, end_time, tick_event)

    ### end
    print( "### END Simulation" )

main( )
