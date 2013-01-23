'''
Created on Jan 21, 2013

@author: akim
'''

class Supernova(object):
    '''
    classdocs
    '''


    def __init__(self,ra,dec,redshift,doe,model,host,id):
        '''
        Constructor
        '''
        self.ra=ra
        self.dec=dec
        self.doe=doe
        self.redshift=redshift
        self.model=model
        self.host=host
        self.id=id
        
    def luminosity(self,date,wavelength):
        return self.model.luminosity((date-self.doe)/(1+self.redshift),wavelength)
    
class Galaxy(object):
    
    def __init__(self, ra, dec, redshift,name):
        self.ra = ra
        self.dec = dec
        self.redshift = redshift
        self.id=name
