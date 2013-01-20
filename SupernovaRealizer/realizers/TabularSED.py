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

    parameter_names=[]
    
    @staticmethod
    def ascii2pkl(name):
        table=asciitable.read(name,delimiter="\s")
        points=numpy.zeros((len(table),2))
        for i in xrange(len(table)):
            points[i]=(table.col1[i],table.col2[i])
        values=table.col3
        out=dict([('points', points), ('values', values)])
        f = open(name+'.pkl', 'wb')
        pickle.dump(out,f,pickle.HIGHEST_PROTOCOL)
        f.close()
        
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name
        self.table=None
        
        
    def luminosity(self, phase, wavelength):
        if (self.table is None):
            f=open(self.name+'.pkl','rb')
            self.table=pickle.load(f)
        return griddata(self.table['points'], self.table['values'], (phase,wavelength), method = 'linear')