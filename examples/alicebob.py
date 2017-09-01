
"""
alice and bob
"""

import storytime


universe  = storytime.Engine( )

class Character(storytime.Actor) :
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)


universe.actors.append( Character( 'Alice' ) )
universe.actors.append( Character( 'Bob' ) )


@universe.zone
class World(storytime.HexMap):
    pass
