'''
Created on Jan 16, 2013

@author: akim
'''

from configobj import ConfigObj

class Registry(object):
    '''
    classdocs
    '''

    configFileName='realizers.ini'

    def __init__(self):
        '''
        Constructor
        '''
        #The registry contains a list of instances of Realizers and knows about arguments.
        #This information is read it from a file.
        
        config = ConfigObj(Registry.configFileName)

        
        