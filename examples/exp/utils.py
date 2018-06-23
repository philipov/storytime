

'''
utilities
'''

#----------------------------------------------------------------------------------------------#

class Cache :
    """
    Defer evaluation until the first time the value is accessed
    Then store the value and return it on future access attempts
    Unless the condition callback evaluates to True, in which case recalculate
    """

    def __init__( self, key=None, value=None, update_method=None, condition=None ) :
        self._update_method = update_method
        self._condition = condition
        self._value = value
        if value is None :
            self._dirty = True
        else :
            self._dirty = False

    def dirty( self ) :
        self._dirty = True

    def clean( self ) :
        self._dirty = False

    @property
    def value( self ) :
        if self._dirty or self._condition is not None and self._condition( self ) :
            self._value = self._update_method( self._value )
            self.clean( )
        return self._value

class CacheArray( Cache ) :
    """Cache each element of an array"""
    pass

class CacheDict( Cache ) :
    """Cache a value for each key """
    pass
    #ToDo: This one can be used for GraphMatrix, key = (args, kwargs)

#----------------------------------------------------------------------------------------------#
### magic methods

def equality_of( self, other, key: tuple ) :
    """equal if keys exist and _function_tag values are equal"""

    assert self is not None
    assert other is not None
    assert key is not None
    assert key is not []

    is_equal = True
    for attribute_name in key :
        if not hasattr( self, attribute_name ) :
            raise TypeError( "__eq__: self is missing required _function_tag: " + attribute_name )
        if not hasattr( other, attribute_name ) :
            is_equal = False
        if getattr( self, attribute_name ) != getattr( other, attribute_name ) :
            is_equal = False
    return is_equal

#####################

def interface_of( self, other, attributes: tuple ) :
    """interface shared if attributes exist on both objects"""

    assert self is not None
    assert other is not None
    assert attributes is not None
    assert attributes is not []

    shares_interface = True
    for attribute_name in attributes :
        if not hasattr( self, attribute_name ) :
            raise TypeError( "__eq__: self is missing required interface attribute: " + attribute_name )
        if not hasattr( other, attribute_name ) :
            shares_interface = False
    return shares_interface

#----------------------------------------------------------------------------------------------#
### attribute assignment

import inspect
from copy import deepcopy as _deepcopy

def prepare_object( parameter, cls=object, deepcopy=False, args=None, **kwargs ) :
    """__init__ default object if None; strict type"""

    obj = None
    if parameter is None :                  # default object
        if args is None :
            args = list( )
        obj = cls( *args, **kwargs )
    # if isinstance(parameter, type):
    #     if args is None :
    #         args = list( )
    #     obj = parameter( *args, **kwargs )
    elif inspect.isclass( cls ) :
        if isinstance( parameter, cls ) :   # strict type
            if deepcopy :
                obj = _deepcopy( parameter )
            else :
                obj = parameter
        else :
            raise TypeError( "object parameter must be " + str( cls ) + ", or None: " + str( parameter ) )
    else :
        raise TypeError( "cls must be a class: " + str( cls ) )
    return obj

#####################

import numpy as np

def prepare_ndarray( parameter=None, dim: int = 0, **kwargs ) :
    """assign 1d ndarray. convert if list, initialize with shape=(dim,) if None"""

    vector = None
    if parameter is None :
        vector = np.zeros( dim )
    elif isinstance( parameter, list ) :
        vector = np.array( parameter, **kwargs )
    elif isinstance( parameter, np.ndarray ) :
        vector = parameter
    else :
        raise TypeError( "vector parameter must be list, ndarray, or None: " + str( parameter ) )

    if vector.ndim != 1 :
        raise ValueError( "vector must have ndim=1: " + str( vector ) )
    return vector

#####################

def append( target: np.ndarray, item ) :
    """append to numpy array"""
    return np.append( target, [item] )


#----------------------------------------------------------------------------------------------#
