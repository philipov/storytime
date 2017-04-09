#!/Anaconda3/python
# storytime

"""
description
"""


from enum import Enum
from enum import unique

from copy import deepcopy

from .meta import equality_of


#----------------------------------------------------------------------#
# Time data types

@unique
class Cycle( Enum ) :
    """Base class for cyclic enumerations"""

    # ToDo: Make member values represent phase weight instead of phase position
    def __next__(self):
        members = type( self ).__members__      # __members__ is an ordered dict
        for (name, member) in members.items() :
            if member.value > self.value:
                return type(self)(member.value)
        return type( self )( 1 )

    @classmethod
    def __len__(cls):
        length = len(list(cls.__members__.values()))
        return length

    @classmethod
    def phase_length(cls):
        length = len(cls) - 1
        return length

    @property
    def is_last( self ) :
        last_phase = list( type( self ).__members__.values( ) )[-1]
        return self == last_phase


class __Season( Cycle ) :
    NULL = 0
    WINTER = 1
    SUMMER = 2


class __Turn( Cycle ) :
    NULL = 0
    DEAL = 1
    BET = 10
    DRAW = 20




#----------------------------------------------------------------------#

class Year :
    """
    Year( )             - 1 turn = 1 year, no phases
    Year( year )        - begin on given year, no phases
    Year( phase )       - 1 turn == 1 phase
    Year( year, phase ) - begin on given year and phase
    """

    # ToDo: Eras

    def __init__( self, arg1=None, arg2=None) :
        self.turn = 0
        self.stop_iteration = False

        # polymorphic parametrization
        if arg2 is None:
            if arg1 is None:                # ( )
                self.year=0
                self.phase=None
            else:
                if isinstance(arg1, Enum):  # ( phase )
                    self.year   = 0
                    self.phase  = arg1
                else:                       # ( year )
                    self.year = arg1
                    self.phase = None
        else:                               # ( year, phase )
            self.year = arg1
            self.phase = arg2


    def __eq__( self, other ) :
        if self.phase is None or other.phase is None:
            if self.phase is not None or other.phase is not None :
                raise TypeError("Cycle only set on one side: " + str(self) +", "+ str(other))
        elif type(self.phase) != type(other.phase):
            raise TypeError("Cycle types don't match: " + str(self) +", "+ str(other))

        primary_key = ("year", "phase")
        return equality_of(self, other, primary_key )


    def __str__( self ) :
        string = "<"
        string += "[" + str( self.turn ) + "] "
        if self.phase is not None:
            string += str( self.phase.name.title() + " " )
        string += str( self.year )

        string += ">"
        return string


    def __iter__( self ) :
        return self

    def __next__( self ) :
        if self.stop_iteration is True :
            raise StopIteration
        if self.phase is not None:
            if self.phase.is_last:
                self.year += 1
            self.phase = next(self.phase)
        elif self.phase is None:
            self.year += 1

        self.turn += 1
        return str( self )


    def __add__( self ) :
        pass

    def __sub__(self, other):
        pass

    def stop( self ) :
        self.stop_iteration = True


    def next( self ) :
        next_turn = deepcopy(self)
        next_turn.next( )

        return next_turn


#----------------------------------------------------------------------#

class Calendar:
    pass


#----------------------------------------------------------------------#

class CalendarScaling(Calendar) :
    pass


#----------------------------------------------------------------------#

class GameTime :
    pass

#----------------------------------------------------------------------#

class Turn :
    pass

#----------------------------------------------------------------------#
