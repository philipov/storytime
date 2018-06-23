### examples/test1.py

""" prototype simulator
"""
from powertools import AutoLogger
log = AutoLogger()
from powertools import name
from powertools.print import listprint

####################
simtypes = dict()
def simtype( cls ):
    global sim
    simtypes[cls] = cls
    return cls


#----------------------------------------------------------------------------------------------#

@simtype
class Field:
    ''' continuous wave-like behavior
    '''


#----------------------------------------------------------------------------------------------#

@simtype
class Edge:
    ''' weight between nodes '''

    def __init__(self, source, destination, weight):
        self.source         = source
        self.destination    = destination
        self.weight         = weight


@simtype
class Network:
    ''' discrete wave-like behavior
    '''

    def __init__( self, *,
        nodes = None,
        edges = None
    ):
        self.nodes      = list() if nodes is None else nodes
        self.edges      = list() if edges is None else edges
        self.matrix     = None



#----------------------------------------------------------------------------------------------#

####################
@simtype
class Entity:
    ''' discrete particle-like behavior
    '''
    def __init__(self, id, *,
                 fields:dict    = None,
                 edges:dict     = None,
                 parents:dict   = None,

                 ):
        self.id         = id

        self.fields     = dict() if fields is None else fields
        self.edges      = dict() if edges is None else edges
        self.parents    = dict() if parents is None else parents

    def __repr__(self):
        return f'<{name(self)} id={self.id}>'


#----------------------------------------------------------------------------------------------#

####################
@simtype
class Location(Entity):
    '''
    '''

@simtype
class Star(Location):
    '''
    '''

@simtype
class Planet(Location):
    '''
    '''


class Zone(Entity):
    ''' contains locations
    '''

#----------------------------------------------------------------------------------------------#


@simtype
class Plant(Entity):
    '''
    '''

####################
@simtype
class Creature(Entity):
    '''
    '''

@simtype
class Person(Entity):
    '''
    '''

@simtype
class Group(Entity):
    '''
    '''

####################
@simtype
class Ideal(Entity):
    '''
    '''

####################
class Resource(Field):
    '''
    '''

@simtype
class Item(Entity):
    '''
    '''

@simtype
class Structure(Item, Location):
    '''
    '''


####################
@simtype
class Event(Entity):
    '''
    '''



#----------------------------------------------------------------------------------------------#

def id_number(init=0):
    while True:
        yield init
        init += 1

def random_person(seed) -> Person:
    return Person(id=next(seed))


####################
class Simulation:
    ''' top conatiner for simulation state
        define initial conditions

    '''

    class EntityIdExists(Exception):
        ''' entity.id must be unique
        '''


    ########################################
    def __init__(self, *,
                 entities:dict = None
                 ):

        self.entities   = dict() if entities is None else entities

        init            = max(i for i in self.entities.keys()) \
                            if   len(self.entities) > 0 \
                            else 0
        self.seed       = id_number(init)

        self.people     = [entity for entity in self.entities.values()
                            if isinstance(entity, Person)
                          ]
        self.locations  = [entity for entity in self.entities.values()
                            if isinstance(entity, Location)
                          ]


    ########################################
    def insert(self, entity:Entity):
        if entity.id in self.entities:
            raise Simulation.EntityIdExists(entity)

        self.entities[entity.id] = entity
        if isinstance(entity, Person):      self.people.append(entity)
        if isinstance(entity, Location):    self.locations.append(entity)


####################

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

class View:
    ''' a frame of limited information about the simulation, to be displayed to the user
    '''


class PopulationView(View):
    def __init__(self, people:list):
        self.people = people

    def display(self):
        print('PopulationView:')
        listprint(self.people)
        print('---------------')


#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

class Controller:
    ''' controller interface specification
    '''

    def __init__(self, simulation):
        self.simulation = simulation

    def look(self, target = None) -> View:
        raise NotImplementedError


####################
class PlayerController(Controller):
    ''' user interface
    '''

    def look(self, target = None) -> View:
        raise NotImplementedError


####################
class GameController(Controller):
    '''
    '''

    def look(self, target = None) -> View:
        raise NotImplementedError


####################
class GnController(Controller):
    '''
    '''

    def look(self, target = None):
        PopulationView(self.simulation.people).display()

        person = random_person(self.simulation.seed)
        self.simulation.insert(person)



####################

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

def garden_of_eden() -> Simulation:
    ''' initial condition
    '''

    locations = dict()
    return Simulation( entities = locations )


####################
def flat_zone(x, y) -> Simulation:
    ''' initial condition
    '''

    locations = dict()
    return Simulation( entities = locations )


####################
def round_planet(radius) -> Simulation:
    ''' initial condition
    '''

    locations = dict()
    return Simulation(entities = locations)


####################
if __name__ == '__main__':
    sim = flat_zone(10, 10)
    gn  = GnController(sim)
