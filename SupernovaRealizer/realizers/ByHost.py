'''
Created on Jan 19, 2013

@author: akim
'''

import numpy
import TabularSED

class Realizer(object):
    '''
    classdocs
    '''
    parameter_names=['seed']


    def __init__(self,seed,sim_start,sim_end):
        
        #worry about how galaxies get in later
        class Galaxy:
            def __init__(self,ra,dec):
                self.ra=ra
                self.dec=dec
        oneGalaxy=Galaxy(10,10)
        galaxies=[oneGalaxy,oneGalaxy,oneGalaxy]

        
        '''
        Constructor
        '''
        self.seed=seed
        self.sim_start=sim_start
        self.sim_end=sim_end
         
        
        numpy.random.seed(self.seed)
        subseeds=numpy.random.seed(high=None,size=2)
        self.when=When(subseeds(0),self.sim_start,self.sim_end)
        self.where=Where(subseeds(1))
        self.what=TabularSED.TabularSED('data/snflux_1a.dat')
        
    def realizeUniverse(self):
        return 0

class When(object):
    '''
    classdocs
    '''
    parameter_names=['seed','sim_start','sim_end']
    rate=1./100./365.25     #1 per century

    def __init__(self, seed, sim_start, sim_end):
        '''
        Constructor
        '''
        self.seed=seed
        self.sim_start=sim_start
        self.sim_end=sim_end
        
    def realize(self,galaxy):
        return 0
        
class Where(object):
    '''
    classdocs
    '''
    parameter_names=['seed']


    def __init__(self, seed):
        '''
        Constructor
        '''
        self.seed=seed
        
    def realize(self,galaxy):
        numpy.random.seed(self.seed+galaxy.id)
        return (galaxy.ra(),galaxy.dec())
    