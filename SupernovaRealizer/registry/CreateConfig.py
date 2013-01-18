'''
Created on Jan 16, 2013

@author: akim
'''
import registry

from configobj import ConfigObj
filename=registry.Registry.configFileName

if __name__ == '__main__':
    config = ConfigObj()
    config.filename = filename
    #
    config['Realizers'] = {}
    
    config['Realizers']['TabularSED']= {}
    
    config['Realizers']['TabularSED']['sed_name']=0

    config['Realizers']['TabularSED']['nugget']=0

    config.write()