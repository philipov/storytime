#-- storytime.modes

"""
callback functions implementing the action selected by the first command-line parameter.
"""

import logging
log = logging.getLogger( name="smash.modes" )
logging.basicConfig( level=logging.DEBUG )
# debug   = lambda *a, **b : log.debug( "".join( str( arg ) for arg in a ) )
# info    = lambda *a, **b : log.info(  "".join( str( arg ) for arg in a ) )
debug = print
info = print
# debug = lambda *a, **b : None

import sys
import os

from importlib import import_module

from .engine import Engine

#----------------------------------------------------------------------#


def do_run(target, *args, workdir, duration, **kwargs):
    info( "Run target in a loop until end" )

    sys.path.append(str(workdir) )
    os.chdir(str(workdir))

    info('-- do_run:', target, duration)

    app = import_module(str(target))
    app.engine.run(duration)



def do_play(target, *args, workdir, **kwargs ) :
    info( "Run target in interactive mode" )

    sys.path.append( str( workdir ) )
    os.chdir( str( workdir ) )


def __default__(*args, **kwargs):
    info( "Unknown Command", )




#----------------------------------------------------------------------#
