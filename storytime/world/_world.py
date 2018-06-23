# storytime.core.vmap

"""
voronoi tiles
"""

from powertools import AutoLogger
log = AutoLogger()
##############################

#----------------------------------------------------------------------------------------------#

class World:
    ''' game controller
        progress the state one tick
    '''

    def __init__(self, name:str = None):
        self.name   = name
        self.tiles  = None


#----------------------------------------------------------------------------------------------#
