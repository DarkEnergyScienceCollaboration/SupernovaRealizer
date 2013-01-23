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

    parameter_names = ['what.name','what.normalization']
    
    @staticmethod
    def ascii2pkl(name, phase):
        table = asciitable.read(name, delimiter="\s")
        points = numpy.zeros((len(table), 2))
        for i in xrange(len(table)):
            points[i] = (table.col1[i] - phase, table.col2[i])
        values = table.col3
        out = dict([('points', points), ('values', values)])
        f = open(name + '.pkl', 'wb')
        pickle.dump(out, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        
    def __init__(self, name, normalization):
        '''
        Constructor
        '''
        self.name = name
        self.normalization=normalization
        self.table = None
        
        
    def luminosity(self, phase, wavelength):
        if (self.table is None):
            f = open(self.name + '.pkl', 'rb')
            self.table = pickle.load(f)
        if (phase < self.table['points'][0][0] or phase > self.table['points'][-1][0] or wavelength < self.table['points'][0][1] or wavelength > self.table['points'][-1][1]):
            return 0
        return self.normalization*griddata(self.table['points'], self.table['values'], (phase, wavelength), method='linear')
