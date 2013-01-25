'''
Created on Jan 21, 2013

@author: akim
'''

class Supernova(object):
    '''
    classdocs
    '''

    parameter_names = ['ra', 'dec', 'redshift', 'host', 'id', 'doe', 'model']

    def __init__(self, ra, dec, redshift, doe, model, host, id):
        '''
        Constructor
        '''
        self.pars = dict([['ra', ra], ['dec', dec], ['doe', doe], ['redshift', redshift], ['model', model], ['host', host], ['id', id]])

#        self.ra=ra
#        self.dec=dec
#        self.doe=doe
#        self.redshift=redshift
#        self.model=model
#        self.host=host
#        self.id=id

    def luminosity(self, obsdate, restwavelength):
        return self.pars['model'].luminosity((obsdate - self.pars['doe']) / (1 + self.pars['redshift']), restwavelength)

class Galaxy(object):

    def __init__(self, ra, dec, redshift, name):
        self.ra = ra
        self.dec = dec
        self.redshift = redshift
        self.id = name
