#-- storytime.setup

'''--- Storytime
'''

#----------------------------------------------------------------------------------------------#

from pathlib import Path
import os
def collect_package_data( package_path ) :
    root_path = Path( __file__ ).parents[1].resolve() / package_path
    package_data = list()

    for root, _, _ in os.walk( str( root_path ) ) :
        package_data.append( str( Path( root ) / '*' ) )

    return package_data


#----------------------------------------------------------------------------------------------#

options = dict(
    name            = 'storytime',
    version         = '0.1.0',
    description     = __doc__,
    license         = "MIT License",

    url             = 'https://github.com/philipov/storytime',
    author          = 'Philip Loguinov',
    author_email    = 'philipov@gmail.com',

    packages = [
        'storytime',
        'storytime.agent',
        'storytime.world',
    ],

    zip_safe                = True,
    include_package_data    = True,
    package_data = {
        'storytime' : collect_package_data( Path('storytime') )
    },
    entry_points = {
        'console_scripts': [
            'storytime  = storytime:console',
        ],
    },
    install_requires = [
        'powertools',
        'curio',
        'click',

        'numpy',
        'pandas',
        'scipy',
        'deepgraph',


    ],
)

__version__ = options['version']

#----------------------------------------------------------------------------------------------#
