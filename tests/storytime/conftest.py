#!/Anaconda3/python
# storytime

'''
description
'''

import pytest

#----------------------------------------------------------------------#

from storytime.examples import sample_universe

@pytest.fixture
def universe( ) :
    return sample_universe( 20, 10 )
