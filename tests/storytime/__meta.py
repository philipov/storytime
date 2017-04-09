#!/Anaconda3/python
# storytime

'''
description
'''


#----------------------------------------------------------------------#

from storytime.meta import IdGenerator
def test__IDGenerator( ):
    gen = IdGenerator()
    for count in gen :
        print("count: ", count)
        if count > 5:
            break
    # assert False

#----------------------------------------------------------------------#

from storytime.meta import introspective2
def test__introspective_function( ):

    @introspective2
    def some_func(me:Function, arg1:str):
        print( "annot", me.__inner__.__annotations__ )

        print( "me", me )
        assert me.monkey == "monkey"

        return arg1

    some_func.monkey = "monkey"

    print( "local", some_func )
    assert some_func("arg1") == "arg1"

    # assert False

from storytime.meta import introspective
def test__introspective2_function( ) :

    @introspective
    def some_func( me:Function, arg1: str ) :
        print( "annot", me.__annotations__ )

        print( "me", me )
        assert me.monkey == "monkey"

        return arg1

    some_func.__inner__.monkey = "monkey"

    print( "local", str( some_func ) )
    assert some_func( "arg1" ) == "arg1"

    # assert False


from storytime.meta import introspectivemethod
def test__introspective_method( ) :

    class some_cls:
        def __init__(self):
            self.attr0 = "attr0"

        @introspectivemethod
        def some_meth( self, me:Function, arg1:str ) :
            print( "annot", me.__annotations__ )

            print( "me", me )
            assert me.monkey == "monkey"

            print( "self", self )
            assert self.attr0 == "attr0"

            return arg1

    obj = some_cls()
    obj.some_meth.__func__.__inner__.monkey = "monkey"

    print( "local", str( obj.some_meth ) )
    assert obj.some_meth( "arg1" ) == "arg1"

    # assert False


#----------------------------------------------------------------------#

from storytime.meta import profile
from time import sleep
def test__profile():

    @profile
    def func1():
        sleep(0.03)

    @profile
    def func2( ) :
        sleep( 0.01 )

    class Class0:
        @profile
        def some_meth(self):
            sleep(0.02)


    func1()
    func2()
    c = Class0()
    c.some_meth()


    print("func", str(dir(c.some_meth)))
    # print( c.some_meth.__class__)

    print( profile.report( ) )
    assert profile.time( func1 ) == 0.03
    assert profile.time( func2 ) == 0.01
    assert profile.time( c.some_meth ) == 0.02

    # assert False

#----------------------------------------------------------------------#

from sympy import symbols
from sympy import Function
from sympy import integrate
from sympy import exp
from sympy import sin
from sympy import cos


def test__profile_sympy( ) :
    x, y, z, t = symbols( 'x y z t' )
    k, m, n = symbols( 'k m n', integer=True )
    f, g, h = symbols( 'f g h', cls=Function )
    integral = None

    profile.reset()
    profile.tag_start("integrate")

    # ToDo: turn this back on when relative load decreases (total pytest time increases)
    # integral = integrate( exp( x ) * sin( x ) + exp( x ) * cos( x ), x )

    profile.tag_stop("integrate")
    print( profile.report( ) )
    print("Integral:", integral)

    # assert False

#----------------------------------------------------------------------#
