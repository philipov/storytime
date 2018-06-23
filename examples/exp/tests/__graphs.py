#!/Anaconda3/python
# storytime

'''
description
'''

import numpy as np

from storytime.out import dprint
from copy import deepcopy


#----------------------------------------------------------------------------------------------#

from storytime.graphs import Edge
from storytime.graphs import __EdgeColor as EdgeColor

def test__Edge( ) :
    edge0 = Edge( 0, 0 )
    edge1 = Edge( 1, 3, 4, EdgeColor.RED )

    print( edge0 )
    print( edge1 )

    # assert False

#----------------------------------------------------------------------------------------------#

from storytime.graphs import Node

def test__Node( ) :
    node0 = Node( 0 )
    node1 = Node( 1, 5 )
    node1.add_edge( Edge( 1, 0 ) )

    print( node0 )
    print( node1 )

    # assert False


#----------------------------------------------------------------------------------------------#

from storytime.graphs import Network
from storytime.graphs import GraphMatrix

class __Graphs :

    def prepare_network0( self ):
        """test network"""

        network = deepcopy( self.network )
        network.add_node( 0 )
        network.add_node( 1 )
        network.add_edge( Edge( 1, 0, 5, EdgeColor.GREEN ) )
        network.add_edge( Edge( 0, 1, 1, EdgeColor.GREEN ) )
        network.add_edge( Edge( 0, 1, 1 ) )
        return network

    #####################
    def test__Network(self):

        network = self.prepare_network0( )
        print( str(network) +"\n")
        dprint( network )

        print("\nselect_edges")
        dprint( list( network.edges( EdgeColor.GREEN ) ) )

        # assert not self.debug

    def test__GraphMatrix( self ) :

        network = self.prepare_network0( )
        print(network,"\n")

        matrix0 = GraphMatrix( )
        print( "0:\n" + str( matrix0.toarray() ) + "\n" )

        matrix1 = GraphMatrix( network ) # all edges
        print( "1:\n" + str( matrix1.toarray( ) ) + "\n" )

        network.add_node( 2 )
        network.add_edge( Edge( 2, 1, 1, EdgeColor.GREEN ) )

        matrix1 = GraphMatrix( network )            # all edges
        matrix2 = GraphMatrix( network, [None] )    # select edges with color==None
        matrix3 = GraphMatrix( network, [EdgeColor.GREEN] )
        matrix4 = GraphMatrix( network.edges( EdgeColor.GREEN ), network.count_nodes( ) )

        print( "1:\n" + str( matrix1.toarray() ) + "\n" )
        print( "2:\n" + str( matrix2.toarray() ) + "\n" )
        print( "3:\n" + str( matrix3.toarray() ) + "\n" )
        print( "4:\n" + str( matrix4.toarray() ) + "\n" )

        assert not np.array_equal( matrix1.toarray( ), matrix2.toarray( ) )
        assert np.array_equal( matrix3.toarray(), matrix4.toarray() )

        dprint(matrix2)

        # assert not self.debug


    #####################
    def prepare_network1( self ) :
        """test matrix"""

        network = deepcopy( self.network )
        network.add_node( 0 )
        network.add_node( 1 )
        network.add_node( 2 )
        network.add_node( 3 )
        network.add_node( 4 )
        network.add_node( 5 )
        network.add_edge( Edge( 0, 1 ) )
        network.add_edge( Edge( 1, 0, -1 ) )
        network.add_edge( Edge( 2, 3 ) )
        network.add_edge( Edge( 3, 2 ) )
        network.add_edge( Edge( 4, 2 ) )
        network.add_edge( Edge( 2, 5 ) )

        return network

    #####################
    def test__GraphMatrix_connection(self):

        network=  self.prepare_network1()
        dprint(network)

        matrix = GraphMatrix( network )
        print( "\n0:\n" + str( matrix.toarray( ) ) + "\n" )
        dprint(matrix)

        (n,labels) = matrix.connected_components()
        print(n, labels, "\n")

        distance_matrix = matrix.distance_matrix( )
        print( distance_matrix )

        # assert not self.debug

#####################

    network = Network( )
    debug = True


class __Graphs_symmetric( __Graphs ) :
    network = Network( symmetry = 1)
    debug = True


class __Graphs_antisymmetric( __Graphs ) :
    network = Network( symmetry = -1 )
    debug = True


#----------------------------------------------------------------------------------------------#

from storytime.graphs import BKTree
def test__BKTree():
    def subtraction(a:int,b:int) -> int:
        return a-b
    tree = BKTree(subtraction)

    tree.add( 1 )
    tree.add( 1 )
    tree.add( 1 )
    tree.add( 2 )
    tree.add( 2 )
    tree.add( 3 )
    tree.add( 4 )

    print( tree.search( 4, 1 ) )
    print( tree.search( 4, 2 ) )
    # assert False


#----------------------------------------------------------------------------------------------#
