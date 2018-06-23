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
###     start a game
##############################

def raise_sys_exit( ) :
    """Called inside interactive console to return to player_function"""
    raise SystemExit
extra_locals = { "exit" : raise_sys_exit }  # other locals go in here

def interactive_interpreter( local_vars:dict ) :
    """Enter the interactive interpreter"""

    local_vars.update(extra_locals)
    #try :
    code.interact( local=local_vars )
    #except SystemExit :
     #   pass


##############################
class CommandWord:
    def __init__(self, func):
        self.func = func
    def __repr__(self):
        self.func()
    def __str__(self):
        return f'<CommandWord {self.func.__name__}>'

def commandword(func):
    return CommandWord(func)


##############################
async def starter(auto):

    this        = await curio.current_task()

    engine      = Simulation(scenario.Test(), realtime=auto)
    timer       = await curio.spawn(engine.timer())

    ### quality-of-life
    @commandword
    def q():
        raise SystemExit

    ### spawn task to run python repl in a thread
    controller:curio.Task  = await curio.spawn(curio.run_in_thread(
        interactive_interpreter, {**globals(),**locals()}
    ))

    ### wait
    try:
        while True:
            await curio.sleep(10)
    except SystemExit:
        controller.join()


#----------------------------------------------------------------------------------------------#

@console.command( 'game' )
@click.argument( 'game_name',             default = 'game')
@click.option(   '-m', '--with_monitor',  default = False, is_flag=True)
@click.option(   '-a', '--auto',          default = False, is_flag=True)
@click.pass_obj
def game( outer_env, game_name, with_monitor, auto) :
    ''' create new boxtree instance in target directory using a root template
    '''

    curio.run(starter, auto,
        with_monitor = with_monitor,
    )


##############################
if __name__ == '__main__':
    console()


#----------------------------------------------------------------------------------------------#
