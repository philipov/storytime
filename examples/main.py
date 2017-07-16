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

    ### main loop - with player events

    tick_event      = storytime.tick_controller( engine )
    player_event    = storytime.player_controller( engine )

    storytime.loop_interactive( start_time, tick_event, player_event )

    ### end
    print( "### END Simulation" )

main()
