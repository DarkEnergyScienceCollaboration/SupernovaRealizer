'''
Created on Jan 22, 2013

@author: akim
'''
import Registry
import SupernovaRealizer.realizers.Sources
from configobj import ConfigObj
from validate import Validator


if __name__ == '__main__':

    # choose some galaxies to study
    galaxies = []
    for i in xrange(20):
        galaxies.append(SupernovaRealizer.realizers.Sources.Galaxy(1 + i * .1, 2 + i * .1, 0.1 + i * .1, i))

    # Read and validate configuration file that controls the simulation
    config = ConfigObj('realizer.ini', configspec='realizer_validation.ini')
    validator = Validator()
    result = config.validate(validator)
    realizername = config['Realizer']['name']
    pars = config['Realizer']['parameters']

    # Choose the realizer based on what was in the configuration file
    realizer = Registry.Registry.get_realizer(realizername, galaxies, pars)

    # get all supernovae
    print "All"
    for sn in realizer.realize(None):
        print '   Supernova ', sn.pars['ra'], sn.pars['dec'], sn.pars['redshift'], sn.pars['doe'], sn.pars['id']  # , sn.luminosity(sn.pars['doe']+30,5000)

    # get supernovae for one galaxy at a time
    print "By Galaxy ID"
    for galaxy in galaxies:
 #       print 'Galaxy id ',galaxy.id
        for sn in realizer.realize("pars['host'].id ==" + str(galaxy.id)):
            print '   Supernova ', sn.pars['ra'], sn.pars['dec'], sn.pars['redshift'], sn.pars['doe'], sn.pars['id']  # , sn.luminosity(sn.pars['doe']+30,5000)

    # get supernovae by coordinates
    print "By SN coordinates"
 #       print 'Galaxy id ',galaxy.id
    for sn in realizer.realize("pars['ra'] > 1.5"):
            print '   Supernova ', sn.pars['ra'], sn.pars['dec'], sn.pars['redshift'], sn.pars['doe'], sn.pars['id']  # , sn.luminosity(sn.pars['doe']+30,5000)
