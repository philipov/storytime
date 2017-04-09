#!/Anaconda3/python
# storytime

"""
description
"""

from copy import deepcopy

from .meta import equality_of
from .meta import prepare_ndarray
from .meta import prepare_object

#----------------------------------------------------------------------#

#----------------------------------------------------------------------#

from .actors import Entity
class Location(Entity) :
    """
    Encapsulates game logic and data related to cells of a zone
    A zone is nested if its locations contain a zone inside them,
    such as a universe containing star systems and planets
    """

    def __init__( self,
                  index: int,
                  # coord: CoordR = None,
                  properties: dict = None,
                  ) :
        assert index is not None
        self.index = index
        self.properties = prepare_object(properties, dict)


#----------------------------------------------------------------------#

from .spatial.surfaces import Surface

class Zone:
    """
    Associate points on a surface with physical location data
    construct a connectedness network between cells
    """

    def __init__( self,
                  surface: Surface = None,
                  cells: list = None
                  ) :

        self._surface    = surface
        self._cells      = prepare_object( cells, list )


    def __str__( self ) :
        return NotImplemented

    def construct( self ) :
        pass

    def neighbors( self, cell_index, distance=1 ) -> list :
        neighbors = self
        return NotImplemented

    def find_path(self, source:int, destination:int, search_depth=None) -> list:
        path = self
        return NotImplemented

    def __dprint__(self):
        string  = str(self)
        string += self._surface.__dprint__( )



#####################

from .spatial.surfaces import SurfacePlane

class ZoneMap( Zone ):

    def __init__( self,
                  radius=None,
                  size_x=0, size_y=0,
                  surface: SurfacePlane = None,
                  cells: list = None
                  ) :
        super( ).__init__( surface, cells )


class Layers( Zone ) :
    pass





#####################

from .spatial.surfaces import SurfaceSphere2
from .spatial.projections import waterman
from .spatial.transformations import Transformer

class Planet( Zone ):
    """A planet with oceans and tectonic motion"""

    def __init__( self,
                  radius = None,
                  surface: SurfaceSphere2 = None,
                  transformer: Transformer = None,
                  cells: list = None
                  ) :
        super().__init__( surface, cells )

        self.cells  = prepare_object( cells, list )


        self._transformer = prepare_object(transformer, )

    @property
    def radius(self):
        return self._surface._extent

    def __str__( self ) :
        pass


    def construct( self ) :
        pass


#####################

class Orbit(Zone):
    pass


class StarSystem(Orbit):
    pass


class Galaxy(Orbit):
    pass


#----------------------------------------------------------------------#

#----------------------------------------------------------------------#

# ToDo: Perform search operations using SQLLite in :memory:

from .time import Year
from .actors import Population
from .actors import Entity


class Universe :
    """top-level control collection"""

    def __init__( self,
                  gametime: Year = None,
                  zone: Zone = None,
                  zone_class=Zone,
                  entities: list = None,
                  population: Population = None
                  ) :


        assert issubclass( zone_class, Zone )
        self._zone          = prepare_object( zone, zone_class )
        self._entities      = prepare_object( entities, list )

        self.gametime = prepare_object( gametime, Year )


    def add_entity( self, entity ) :
        self._entities.append( entity )
        # add to structured views

    def find_entity(self, target_entity:Entity ):
        for entity in self._entities:
            if entity == target_entity:
                return entity

    @property
    def entities( self ) :
        for entity in self._entities:
            yield entity

    def tick_time( self, next_time, history ) :
        pass


    def str_terrain(self):
        string = self._zone.__dprint__( )
        return string


#####################

class Timeline:
    pass


#####################

class Spacetime(Timeline):
    """
    data structure for representing space and time together
    1) state can be viewed either as a slice of space in time,
        or as a slice of time for a space
    """


    variable = "Hello"

    def __init__(self, universe:Universe, parameters=None):
        self._timeline = [ universe ]
        self._parameters = prepare_object(parameters, dict)


    def trace_entity(self, entity):
        """list of states of the entity over time"""
        entity = self
        return NotImplemented

    def now(self):
        return self._timeline[0]

    def step_time(self, *args, **kwargs):
        new_universe = deepcopy(self._timeline[0])
        new_universe.tick_time(*args, **kwargs)
        self._timeline.append(new_universe)


    def distance(self, source, destination):
        distance = self
        return NotImplemented



#----------------------------------------------------------------------#
