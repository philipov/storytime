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

#----------------------------------------------------------------------------------------------#

##############################
class Network:
    ''' 2D voronoi tiling
        immutable, update methods return a new instance
        line and vertex calculation
        adjacency matrix
        pathfinding
    '''
    __slots__ = (
        '_nodes',
        '_edges',
        '_matrix',
    )
    def __init__( self, *,
        nodes:dict = None,
        edges:list = None,
    ):
        self._nodes     = nodes if nodes is not None else dict()
        self._edges     = edges if edges is not None else list()

        self._matrix    = None


    ###############
    @classmethod
    def from_yaml(cls, name, filepath:Path):
        ''' load csv file containing sites'''

        data  = yaml.load(filepath)
        # print(yaml.yformat(data))
        edges = data[name]['edges']


        return cls(edges=edges)

    ###############
    @property
    def nodes(self):
        '''read-only'''
        return self._nodes

    @property
    def edges(self):
        '''read-only'''
        return self._edges



    ###############
    def __getitem__(self, id):
        if id in self._nodes:
            return self._nodes[id]


    ###############
    def new_site(self, id, node=None):
        self._nodes[id] = node


##############################

#----------------------------------------------------------------------------------------------#
