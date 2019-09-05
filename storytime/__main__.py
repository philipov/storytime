#-- storytime.__main__

'''
application entry point
'''


from powertools import AutoLogger
log = AutoLogger()
##############################
from powertools import term
from powertools import click
from powertools.print import pprint

import os
from pathlib import Path
from collections import namedtuple

import code
import curio
import curio.monitor

from .__setup__ import __version__
from .simulation import Simulation
from . import scenario


#----------------------------------------------------------------------------------------------#

term.init_color()

CONTEXT_SETTINGS = dict(
    help_option_names   = ['-h', '--help'],
    terminal_width      = 97,
    max_content_width   = 97,
    color               = True
)


##############################
@click.group(               'storytime',
    context_settings        = CONTEXT_SETTINGS,
    cls                     = click.Group
)
@click.version_option(
    __version__,
    '--version', '-V',
    prog_name = 'storytime'
)
@click.option(
    '--verbose', '-v',
    default = False,
    is_flag = True,
    help    = 'Display additional logging information.'
)
@click.contextmanager
def console( verbose ) :
    ''' storytime console interface
    '''
    if verbose:
        log.setDebug()

    log.print( term.cyan( '\n~~~~~~~~~~~~~~~~~~~~ ' ), term.pink( 'STORYTIME') )
    log.print( 'SCRIPT:  ', __file__ )
    cwd = Path( os.getcwd() )
    log.print( 'WORKDIR: ', cwd, '\n' )

    result = yield

    log.print( '\n', term.pink( '~~~~~~~~~~~~~~~~~~~~' ), term.cyan(' DONE'), '.' )


#----------------------------------------------------------------------------------------------#

@console.command( 'run' )
@click.argument( 'game_name',             default = 'game')
@click.option(   '-m', '--with_monitor',  default = False, is_flag=True)
@click.option(   '-a', '--auto',          default = False, is_flag=True)
@click.pass_obj
def run( outer_env, game_name, with_monitor, auto) :
    '''
    '''
    from .starter import starter
    curio.run(starter, auto,
        with_monitor = with_monitor,
    )


@console.command( 'make' )
@click.argument( 'game_name',             default = 'game')
@click.pass_obj
def make( outer_env, game_name, with_monitor, auto) :
    '''
    '''



##############################
if __name__ == '__main__':
    console()


#----------------------------------------------------------------------------------------------#
