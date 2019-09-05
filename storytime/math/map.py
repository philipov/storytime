# storytime.core.vmap

"""
voronoi tiles
"""

from powertools import AutoLogger
log = AutoLogger()
from powertools import yaml
##############################
from collections import namedtuple
from pathlib import Path

import deepgraph as dg

#----------------------------------------------------------------------------------------------#

class Vector2D(namedtuple('_Vector2D', ['x', 'y'])):
    def __hash__(self):
        return hash((self.x, self.y))

    def __add_(self, other):
        return Radvec2D(self.x + other.x, self.y + other.y)


##############################
class Radvec2D(namedtuple('_Radvec2D', ['radius', 'angle'])):
    def __hash__(self):
        return hash((self.radius, self.angle))

    def __add__(self, other):
        return Radvec2D(self.radius + other.radius, self.angle + other.angle)

##############################
VecBox = namedtuple('VecBoundary', ['min', 'max'])

#----------------------------------------------------------------------------------------------#

##############################
location_classes = dict()

def locationtype(cls):
    ''' decorator: register a location class for loading from yaml file '''

    global location_classes
    location_classes[cls.__name__] = cls
    return cls


##############################
@locationtype
class Location:
    ''' game data for a node in the vmap '''

    __slots__ = (
        'coord',
        'name',
    )
    def __init__(self,
        coord:  Vector2D,
        name:   str,
    ):
        self.coord  = coord
        self.name   = name

    @classmethod
    def from_data(cls, x, y, *args):
        ''' construct using yaml data '''
        return cls(Vector2D(x,y), *args)


#----------------------------------------------------------------------------------------------#

class Field:
    def __init__(self, *args, **kwargs):
        pass


##############################
class VorMap2D(Field):
    ''' 2D voronoi tiling
        immutable, update methods return a new instance
        line and vertex calculation
        adjacency matrix
        pathfinding
    '''
    __slots__ = (
        '_len_x',
        '_len_y',
        '_sites',
        '_matrix',
    )
    def __init__( self,
        len_x:int,
        len_y:int,
        *,
        sites:dict  = None,
    ):
        super().__init__()
        self._len_x     = len_x
        self._len_y     = len_y

        self._sites     = dict() if sites is None else sites
        self._matrix    = None


    ###############
    @classmethod
    def from_yaml(cls, filepath:Path):
        ''' load csv file containing sites'''

        data    = yaml.load(filepath)
        # print(yaml.yformat(data))
        len_x       = data['vmap']['len_x']
        len_y       = data['vmap']['len_y']
        site_type   = location_classes[data['sites']['type']]

        sites = dict()
        for row in data['sites']['data']:
            site = site_type.from_data(*row)
            sites[site.coord] = site

        return cls(len_x, len_y, sites=sites)

    ###############
    @property
    def sites(self):
        return self._sites.keys()

    @property
    def max_x(self):
        '''read-only'''
        return self._max_x

    @property
    def max_y(self):
        '''read-only'''
        return self._max_y

    ###############
    def __getitem__(self, coord:Vector2D):
        if coord in self._sites:
            return self._sites[coord]

    def add_sites(self, sites:dict ):
        new_self = type(self)(
            sites = { **self.sites, **sites },
            max_x = self.max_x,
            max_y = self.max_y,
        )


    ###############
    def new_site(self, coord, data=None):
        self._sites[coord] = data


##############################

#----------------------------------------------------------------------------------------------#
