# storytime.agent

""" agent performs speculative computation while it's not their turn
"""

from powertools import AutoLogger
log = AutoLogger()
##############################

import curio

#----------------------------------------------------------------------------------------------#

class Agent:
    ''' Agent.planner:
        each turn, receive sensory input and use it to pick an available move
        agents are composed of traits of various classes (physical, mental)
        traits are bundles of parameters and moves that can be used to form plans
        create/update beliefs based on the input. memories are a type of belief.
        use beliefs to form/modify plans out of available moves
        allocate resources to each plan based on current conditions
        execute the next step of the next plan in the priority queue

        The frequency with which Agent.planner is called depends on the Simulator.timer
    '''

    def __init__(self):
        self.traits     = dict()
        self.beliefs    = dict()
        self.plans      = dict()
        self.task       = None

    async def planner(self, prompter):
        self.task       = curio.current_task()

        while True:
            world = await prompter()
            await curio.sleep(0.1)

#----------------------------------------------------------------------------------------------#
