#!/Anaconda3/python
# storytime

'''
description
'''

import numpy as np

from storytime.out import dprint
from copy import deepcopy


#----------------------------------------------------------------------#

from storytime.spatial.surfaces import Coord
def test__Coord( ) :
    coord = Coord( )


#####################

from storytime.spatial.surfaces import CoordR
def test__CoordR( ) :
    coord = CoordR( )
    coord0 = CoordR( [0, 0] )
    coord1 = CoordR( np.array( [0, 0] ) )
    coord2 = CoordR( np.array( [1, 0] ) )
    coord3 = CoordR( np.array( [1, 1] ) )

    print( "O: ", coord1 )
    print( "A: ", coord2 )
    print( "B: ", coord3 )

    print( "OA:", coord1 - coord2 )
    print( "OB:", coord1 - coord3 )
    print( "AB:", coord2 - coord3 )
    print( "BA:", coord3 - coord2 )

    # assert False


#####################

from storytime.spatial.surfaces import CoordS2
def test__CoordS2( ) :
    coord = CoordS2( )
    coord0 = CoordS2( shape=1, index=0 )
    coord1 = CoordS2( shape=3, index=1 )
    coord2 = CoordS2( np.array( [0, 0] ), index=2 )
    coord3 = CoordS2( np.array( [90, 0] ), radius=0, index=3 )
    coord4 = CoordS2( np.array( [90, 90] ), radius=10, center=coord3, index=4 )
    coord5 = CoordS2( [90, 90], radius=10)

    print( " : ", coord )
    print( "0: ", coord0 )
    print( "1: ", coord1 )
    print( "2: ", coord2 )
    print( "3: ", coord3 )
    print( "4: ", coord4 )

    assert str( coord )  == "<s2 [0.0 0.0]>"
    assert str( coord0 ) == "<s1 [0.0]>"
    assert str( coord1 ) == "<s3 [0.0 0.0 0.0]>"
    assert str( coord2 ) == "<s2 [0 0]>"
    assert str( coord3 ) == "<s2 [90 0] r=0>"
    assert str( coord4 ) == "<s2 [90 90] r=10| [S2 3]>"

    # assert False


from storytime.spatial.surfaces import metric_sphere2
def test__metric_sphere2():

    # Radius of the earth in km (GRS 80-Ellipsoid)
    EARTH_RADIUS = 6371.007176

    # Example lat-long
    coordinates_dict = dict()
    coordinates_dict['A'] = [41.3111, -72.9267]
    coordinates_dict['B'] = [37.5664, 126.939]
    coordinates_dict['C'] = [43.7731, -79.5036]
    coordinates_dict['D'] = [24.9697, 121.267]
    coordinates_dict['E'] = [30.2636, 120.121]
    coordinates_dict['F'] = [30.4752, 114.394]

    # ndarray([ [x0,y0], [x1,y1], ... ])
    coordinates_array = np.array( [(val[0], val[1]) for key, val in coordinates_dict.items( )] )

    distance_array = metric_sphere2( coordinates_array, EARTH_RADIUS )
    print(distance_array)

    # assert False


#----------------------------------------------------------------------#

from storytime.spatial.surfaces import Surface
class __Surface :

    def prepare_surface0(self) -> Surface:
        surface = deepcopy(self.surface)
        sites = deepcopy( self.sites )
        surface.site_add( *sites )
        return surface

    #####################
    def test__Create(self):

        surface = self.prepare_surface0( )
        dprint(surface)
        distance_array = surface.distance_matrix()
        print(distance_array)

        # assert not self.debug

    def test__Voronoi(self):
        surface = self.prepare_surface0( )

        # assert not self.debug

#####################
    surface = Surface()
    sites = [
        Coord()
    ]
    debug = True


from storytime.spatial.surfaces import SurfacePlane
class __SurfacePlane( __Surface ) :
    surface = SurfacePlane(10,10)
    sites = [
        CoordR([0, 0])
    ,   CoordR([5, 0])
    ,   CoordR([3, 4])
    ]
    debug = True


from storytime.spatial.surfaces import SurfaceSphere2
class __SurfaceSphere2( __Surface ) :
    surface = SurfaceSphere2(1)
    sites = [
        CoordS2([45, 90])
    ,   CoordS2([45, 91])
    ]
    debug = True


#----------------------------------------------------------------------#
