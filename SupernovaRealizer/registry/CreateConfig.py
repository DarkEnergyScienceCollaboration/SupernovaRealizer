'''
Created on Jan 16, 2013

@author: akim
'''
from configobj import ConfigObj
import numpy

filename='realizer.ini'

if __name__ == '__main__':
    config = ConfigObj()
    config.filename = filename
    #
    config['Realizer'] = {}
    
    config['Realizer']['name']= 'ByHost'
    
    config['Realizer']['parameters']={}
    
    config['Realizer']['parameters']['seed']=0
    config['Realizer']['parameters']['when.sim_start']=1000
    config['Realizer']['parameters']['when.sim_end']=1000+200*365.25
    config['Realizer']['parameters']['where.radius']=2./3600 
    config['Realizer']['parameters']['what.name']='data/snflux_1a.dat'
    config['Realizer']['parameters']['what.normalization']=numpy.power(10.,19./2.5) 

    config.write()