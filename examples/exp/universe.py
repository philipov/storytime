

"""
description
"""

from copy import deepcopy


from .utils import prepare_object

from collections import OrderedDict

#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------#

class Zone:
    """
    Associate points on a surface with physical location data
    construct a connectedness network between cells
    """

    def __init__( self,
                  surface = None,
                  cells: list = None
                ):

        self._surface       = prepare_object( surface,  )
        self._cells         = prepare_object( cells, list )


    def __str__( self ) :
        string  = "<Zone"
        string += " " + str( type(self._surface).__name__ )
        string += " " + str( len(self._cells) )
        string += ">"
        return string

    @property
    def __dprint__( self ) :
        string = str( self )
        string += "\n " + self._surface.__dprint__
        for cell in self._cells:
            string += "\n " + str(cell)
        return string

    def construct( self ) :
        pass

    def neighbors( self, cell_index, distance=1 ) -> list :
        neighbors = self
        return NotImplemented

    def find_path(self, source:int, destination:int, search_depth=None) -> list:
        path = self
        return NotImplemented


#####################


class HexMap(Zone):
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        super().__init__(self)



#----------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------#

# ToDo: Perform search operations using SQLLite in :memory:


class Universe :
    """Associate space with its content"""

    def __init__( self,
                  zone: Zone = None,
                  entities:list = None,
                  parameters:dict = None
                ) :

        self._zone          = prepare_object( zone, Zone )
        self._entities      = prepare_object( entities, list )
        self._parameters    = prepare_object( parameters, dict )
        self._created       = False


    #####################
    def create( self, now_time, start_time, physics ) :
        physics.initial_universe(self, now_time, start_time)
        self._created = True


    def tick( self, next_time ) :
        if not self._created:
            raise RuntimeError("Attempt to tick() Universe before create() was called")
        pass


    #####################
    @property
    def entities( self ) :
        for entity in self._entities :
            yield entity

    def find_entity( self, target_entity ) :
        for entity in self._entities :
            if entity == target_entity :
                return entity
        return None

    def add_entity( self, entity ) :
        self._entities.append( entity )
        # add to structured views


    #####################
    @property
    def __dprint__( self ) :
        string = self._zone.__dprint__
        return string

#----------------------------------------------------------------------------------------------#

class Spacetime:
    """
    data structure for representing space and time together
    1) state can beengine.actors.append(Character('alice')) viewed either as a slice of space in time,
        or as a slice of time for a space
    """

    def __init__( self,
                  start_time,
                  universe,

                 ):

        self._timeline = OrderedDict()
        self._timeline[start_time] = universe


#----------------------------------------------------------------------------------------------#
