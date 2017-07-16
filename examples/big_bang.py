#!/Anaconda3/python
# storytime

"""
description
"""

import storytime
import storytime.examples

#----------------------------------------------------------------------#

class FantasySphere( storytime.PhysicalLaws ) :
    """callbacks for physical process"""

    def __init__( self ) :
        self.total_energy = 100000
        self.continent_energy = 14000
        self.cell_energy = 100

        self.initial_radius = 1
        self.gravitational_constant = 10

    #####################
    def initial_universe( self, universe, now_time, start_time ) :
        pass

    def tick_universe( self, universe, now_time, next_time ) :
        pass

    #####################
    def initial_planet( self, planet, now_time, start_time ) :
        pass

    def tick_planet( self, planet, now_time, next_time ) :
        pass

    #####################
    def initial_zonemap( self, zonemap, now_time, start_time, projection_of=None ) :
        pass

    def tick_zonemap( self, zonemap, now_time, next_time ) :
        pass

    #####################
    def initial_entities( self, universe, now_time, start_time ) :
        pass

    def tick_entities( self, universe, now_time, next_time ) :
        pass


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
