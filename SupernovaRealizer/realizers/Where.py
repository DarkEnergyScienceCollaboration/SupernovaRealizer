'''
Created on Feb 11, 2013

@author: akim
'''

class Normal(object):
    '''
    classdocs
    '''
    # stupid implementation that puts things in a gaussian distribution around the host
    parameter_names = ["where.radius"]


    def __init__(self, pars):
        '''
        Constructor
        '''
        self.radius = pars['radius']

    def realize(self, random_state, coordinate):
        return (coordinate) + random_state.normal(scale=self.radius, size=2)
    
class Uniform(object):
    '''
    classdocs
    '''
    # stupid implementation that puts things in a gaussian distribution around the host
    parameter_names = ["where.ramin","where.ramax","where.decmin","where.decmax"]
    

    def __init__(self, pars):
        '''
        Constructor
        '''
        self.ramin=pars['ramin']
        self.ramax=pars['ramax']
        self.decmin=pars['decmin']
        self.decmin=pars['decmax']
        

    def realize(self, random_state):
        return (random_state.uniform(low=self.ramin,high=self.ramax, size=1),random_state.uniform(low=self.decmin,high=self.decmax, size=1))