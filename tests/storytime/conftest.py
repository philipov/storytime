#-- conftest.storytime

"""
fixtures for module unit tests
"""

import pytest
import time
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('conftest.storytime')


#----------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------#


@pytest.fixture( scope="session" )
def path_vmaps( path_testdata ) :
    return path_testdata/'vmap'

@pytest.fixture( scope="session" )
def path_sites0( path_vmaps ) :
    return path_vmaps/'sites0'


#----------------------------------------------------------------------------------------------#
