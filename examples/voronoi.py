#!/Anaconda3/python
# storytime

"""
description
"""

# import storytime

#----------------------------------------------------------------------#
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

import numpy as np

from scipy.spatial import Voronoi, voronoi_plot_2d
# import shapely.geometry
# import shapely.ops


def main():
    points = np.random.random( (10, 2) )
    vor = Voronoi( points )
    print("A")
    voronoi_plot_2d( vor )
    print("B")
    matplotlib.pyplot.show( )
# simulation = storytime.Engine()

#----------------------------------------------------------------------#

main()
