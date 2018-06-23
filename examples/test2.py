### examples/test1.py

""" prototype simulator
"""
from powertools import AutoLogger
log = AutoLogger()
from powertools import name
from powertools.print import listprint, pprint
from powertools import term

from pathlib import Path

import storytime

#----------------------------------------------------------------------------------------------#

def test_vmap0():
    print(__file__)
    filename    = Path(__file__).resolve().parents[1]/'tests'/'testdata'/'vmaps'/'sites0.yaml'
    vmap        = storytime.VMap2D.from_yaml(filename)



####################
if __name__ == '__main__':
    test_vmap0()


#----------------------------------------------------------------------------------------------#
