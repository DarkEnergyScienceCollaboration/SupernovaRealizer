'''
Created on Jan 19, 2013

@author: akim
'''

import numpy
import TabularSED
import Sources

class RealizerContainer(object):
    def __init__(self, realizer, galaxy):
        self.random_state = numpy.random.RandomState(realizer.seed + galaxy.id)

        self.realizer = realizer
        self.galaxy = galaxy
        self.nsn = self.realizer.when.number(self.random_state, self.galaxy)
        self.index = 0
        
    def __iter__(self):
        self.index = 0
        return self

    def next(self):
        if self.index >= self.nsn:
            raise StopIteration
        else:
            self.index += 1           
            (ra, dec) = self.realizer.where.realize(self.random_state, self.galaxy)
            redshift = self.galaxy.redshift
            doe = self.realizer.when.realize(self.random_state, self.galaxy)
            model = self.realizer.what
            name = self.galaxy.id + self.index
            return Sources.Supernova(ra, dec, redshift, doe, model, name)

class Realizer(object):
    '''
    classdocs
    '''
    parameter_names = ['seed']

    def __init__(self, seed, sim_start, sim_end, radius, sedname):
        
        '''
        Constructor
        '''
        self.seed = seed
        self.sim_start = sim_start
        self.sim_end = sim_end
        self.radius=radius
        self.sedname = 'data/snflux_1a.dat'
         
        self.when = When(self.sim_start, self.sim_end)
        self.where = Where(self.radius)
        self.what = TabularSED.TabularSED(self.sedname)
        
    def realize(self, galaxy):
        
        return RealizerContainer(self, galaxy)


class When(object):
    '''
    classdocs
    '''
    parameter_names = ['sim_start', 'sim_end']
    rate = 1000. / 100. / 365.25  # 1 per century

    def __init__(self, sim_start, sim_end):
        '''
        Constructor
        '''
        self.sim_start = sim_start
        self.sim_end = sim_end
        
    def number(self, random_state, galaxy):
        
        expected = When.rate * (self.sim_end - self.sim_start) / (1 + galaxy.redshift)
        
        # calculate the number of explosions in the time period
        return random_state.poisson(expected)

    def realize(self, random_state, galaxy):
        
        # calculate the number of explosions in the time period
        return random_state.uniform(low=self.sim_start, high=self.sim_end)


class Where(object):
    '''
    classdocs
    '''
    # stupid implementation that puts things in a gaussian distribution around the host
    parameter_names = ["radius"]


    def __init__(self, radius):
        '''
        Constructor
        '''
        self.radius=radius
        
    def realize(self, random_state, galaxy):
        return (galaxy.ra, galaxy.dec)+random_state.normal(scale=self.radius,size=2)
