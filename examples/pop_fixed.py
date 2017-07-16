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
    start_time  = storytime.GameTurn( 1, storytime.setting.Season.SUMMER )
    end_time    = storytime.GameTurn( 10, storytime.setting.Season.SUMMER )

    universe    = storytime.examples.sample_universe( 20, 10 )
    engine      = storytime.Engine( start_time, universe )

    ### main loop - fixed length

    tick_event = storytime.tick_controller( engine )

    storytime.loop_fixed( start_time, end_time, tick_event)

    ### end
    print( "### END Simulation" )

main( )
