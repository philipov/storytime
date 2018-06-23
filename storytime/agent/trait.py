# storytime.agent.trait

"""
"""

from powertools import AutoLogger
log = AutoLogger()
##############################


#----------------------------------------------------------------------------------------------#

class Trait:
    ''' a bundle of parameters and associated capabilities (methods)
        these form the language with which plans can be constructed
        prerequisite traits may be referenced by a derivative trait
        if a trait uses another trait's parameters,
            it should get the values for the agent it belongs to
    '''

    def __init__(self):
        pass

    actions         = []
    prerequisites   = []


#----------------------------------------------------------------------------------------------#
#   PHYSICAL

class Body(Trait):
    ''' '''
    ...

class Quickness(Trait):
    ''' '''
    ...

class Dexterity(Trait):
    ''' '''
    ...


##############################
class Creature(Trait):
    ''' basic stats for mobile creatures'''
    ...

class Living(Trait):
    ...

class Reproduction(Trait):
    ...


#----------------------------------------------------------------------------------------------#
#   MENTAL

class Willpower(Trait):
    ''' '''
    ...


class Perception(Trait):
    ''' '''
    ...


class Intelligence(Trait):
    ''' '''
    ...


##############################
class Thinking(Trait):
    ''' basic stats for thinking creatures '''
    ...

class Planning(Trait):
    ''' creating plans requires taking moves, and their complexity depends on the parameters'''
    ...


#----------------------------------------------------------------------------------------------#
#   SOCIAL


class Empathy(Trait):
    ''' '''
    ...


class Confidence(Trait):
    ''' '''
    ...


class Status(Trait):
    ''' '''
    ...


##############################
class Social(Trait):
    ''' basic stats for social creatures '''
    ...

class Family(Trait):
    ...

class Lifepath(Trait):
    '''  '''
    ...

#----------------------------------------------------------------------------------------------#
