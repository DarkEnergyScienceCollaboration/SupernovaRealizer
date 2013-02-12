'''
Created on Jan 19, 2013

@author: akim
'''

import Sources
import TabularSED
import numpy
import Where
import When
import importlib


name = 'MyRealizer_ByHost'


class RealizerContainer(object):
    def __init__(self, realizer, logical):
        self.realizer = realizer
        self.logical = logical
        self.galaxyiterator = iter(self.realizer.galaxies)
        self.sniterator = iter(RealizerContainerByGalaxy(realizer, self.galaxyiterator.next()))
   #     print "Init ",self.sniterator.galaxy.id

    def __iter__(self):
        return self

    def next(self):
        done = False
        while not done:
            try:
                thenext = self.sniterator.next()
                if self.logical(thenext):
                    done=True
                    return thenext

            except StopIteration as e1:
                try:
                    nextgal = self.galaxyiterator.next()
                except StopIteration as e2:
                    raise StopIteration
                self.sniterator = iter(RealizerContainerByGalaxy(self.realizer, nextgal))

class RealizerContainerByGalaxy(object):
    def __init__(self, realizer, galaxy):
#        print realizer.seed, galaxy.id
        self.random_state = numpy.random.RandomState([realizer.seed, galaxy.id])

        self.realizer = realizer
        self.galaxy = galaxy
        self.nsn = self.realizer.when.number(self.random_state, self.galaxy.redshift)
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def next(self):
        if self.index >= self.nsn:
            raise StopIteration
        else:
            (ra, dec) = self.realizer.where.realize(self.random_state, (self.galaxy.ra,self.galaxy.dec))
            redshift = self.galaxy.redshift
            doe = self.realizer.when.realize(self.random_state, self.galaxy.redshift)
            model = self.realizer.what
            nm = (self.galaxy.id, self.index)
            self.index += 1
            return Sources.Supernova(ra, dec, redshift, doe, model, self.galaxy, nm)



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
 
    def __init__(self, galaxies, pars):

        '''
        Constructor
        '''
        self.galaxies = galaxies

        self.what=import_class(pars['what']['name'])(pars['what']['parameters'])
        self.when=import_class(pars['when']['name'])(pars['when']['parameters'])
        self.where = import_class(pars['where']['name'])(pars['where']['parameters'])

        self.parameter_names += (self.when.parameter_names + self.where.parameter_names + self.what.parameter_names)

        self.seed = pars['seed']
#        self.sim_start = pars[Realizer.parameter_names[1]]
#        self.sim_end = pars[Realizer.parameter_names[2]]
#        self.radius = pars[Realizer.parameter_names[3]]
#        self.sedname = pars[Realizer.parameter_names[4]]
#        self.normalization = pars[Realizer.parameter_names[5]]

        

    def realize(self, logical):

        return RealizerContainer(self, logical)

    def realizeByGalaxy(self, galaxy):

        return RealizerContainerByGalaxy(self, galaxy)
    
def import_class(cl):
    d = cl.rfind(".")
    classname = cl[d+1:len(cl)]
    m = __import__(cl[0:d], globals(), locals(), [classname])
    return getattr(m, classname)
