'''
Created on Jan 19, 2013

@author: akim
'''

import Sources
import TabularSED
import numpy

name='ByHost'

class RealizerContainer(object):
    def __init__(self, realizer, galaxy):
        self.random_state = numpy.random.RandomState([realizer.seed, galaxy.id])

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
            (ra, dec) = self.realizer.where.realize(self.random_state,self.galaxy)
            redshift = self.galaxy.redshift
            doe = self.realizer.when.realize(self.random_state, self.galaxy)
            model = self.realizer.what
            nm = (self.galaxy.id, self.index)
            self.index += 1
            return Sources.Supernova(ra, dec, redshift, doe, model,self.galaxy, nm)

class When(object):
    '''
    classdocs
    '''
    parameter_names = ['when.sim_start', 'when.sim_end']
    rate = 1. / 100. / 365.25  # 1 per century

    def __init__(self, sim_start, sim_end):
        '''
        Constructor
        '''
        self.sim_start = sim_start
        self.sim_end = sim_end

    def number(self, random_state, galaxy):

        expected = When.rate * (self.sim_end - self.sim_start)/(1 + galaxy.redshift)

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
    parameter_names = ["where.radius"]


    def __init__(self, radius):
        '''
        Constructor
        '''
        self.radius = radius

    def realize(self, random_state, galaxy):
        return (galaxy.ra, galaxy.dec) + random_state.normal(scale=self.radius,size=2)

class Realizer(object):
    '''
    Supernova realizer that generates objects given an input galaxy.  Supernovae are discovered
    with uniform probability over a time window given a constant local rate.  Supernovae
    are placed within a Gaussian distribution around the input gaalxy.  The supernova model
    is based on the interpolation of tabular (phase,wavelength,flux) data.
    
    The realizer instantiation is specified by a set of parameters
    
     seed                        seed for random number generator
     when.sim_start                start of time window in which SNe are generated
     when.sim_end                    end of time window in which SNe are generated
     where.radius                supernovae are randomly distributed in a Gaussian
                                 distribution around the galaxy with this sigma
     what.name                    name+'.pkl' is the file that contains (phase,wavelength,flux) information
     what.normalization        normalization applied to the flux in the file to give luminosity
    '''
    parameter_names = ['seed']
    parameter_names+=(When.parameter_names+Where.parameter_names+TabularSED.TabularSED.parameter_names)
    
    def __init__(self,pars):

        '''
        Constructor
        '''
        self.seed = pars[Realizer.parameter_names[0]]
        self.sim_start = pars[Realizer.parameter_names[1]]
        self.sim_end = pars[Realizer.parameter_names[2]]
        self.radius = pars[Realizer.parameter_names[3]]
        self.sedname = pars[Realizer.parameter_names[4]]
        self.normalization=pars[Realizer.parameter_names[5]]

        self.when = When(self.sim_start, self.sim_end)
        self.where = Where(self.radius)
        self.what = TabularSED.TabularSED(self.sedname, self.normalization)

    def realize(self, galaxy):

        return RealizerContainer(self, galaxy)
