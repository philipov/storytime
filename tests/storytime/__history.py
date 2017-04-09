#!/Anaconda3/python
# storytime

'''
description
'''


#----------------------------------------------------------------------#

from storytime.history import ThemeHandler
from storytime.history import __Theme as Theme

def test__Theme( ):
    theme = Theme.NULL

    theme_h = ThemeHandler( 1 )
    assert theme_h.value == 1


#----------------------------------------------------------------------#

from storytime.history import Event
def test__Event( ) :
    event = Event( Theme.HUNGER )


#----------------------------------------------------------------------#

from storytime.history import History
def test__History( ) :
    history = History( )


#----------------------------------------------------------------------#
