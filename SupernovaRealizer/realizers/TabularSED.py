'''
Created on Jan 17, 2013

@author: akim
'''
import asciitable
import pickle
import numpy
from scipy.interpolate import griddata

class TabularSED(object):
    '''
    classdocs
    '''

    @staticmethod
    def ascii2pkl(name):
        name='data/test.dat'
        table=asciitable.read(name,delimiter="\s")
        points=numpy.zeros((len(table),2))
        for i in xrange(len(table)):
            points[i]=(table.col1[i],table.col2[i])
        values=table.col3
        f = open(name+'pkl', 'wb')
        pickle.dump(points,f,pickle.HIGHEST_PROTOCOL)
        pickle.dump(values,f,pickle.HIGHEST_PROTOCOL)
        f.close()
        
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name
        
        table=asciitable.read(name)
        
        #internal data members
        self.points= (table[0],table[1])
        self.values= table[2]
        
    def luminosity(self, phase, wavelength):
        
        return griddata(self.points, self.values, (phase,wavelength), method = 'linear')