'''
Created on Jan 22, 2013

@author: akim
'''
import Registry
import SupernovaRealizer.realizers.Sources
from configobj import ConfigObj
from validate import Validator


if __name__ == '__main__':

    #Read and validate configuration file that controls the simulation
    config=ConfigObj('realizer.ini',configspec='realizer_validation.ini')
    validator = Validator()
    result = config.validate(validator)
    realizername=config['Realizer']['name']
    pars=config['Realizer']['parameters']

    #Choose the realizer based on what was in the configuration file
    realizer=Registry.Registry.get_realizer(realizername, pars)

    #choose some galaxies to study
    galaxies=[]
    for i in xrange(20):
        galaxies.append(SupernovaRealizer.realizers.Sources.Galaxy(1+i*.1,2+i*.1,0.1+i*.1,i))

    #get supernovae for each galaxy
    for galaxy in galaxies:
        print 'Galaxy id ',galaxy.id
        for sn in realizer.realize(galaxy):
            print '   Supernova ',sn.ra, sn.dec, sn.redshift, sn.doe, sn.id
    

    